%global source0_hash 176234eb38d4971496c5054b9b5f89566e3f2db2e37a841c9820f576dc2fd98c
Name:       vconfig
Version:    1.9
Release:        41%{?dist}
Summary:        Linux 802.1q VLAN configuration utility
License:    GPL-2.0-or-later
URL:        https://www.candelatech.com/~greear/vlan.html
Source0:        https://www.candelatech.com/~greear/vlan/vlan.%{version}.tar.gz
Patch0:     %{name}-1.9-Pass-compilation-with-Werror-format-security.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description 
The vconfig program configures and adjusts 802.1q VLAN parameters.
This tool is deprecated in favor of "ip link" command.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n vlan
%patch -P0 -p1 -b .warning

%build

make clean
rm -f vconfig
make CCFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" STRIP=/bin/true vconfig
%install
install -D -m755 vconfig ${RPM_BUILD_ROOT}%{_sbindir}/vconfig
install -D -m644 vconfig.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/vconfig.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
