%global source0_hash 8b788f717589cad7e26793b7d5e3f94903523dd5e9c1a9cdc431bdbd8324dc13

%global forgeurl0 %{url}

Name:           unresolved
Version:        0.1
Release:        %autorelease
Summary:        Remove systemd-resolved and have still working network

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/pemensik/unresolved

%forgemeta
Source0:        %{forgesource0}

Requires:       systemd
BuildArch:      noarch

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

%files
%license LICENSE
%doc README.md
%{_sbindir}/unresolved

%files force
%license LICENSE

%changelog
%autochangelog
