%global source0_hash 3b8f0a1bf0d3642764e5f646e1f3bbc8b1eeec474a77392d9aeb4868842b4cca

Name:       vconfig
Version:    1.9
Release:    41%{?dist}
Summary:    Linux 802.1q VLAN configuration utility
# candela_2.4.21.patch:             GPL-2.0-or-later
# contrib/vlan_2.2-full.patch:      GPL-2.0-or-later
# contrib/vlan_2.2-module.patch:    GPL-2.0-or-later
# howto.html:       "part of the Linux HOWTO project", "see [...] GNU GPL 0.1.1"
# macvlan_config.c: GPL-2.0-or-later
# vconfig.c:        GPL-2.0-or-later
# vlan_2.2.patch:   GPL-2.0-or-later
License:    GPL-2.0-or-later
URL:        https://www.candelatech.com/~greear/vlan.html
# The URL now returns a bogus file full of zeros
Source:     https://www.candelatech.com/~greear/vlan/vlan.%{version}.tar.gz
# Fix a security warning by compiler, bug #1037376
Patch0:     %{name}-1.9-Pass-compilation-with-Werror-format-security.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make

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

%files 
%doc CHANGELOG README vlan.html vlan_test.pl
%{_sbindir}/vconfig
%{_mandir}/man8/vconfig.8*

%changelog
%autochangelog
