Name: kexec-tools
Version: 2.0.32
Release: 3%{?dist}
URL: https://kernel.org/pub/linux/utils/kernel/kexec
License: GPL-2.0-only
Summary: The kexec/kdump userspace component

Source0: https://kernel.org/pub/linux/utils/kernel/kexec/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 8f81422a5fd2362cf6cb001b511e535565ed0f32c2f4451fb5eb68fed6710a5d
%global source0_file kexec-tools-2.0.32.tar.xz
# oreon url source checksums end

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel

#START INSERT

#
# Patches 0 through 100 are meant for x86 kexec-tools enablement
#

#
# Patches 101 through 200 are meant for x86_64 kexec-tools enablement
#

#
# Patches 301 through 400 are meant for ppc64 kexec-tools enablement
#

#
# Patches 401 through 500 are meant for s390 kexec-tools enablement
#

#
# Patches 501 through 600 are meant for ARM kexec-tools enablement
#

#
# Patches 601 onward are generic patches


%description
kexec-tools provides /sbin/kexec binary that facilitates a new
kernel to boot using the kernel's kexec feature either on a
normal or a panic reboot. This package contains the /sbin/kexec
binary and ancillary utilities that together form the userspace
component of the kernel's kexec feature.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/kexec-tools-2.0.32.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8f81422a5fd2362cf6cb001b511e535565ed0f32c2f4451fb5eb68fed6710a5d" || { echo "oreon: Source0 SHA256 mismatch for kexec-tools-2.0.32.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
autoreconf
%configure \
%ifarch ppc64
    --host=powerpc64-redhat-linux-gnu \
    --build=powerpc64-redhat-linux-gnu \
%endif
%ifarch ppc64le
    --host=powerpc64le-redhat-linux-gnu \
    --build=powerpc64le-redhat-linux-gnu \
%endif
    --sbindir=%{_sbindir}

%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/kexec-tools/kexec_test


%files
%{_sbindir}/kexec
%{_mandir}/man8/kexec.8*
%{_sbindir}/vmcore-dmesg
%{_mandir}/man8/vmcore-dmesg.8*
%doc News
%license COPYING
%doc TODO

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.32-3
- Prepare for Oreon 11 (RP1)
