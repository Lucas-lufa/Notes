external hard drive fix
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