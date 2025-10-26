# file encoding
https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1702770

file -i /PATH/file.txt

# Add drive to system
need to add entry to fstab - file system table
located /etc/fatab
syntax - device directory type options dump fsck
Each option is separated by white space, if one of these options has options they are separated by commas (,).
 Device can be identified by it path dev/sd<a to z> or Universally Unique Identifier (UUID)
 Directory the mount point in the operating system.
 Type what file system is being used, in this case b-tree file system (BTRFS). Can let the computer guess by putting auto.
 Options there are file system dependent and independent options. Can have multiple options separated by commas.
 Dump is a utility that examines the file to see which ones needs to be backed up. 0 says it dose not need to be backed up.
 Fsck (File System Check) 0 dose not check.
To find the UUID of the partition lsblk -f . Where you want the drive to be mounted in the system, /mnt/data . The file system or auto. Don't really know the options selected. dump and fsck aren't needed so 0 0 . 
To use as a drive needed to change ownership - chown
 maybe could have use chmod or cgroups
# external hard drive fix
sudo ntfxfix /dev/sda1

ls -1
1 flag list one entry per line

to see if a user groups
id ${USER}

testdisk data recovery

# clonezilla

https://medium.com/@mikeycpham/using-clonezilla-to-image-and-getting-the-error-ntfclone-ng-c-ntfs-volume-dev-sd-is-7a467b617c4d
Using Clonezilla to image and getting the error ntfclone-ng-c: NTFS Volume ‘/dev/sd##’ is scheduled for a check or it was shutdown uncleanly. Please boot Windows or fix it by fsck.

boot into windows, restart, run cmd in administrator mode,
run chkdsk /F the F flag will force checkdisk to run on boot.
restart and checkdisk will run to fix the error 

# ventoy

df -h
umount /dev/sdb1
sudo sh Ventoy2Disk.sh -i /dev/

# yt-dlp

Download and merge the best video-only format and the best audio-only format,
or download the best combined format if video-only format is not available
$ yt-dlp -f "bv+ba/b"

yt-dlp -f 'bv*+ba'