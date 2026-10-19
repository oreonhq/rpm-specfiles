%global source0_hash bb4060bddb3fa87eaf58ac3427097fff46d79a6142037380c624636f705174df
Name:           cura-fdm-materials
Version:        5.13.0
Release:        1%{?dist}
Summary:        Cura FDM Material database
License:        LicenseRef-Fedora-Public-Domain
URL:            https://github.com/Ultimaker/fdm_materials
Source0:        https://github.com/Ultimaker/fdm_materials/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        CMakeLists.txt
Source3:        CPackConfig.cmake
BuildArch:      noarch
ExcludeArch:    %{ix86}
Requires:       cura >= 1:%{version}
# oreon:deps
BuildRequires:  cmake
# /oreon:deps
%description
Cura material files.

These files are needed to work with printers like Ultimaker 2+ and Ultimaker 3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fdm_materials-%{version} -p1

rm -rf CMakeLists.txt
cp %{SOURCE2} %{SOURCE3} .

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
