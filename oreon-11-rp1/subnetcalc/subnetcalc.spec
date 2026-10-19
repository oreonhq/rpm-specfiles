%global source0_hash aa0a006c2dc6cb2de890a79971fbd5fda26a531a77addd1c6644c49e9f3ef4f5
Name:           subnetcalc
Version:        2.7.5
Release:        1%{?dist}
Summary:        IPv4/IPv6 Subnet Calculator
License:        GPL-3.0-or-later
URL:            https://www.nntb.no/~dreibh/subnetcalc/
Source0:        https://www.nntb.no/~dreibh/subnetcalc/download/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  GeoIP-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
# /oreon:deps
%description
SubNetCalc is an IPv4/IPv6 subnet address calculator. For given IPv4 or IPv6 
address and netmask or prefix length, it calculates network address, broadcast
address, maximum number of hosts and host address range. Also, it prints the 
addresses in binary format for better understandability. Furthermore, it 
prints useful information on specific address types (e.g. type, scope, 
interface ID, etc.).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
