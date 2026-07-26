%global source0_hash 2ed81ecb86da44d571f950010dc174fe6d702a9942259c7c2890fdfc025e4b9c

Name:           cura-fdm-materials
Version:        5.4.0
Release:        %autorelease
Summary:        Cura FDM Material database

# See https://github.com/Ultimaker/Cura/issues/1779 for clarification
License:        LicenseRef-Fedora-Public-Domain

URL:            https://github.com/Ultimaker/fdm_materials
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2:        CMakeLists.txt
Source3:        CPackConfig.cmake

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
Requires:       cura >= 1:%{version}

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

%files
%license LICENSE
%{_datadir}/cura/resources/materials/

%changelog
%autochangelog
