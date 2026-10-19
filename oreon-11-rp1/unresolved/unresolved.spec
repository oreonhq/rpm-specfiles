%global source0_hash 8b788f717589cad7e26793b7d5e3f94903523dd5e9c1a9cdc431bdbd8324dc13
%global forgeurl0 %{url}
Name:           unresolved
Version:        0.1
Release:        1%{?dist}
Summary:        Remove systemd-resolved and have still working network
License:        GPL-3.0-only
URL:            https://github.com/pemensik/unresolved
%forgemeta
Source0:        https://github.com/pemensik/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       systemd
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
Simple tool fixing DNS resolution on system, when systemd-resolved
is no longer welcome. Disable or unistall the service, but also fix
network resolution to working state.

%package force
Summary:        Keep systemd-resolved out of your system
Conflicts:      systemd-resolved
BuildArch:      noarch
%description force
Make sure systemd-resolved is not allowed back to the system.
Use unresolved purge to uninstall it first.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

:
%install
install -m 755 unresolved -pD %{buildroot}%{_sbindir}/unresolved
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n unresolved-force -f %{oreon_filedir}/unresolved-force.list

%changelog

%autochangelog
