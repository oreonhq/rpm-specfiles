%global source0_hash e358b5cdecdbc6bac959dfa27efbdd24aec3d8b42fdc69162262798aa19b525b

Name: netrate
Version: 0.1
Release: 11%{?dist}
Summary: Network interface traffic meter
License: GPL-2.0-only
URL: https://github.com/mindbit/netrate
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: make

%description
netrate is a simple program that displays real-time byte and packet
count rate of network interfaces in Linux systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build -C src

%install
%make_install -C src

%files
%{_bindir}/netrate
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
