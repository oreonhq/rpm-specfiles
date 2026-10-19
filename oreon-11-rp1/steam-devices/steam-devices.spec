%global source0_hash bdb2c063c741538703267c883afaaae7a0d2cf40d51de52ce76a4bd667005bc0
%global commit e0ab31454b1c55468af14d08740b51f11581a324
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20260123
Name:           steam-devices
Version:        1.0.0.101^git%{commitdate}.%{shortcommit}
Release:        7%{?dist}
License:        MIT
Summary:        Device support for Steam-related hardware
Url:            https://github.com/ValveSoftware/steam-devices/
Source0:        https://github.com/ValveSoftware/%{name}//archive/%{commit}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      steam-devices < %{version}-%{release}
Provides:       steam-devices = %{version}-%{release}
# oreon:deps
BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package contains the necessary permissions for gaming devices (such as
gamepads, joysticks and VR headsets) that can be used by Wine, Lutris, Heroic,
and other non-Steam games and game launchers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -S git_am

%install
install -Dpm0644 60-steam-input.rules %{buildroot}%{_udevrulesdir}/60-steam-input.rules
install -Dpm0644 60-steam-vr.rules %{buildroot}%{_udevrulesdir}/60-steam-vr.rules
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
