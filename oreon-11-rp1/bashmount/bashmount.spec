%global source0_hash 4fa5be39b10c3ce24f3f21ff6605ce0499ab9b24baf1b5762be36b9003eab169
Name:              bashmount
Version:           4.3.2
Release:        15%{?dist}
Summary:        A menu-driven bash script for mounting removable media
License:           GPL-2.0-only
URL:               https://github.com/jamielinux/bashmount
Source0:        https://github.com/jamielinux/bashmount/archive/%{version}.tar.gz
BuildArch:         noarch
Requires:          bash
Requires:          sed
Requires:          udisks2
Requires:          util-linux
# oreon:deps

# /oreon:deps
%description
bashmount is a menu-driven bash script that uses udisks2 to easily mount,
unmount or eject removable devices without dependencies on any GUI or
desktop environment. An extensive configuration file allows custom commands
to be run on devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
install -p -D -m755 bashmount \
    %{buildroot}%{_bindir}/bashmount
install -p -D -m644 bashmount.conf \
    %{buildroot}%{_sysconfdir}/bashmount.conf
install -p -D -m644 bashmount.1 \
    %{buildroot}%{_mandir}/man1/bashmount.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
