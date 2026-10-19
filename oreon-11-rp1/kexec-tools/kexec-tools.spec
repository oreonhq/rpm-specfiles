%global source0_hash 8f81422a5fd2362cf6cb001b511e535565ed0f32c2f4451fb5eb68fed6710a5d
Name: kexec-tools
Version: 2.0.32
Release:        1%{?dist}
URL: https://kernel.org/pub/linux/utils/kernel/kexec
License: GPL-2.0-only
Summary:        The kexec/kdump userspace component
Source0:        https://kernel.org/pub/linux/utils/kernel/kexec/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
kexec-tools provides /sbin/kexec binary that facilitates a new
kernel to boot using the kernel's kexec feature either on a
normal or a panic reboot. This package contains the /sbin/kexec
binary and ancillary utilities that together form the userspace
component of the kernel's kexec feature.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.32-3
- Prepare for Oreon 11 (RP1)
