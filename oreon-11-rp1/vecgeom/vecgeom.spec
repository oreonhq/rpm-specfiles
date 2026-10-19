%global source0_hash 5143f1357b4a385f379cda4b51b16adb92f98c7e7e396feeb826c1945a6b7ea4
%bcond check 0
%global forgeurl https://gitlab.cern.ch/VecGeom/VecGeom
Version:        2.1.1
%global tag v%{version}
%forgemeta
Name:           vecgeom
Release:        1%{?dist}
Summary:        A vectorized geometry library for particle-detector simulation
License:        Apache-2.0 AND MIT AND (Apache-2.0 OR MIT)
URL:            %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{tag}/VecGeom-%{tag}.tar.bz2
Patch0:         vecgeom-add-soversion.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(veccore)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xerces-c)
# /oreon:deps
%description
VecGeom is a geometry modeller library with hit-detection features as needed by
particle detector simulation at the LHC and beyond. It was incubated by a
Geant-R&D initiative and the motivation to combine the code of Geant4 and
ROOT/TGeo into a single, better maintainable piece of software within the
EU-AIDA program. As such it is close in scope to TGeo and Geant4 geometry
modellers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake \
    -GNinja \
    -DVECGEOM_GDML=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ifarch x86_64
%ctest
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n vecgeom-devel -f %{oreon_filedir}/vecgeom-devel.list

%changelog

%autochangelog
