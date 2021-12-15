#!/bin/bash

LOCAL_BACKUP_DIR='/path/to/Addons'
ADDONS_ZIP_FILE_FILTER='prod-addons-backup-'
ADDONS_PARENT_DIRECTORY='/usr/local/lib/python2.7/dist-packages/openerp-server/'
BACKUP_SERVER_USER=USERNAME
BACKUP_SERVER_IP=SERVER_IP_ADDRESS
BACKUP_SERVER_PATH='/home/username/db_backup/'
BACKUP_SERVER_DIR_PATH=$BACKUP_SERVER_USER@$BACKUP_SERVER_IP:$BACKUP_SERVER_PATH
BACKUP_SERVER_MP=/mnt/backup-server


do_unmount_back_server()
{
	`sudo umount "${BACKUP_SERVER_MP}"`
}

do_script_backup()
{
        DATE_STR=$(date +'%y-%m-%d-%T')
        $(`cd "${ADDONS_PARENT_DIRECTORY}" && zip -r "${LOCAL_BACKUP_DIR}"/"${ADDONS_ZIP_FILE_FILTER}""${DATE_STR}".zip addons -x *.git*`)
}

do_mount_backup_server()
{
	set -- $(`sudo sshfs -o allow_other,IdentityFile=~/.ssh/id_rsa "${BACKUP_SERVER_DIR_PATH}" "${BACKUP_SERVER_MP}"`)
}

copy_local_backup_files_to_backup_server()
{
        ls -t "${LOCAL_BACKUP_DIR}" | grep -q "${FILE_FILTER}" && $(`sudo rsync -r --append-verify "${LOCAL_BACKUP_DIR}"/* "${BACKUP_SERVER_MP}"/`)
}

delete_addons_archive()
{
	$(rm  "${LOCAL_BACKUP_DIR}"/"${ADDONS_ZIP_FILE_FILTER}""${DATE_STR}".zip)
}

do_script_backup

mount | grep -q "${BACKUP_SERVER_DIR_PATH}" || $(do_mount_backup_server)

mount | grep -q "${BACKUP_SERVER_DIR_PATH}" && $(copy_local_backup_files_to_backup_server)

mount | grep -q "${BACKUP_SERVER_DIR_PATH}" &&  $(do_unmount_back_server)

delete_addons_archive

exit 0
