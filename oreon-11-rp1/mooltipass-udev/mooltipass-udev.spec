%global source0_hash 00285402ecf887da2a938d8375725fd07553c1ad11e426659a72c42dc0027c82

Name:           mooltipass-udev
Version:        2023011200
Release:        %autorelease
Summary:        Udev rules for Mooltipass devices

License:        GPL-3.0-or-later
URL:            https://github.com/mooltipass/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        mooltipass-udev-gpgkey.gpg
BuildArch:      noarch

Requires:       udev

BuildRequires:  gnupg2
# for _udevrulesdir macro
BuildRequires:  systemd-rpm-macros

Conflicts:      moolticute <= 1.00.1-4

%description
Udev rules to allow user access to Mooltipass devices for use with Moolticute.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# Nothing to build

%install
install -Dpm 0644 udev/69-mooltipass.rules %{buildroot}%{_udevrulesdir}/69-mooltipass.rules

%files
%license license.txt
%doc README.md
%{_udevrulesdir}/69-mooltipass.rules

%changelog
%autochangelog
