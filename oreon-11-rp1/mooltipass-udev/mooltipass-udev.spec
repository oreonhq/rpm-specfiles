%global source0_hash 00285402ecf887da2a938d8375725fd07553c1ad11e426659a72c42dc0027c82
Name:           mooltipass-udev
Version:        2023011200
Release:        1%{?dist}
Summary:        Udev rules for Mooltipass devices
License:        GPL-3.0-or-later
URL:            https://github.com/mooltipass/%{name}
Source0:        https://github.com/mooltipass/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        mooltipass-udev-gpgkey.gpg
BuildArch:      noarch
Requires:       udev
Conflicts:      moolticute <= 1.00.1-4
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Udev rules to allow user access to Mooltipass devices for use with Moolticute.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%install
install -Dpm 0644 udev/69-mooltipass.rules %{buildroot}%{_udevrulesdir}/69-mooltipass.rules
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
