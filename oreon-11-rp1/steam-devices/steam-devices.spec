%global source0_hash bdb2c063c741538703267c883afaaae7a0d2cf40d51de52ce76a4bd667005bc0

%global commit e0ab31454b1c55468af14d08740b51f11581a324
%if 0%{?rhel} && 0%{?rhel} < 10
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%else
%global shortcommit %{sub %{commit} 1 7}
%endif
%global commitdate 20260123

Name:           steam-devices
Version:        1.0.0.101^git%{commitdate}.%{shortcommit}
Release:        7%{?dist}
License:        MIT
Summary:        Device support for Steam-related hardware
Url:            https://github.com/ValveSoftware/steam-devices/
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros

# Temporary workaround to obsolete and replace the equivalent i686 package in RPMFusion
# so we don't break current installs. Can be removed after a while.
Obsoletes:      steam-devices < %{version}-%{release}
Provides:       steam-devices = %{version}-%{release}

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

%files
%license LICENSE
%{_udevrulesdir}/60-steam-input.rules
%{_udevrulesdir}/60-steam-vr.rules

%changelog
%autochangelog
