%global source0_hash c70432afdfff2453a72d92ce66dd1c1a1c50511ebe014e10be3853d5a80aeb0f
Name: netrate
Version: 0.1
Release:        11%{?dist}
Summary:        Network interface traffic meter
License: GPL-2.0-only
URL: https://github.com/mindbit/netrate
Source0:        https://github.com/mindbit/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
netrate is a simple program that displays real-time byte and packet
count rate of network interfaces in Linux systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build -C src
%install
%make_install -C src
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
