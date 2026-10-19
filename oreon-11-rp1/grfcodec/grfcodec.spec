%global source0_hash 20448dac4032377ed75f8ddace0192f3c57bdc1b798c76c4f3566135c3b3572a
Version:       6.2.0
%global tag %{version}
%global forgeurl https://github.com/OpenTTD/grfcodec
%forgemeta
Name:           grfcodec
Release:        1%{?dist}
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  zlib-ng-compat-devel
# /oreon:deps
%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
