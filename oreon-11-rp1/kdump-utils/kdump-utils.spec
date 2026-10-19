%global source0_hash 9d55e23ee279154b1023fa92095938a07155ea07db546881e9a1d91bae2e1b16
%global debug_package %{nil}
Name: kdump-utils
Version: 1.0.61
Release:        1%{?dist}
Summary:        Kernel crash dump collection utilities
License: GPL-2.0-only
URL: https://github.com/rhkdump/kdump-utils
Source0:        https://github.com/rhkdump/kdump-utils/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%ifarch ppc64 ppc64le
Requires(post): servicelog
Recommends: keyutils
%endif
Requires(pre): coreutils
Requires(pre): sed
Requires: kexec-tools >= 2.0.28-8
Requires: makedumpfile
Requires: dracut >= 058
Requires: dracut-network >= 058
Requires: dracut-squash >= 058
Requires: ethtool
Requires: gawk
Requires: util-linux
Recommends: grubby
Recommends: hostname
%ifnarch s390x
Requires: systemd-udev%{?_isa}
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
kdump-utils is responsible for collecting the crash kernel dump. It builds and
loads the kdump initramfs so when a kernel crashes, the system will boot the
kdump kernel and initramfs to save the collected crash kernel dump to specified
target.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
%make_install sbindir=%_sbindir
%oreon_autofiles main

%post

%systemd_post kdump.service
touch /etc/kdump.conf
%ifarch ppc64 ppc64le
servicelog_notify --remove --command=/usr/lib/kdump/kdump-migrate-action.sh 2>/dev/null
servicelog_notify --add --command=/usr/lib/kdump/kdump-migrate-action.sh --match='refcode="#MIGRATE" and serviceable=0' --type=EVENT --method=pairs_stdin >/dev/null
%endif
:
%postun

%systemd_postun_with_restart kdump.service
%preun

%ifarch ppc64 ppc64le
servicelog_notify --remove --command=/usr/lib/kdump/kdump-migrate-action.sh >/dev/null
%endif
%systemd_preun kdump.service
%posttrans

if [ ! -f /run/ostree-booted ] && [ $1 == 1 -o $1 == 2 ]; then
  kdumpctl _reset-crashkernel-after-update
  :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
