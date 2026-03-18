#!/bin/bash
set -eux

FAILANY=0
BOOTISO=/var/tmp/lorax-fedora-iso/images/boot.iso
KSNAME=fedora-minimal.ks
KS="/usr/share/doc/lorax/$KSNAME"
OUTISO=/var/tmp/out.iso
ISODIR=/var/tmp/iso
## Functions for testing mkkiso


function fail {
    echo -e "\n\n#### ERROR: $1\n"
    FAIL=1
    FAILANY=1
}

function status {
    if [ "$FAIL" -eq 0 ]; then
        echo -e "\n\n#### PASS: $1\n"
    else
        echo -e "\n\n#### FAIL: $1\n"
    fi
}

function running {
    FAIL=0
    echo -e "\n\n#### RUN: $1\n"
}

# unmount the dirs lazily because sometimes some outside thing is still touching them
function umount_dirs {
    umount --lazy "$ISODIR"
    rm -f "$OUTISO"
}

[ -e "$ISODIR" ] || mkdir "$ISODIR"

# Only add kickstart
function ks_only {
    running "Add kickstart to iso using --ks"

    mkksiso --ks $KS $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_ks

    status "Add kickstart to iso using --ks"
    umount_dirs
}

# Only add kickstart
function ks_pos_only {
    running "Add kickstart to iso using positional argument"

    mkksiso $KS $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_ks

    status "Add kickstart to iso using positional argument"
    umount_dirs
}

function test_ks {
    ## This all needs to be another function
    # Is there a kickstart in / of the iso?
    [ -e "$ISODIR/$KSNAME" ] || fail "Missing kickstart"

    # Is the kickstart in the GRUB2 BIOS config?
    grep "inst.ks=.*$KSNAME" "$ISODIR/boot/grub2/grub.cfg" || fail "Missing BIOS grub.cfg kickstart entry"

    # Is the kickstart in the UEFI config?
    grep "inst.ks=.*$KSNAME" "$ISODIR/EFI/BOOT/grub.cfg" || fail "Missing UEFI grub.cfg kickstart entry"
}

# Add ks and cmdline
function ks_serial {
    running "Add kickstart and serial cmdline"

    mkksiso -c "console=ttyS0,115200n8" --ks $KS $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_ks
    test_serial

    status "Add kickstart and serial cmdline"
    umount_dirs
}

# Only add serial console to cmdline
function only_serial {
    running "Add serial cmdline (no ks)"

    mkksiso -c "console=ttyS0,115200n8" $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_serial

    status "Add kickstart and serial cmdline"
    umount_dirs
}

function test_serial {

    # Is the serial in the BIOS config?
    grep "console=ttyS0,115200n8" "$ISODIR/boot/grub2/grub.cfg" || fail "Missing BIOS grub.cfg cmdline entry"

    # Is the serial in the UEFI config?
    grep "console=ttyS0,115200n8" "$ISODIR/EFI/BOOT/grub.cfg" || fail "Missing UEFI grub.cfg cmdline entry"
}

# New VOLID
function new_volid {
    running "Use a new VOLID"

    mkksiso -V "mkksiso-test" --ks $KS $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_ks
    test_volid

    status "Use a new VOLID"
    umount_dirs
}

function test_volid {
    # Is the VOLID in the BIOS config?
    grep "hd:LABEL=mkksiso-test" "$ISODIR/boot/grub2/grub.cfg" || fail "Missing BIOS grub.cfg kickstart entry"

    # Is the VOLID in the UEFI config?
    grep "hd:LABEL=mkksiso-test" "$ISODIR/EFI/BOOT/grub.cfg" || fail "Missing UEFI grub.cfg kickstart entry"
}

# Add extra files
function add_files {
    running "Add files"

    mkksiso -a /etc/services --ks $KS $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_ks
    test_files

    status "Add files"
    umount_dirs
}

# Remove quiet from the cmdline
function remove_quiet {
    running "remove quiet from cmdline (no ks)"

    mkksiso --rm "quiet"  $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_quiet

    status "Remove quiet from cmdline"
    umount_dirs
}

function test_quiet {
    # Is quiet in the BIOS config?
    ! grep "append.*quiet" "$ISODIR/boot/grub2/grub.cfg" || fail "quiet not removed from BIOS grub.cfg cmdline entry"

    # Is quiet in the UEFI config?
    ! grep "linux.*quiet" "$ISODIR/EFI/BOOT/grub.cfg" || fail "quiet not removed from UEFI grub.cfg cmdline entry"
}

# Test error if passing both --ks FILE and 3 arguments
function test_two_kickstarts {
    running "Test two kickstart error"

    mkksiso --ks $KS $KS $BOOTISO $OUTISO && fail "No error using --ks and positional argument"

    status  "Test two kickstart error"
}

function test_files {
    [ -e "$ISODIR/services" ] || fail "Missing file from iso"
}

# Test adding an updates.img file
function add_updatesimg {
    running "Add updates.img"

    # nothing in the file, just test that it is there
    touch /tmp/updates.img
    mkksiso -u /tmp/updates.img $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_updatesimg

    status "Add updates.img"
    umount_dirs
}

function test_updatesimg {
    [ -e "$ISODIR/updates.img" ] || fail "Missing updates.img file from iso"
    grep "inst.updates=.*updates.img" "$ISODIR/boot/grub2/grub.cfg" || fail "Missing BIOS grub.cfg inst.updates entry"
    grep "inst.updates=.*updates.img" "$ISODIR/EFI/BOOT/grub.cfg" || fail "Missing UEFI grub.cfg inst.updates entry"
}

# All of the changes
function run_all {
    running "Use all the options"

    touch /tmp/updates.img
    mkksiso -u /tmp/updates.img -a /etc/services -V "mkksiso-test" -c "console=ttyS0,115200n8" --rm "quiet"  --ks $KS $BOOTISO $OUTISO || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_ks
    test_serial
    test_volid
    test_files
    test_updatesimg
    test_quiet

    status "Use all the options"
    umount_dirs
}

# All of the changes as a user (lorax-ted) with --skip-mkefiboot
function run_as_user {
    running "Use all the options as a user"

    [ ! -e "/home/lorax-ted" ] && useradd -m lorax-ted
    touch /tmp/updates.img
    su - lorax-ted -c "mkksiso --skip-mkefiboot -u /tmp/updates.img -a /etc/services -V "mkksiso-test" -c "console=ttyS0,115200n8" --rm "quiet" --ks $KS $BOOTISO $OUTISO" || exit 1
    mount $OUTISO $ISODIR || exit 1

    test_ks
    test_serial
    test_volid
    test_files
    test_updatesimg
    test_quiet

    status "Use all the options as a user with --skip-mkefiboot"
    umount_dirs
}



# Gather up the list of system repo files and use them for lorax
REPOS=$(for f in /etc/yum.repos.d/*repo; do echo -n "--repo $f "; done)
if [ -z "$REPOS" ]; then
    echo "No system repos found"
    exit 1
fi

# NOTE: We must use --nomacboot because the test system doesn't have the hfsplus fs available
# Run lorax using the host's repository configuration file
if [ ! -e "$BOOTISO" ]; then
    running "Build boot.iso with lorax"
    lorax --product="Fedora" --version=rawhide --release=rawhide --volid="Fedora-rawhide-test" \
        $REPOS --isfinal --nomacboot /var/tmp/lorax-fedora-iso/ || exit 1
fi

# Test mkksiso on the new boot.iso
ks_only
ks_pos_only
ks_serial
only_serial
new_volid
add_files
remove_quiet
test_two_kickstarts
add_updatesimg
run_all
run_as_user

exit $FAILANY
