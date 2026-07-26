#!/bin/bash
# this utility should take the boot params from existing
# loader entries files (from anaconda+linux-kernel install)
# which should be a clone of the machine's /proc/cmdline
# and removes the "inst." options "BOOT_IMG="
# and then merges it with the /etc/kernel/cmdline
# which is generated from anaconda
#
# It also acts as a lightweight grubby for
# printing kernel paths, and updating individual bls entries.
# Its largely intended to shim kdumpctl->grubby and anaconda
# any usefulness beyond that is a bonus.
progname=`basename $0`
utilmode="help"
modify_args=""

# sed and awk invocations for manipulating loader entries and bootctl output
BOOTCTL_TO_GRUBBY_INFO="sed -e \"s/ *options: /args:=/g\"  -e \"s/ *linux: /kernel:=/g\" -e \"s/ *initrd: /initrd:=/g\" -e \"s/ *id: /id:=/g\" -e \"s/ *title: /title:=/g\""
BOOTCTL_REMOVE_UNUSED="sed -e \"/source:/d\" -e \"/machine-id:/d\" -e \"/type:/d\" -e \"/sort-key:/d\" -e \"/version:/d\""
BOOTCTL_QUOTING="sed -e \"s/^\(.*\):=\(.*\)/\\1=\\\"\\2\\\"/\""
FIXCMDLINE='
/^options/ {
  for (i=2;i<=NF;i++) {
    if ($i ~ /^BOOT_IMAGE/)
      continue;
    if ($i ~ /^inst\./)
      continue;
    options[$i] = "1"
  }
  # merge /etc/kernel/cmdline
  while (getline<"/etc/kernel/cmdline") {
    for (i=1;i<=NF;i++) {
        options[$i] = "1"
    }
  }
  printf "options    "
  for (i in options)
      printf "%s ",i
  printf "\n"
  next
}
{ print }
'
CAPTUREROOT='
/options: / {
  for (i=1;i<=NF;i++) {
    if ($i ~ /root=/)
        print "root=\"" substr($i,6) "\""
  }
}
{ print }
'

[[ $? = 0 ]] || exit 1

if [[ "$progname" == "updateloaderentries" ]]; then
    utilmode="merge"
fi


OPTS="$(getopt -o hc:i:b:? --long help,args:,info:,update-kernel:,remove-args:,default-kernel -- "$@")"

eval set -- "$OPTS"

while [ ${#} -gt 0 ]; do
    case "$1" in
	--help)
	    utilmode="help"
	    ;;
	--info)
	    info_kernel="$2"
	    utilmode="info"
	    shift 1
	    ;;
	--args)
	    modify_args="$2"
	    utilmode="add"
	    shift 1
	    ;;
	--remove-args)
	    modify_args="$2"
	    utilmode="remove"
	    shift 1
	    ;;
	--update-kernel)
	    info_kernel="$2"
	    shift 1
	    ;;
	--default-kernel)
	    utilmode="defaultkernel"
	    ;;
    esac
    shift
done

if [[ "$info_kernel" == "ALL" ]]; then
    unset info_kernel
fi

case "$utilmode" in
    help)
	echo "updateloaderentries.sh: When run as updateloaderentries it doesn't require any parameters and merges"
	echo "                        The /etc/kernel/cmdline and /proc/cmdline into all systemd-boot configurations."
	echo "grubby: When run symlinked as grubby, it takes the grubby --args, --remove-args and --info"
	echo "        switches. All three take a uname -r compatible option to specify the kernel/initrd"
	echo "        being modified/shown or ALL."
	;;
    remove)
	config_file=`bootctl list |grep -B7 -A2 ".*linux:.*${info_kernel}"|grep "^.*source:" |cut -d: -f2- `
	sed -i -e "s/^options\(.*\) ${modify_args}/options\\1/" $config_file
	;;
    add)
	config_file=`bootctl list |grep -B7 -A2 ".*linux:.*${info_kernel}"|grep "^.*source:" |cut -d: -f2- `
	for fn in $config_file; do
	    grep ${modify_args} $fn >/dev/null
	    if [[ "$?" == "1" ]]; then
		sed -i -e "s/^options    /options    ${modify_args} /" $fn
	    fi
	done
	;;
    info)
	bootctl list | grep -B7 -A2 ".*linux:.*$info_kernel" | awk "$CAPTUREROOT" | eval "${BOOTCTL_REMOVE_UNUSED}" | eval "${BOOTCTL_TO_GRUBBY_INFO}" | eval "${BOOTCTL_QUOTING}"
	;;
    defaultkernel)
	bootctl list |grep -A6 ".*title:.*(default)" | grep "linux:" | cut -c16-
	;;
    merge)
	for i in /boot/efi/loader/entries/*; do
	    if [[ -f "$i" ]]; then
		/usr/bin/awk -i inplace "$FIXCMDLINE" "$i";
	    fi
	done
        
        # just in case, relink if needed
        if ! [[ -e /sbin/installkernel ]]; then
	    /usr/bin/ln -s /usr/bin/kernel-install /sbin/installkernel
        fi
        if ! [[ -e /sbin/grubby ]]; then
            /usr/bin/ln -s /sbin/updateloaderentries /sbin/grubby
        fi
        ;;
esac

