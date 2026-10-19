%global source0_hash e629d2f3e500ffa5df6f1b1689161ab3dea3a82f66beec2b453a74b8d782f949
%global catch_version 2.13.10
%global libosmium_version 2.23.0
%global protozero_version 1.6.3
%global json_version 3.0
Name:           osmium-tool
Version:        1.19.1
Release:        1%{?dist}
Summary:        Command line tool for working with OpenStreetMap data
License:        GPL-3.0-only
URL:            http://osmcode.org/osmium-tool/
Source0:        https://github.com/osmcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          osmium-tool-bigendian.patch
Patch:          osmium-tool-zlibng.patch
# oreon:deps
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  json-devel
BuildRequires:  json-static
BuildRequires:  libosmium-devel
BuildRequires:  libosmium-static
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  pandoc
BuildRequires:  protozero-devel
BuildRequires:  protozero-static
# /oreon:deps
%description
Command line tool for working with OpenStreetMap data
based on the Osmium library

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git
sed -i -e "s/-O3 -g//" CMakeLists.txt
rm -rf include/rapidjson test/include/catch.hpp
ln -sf /usr/include/catch2/catch.hpp test/include

%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
install -p -m644 zsh_completion/* %{buildroot}%{_datadir}/zsh/site-functions
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
