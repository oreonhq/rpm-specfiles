%global source0_hash 00299c57d216ee3138f700fe3539e1bd0e3328bf18cfe891c3538b7408aa52f9
%define gittag 443e5fa
Name:      restool
Version:   2.4.0
Release:        1%{?dist}
Summary:        A tool to create and manage the DPAA2 Management Complex (MC)
License:   LicenseRef-Callaway-BSD OR GPL-2.0-or-later
URL:       https://github.com/nxp-qoriq/restool
Source0:        %{name}-%{version}-%{gittag}.tar.xz
Source1:   fsl_mc_bus.rules
ExclusiveArch: aarch64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pandoc
# /oreon:deps
%description
restool is a user space application providing the ability to dynamically
create and manage DPAA2 containers and objects from Linux.

restool interacts with the DPAA2 Management Complex (MC).  It uses an ioctl to
send MC commands, and thus requires a Linux kernel driver providing the needed
ioctl support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{make_build} EXTRA_CFLAGS="%{build_cflags} -Wno-error=maybe-uninitialized" LDFLAGS="%{build_ldflags}"
%install
%{make_install} prefix=%{_usr}
mkdir -p %{buildroot}/etc/udev/rules.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
