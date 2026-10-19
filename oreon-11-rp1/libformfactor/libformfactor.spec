%global source0_hash b01b52157ccbb74a8711f9b935a5f6426603186756502aba6f31b5790107f978
Name:           libformfactor
Version:        0.5.1
Release:        1%{?dist}
Summary:        Efficient computation of scattering form factors of arbitrary polyhedra
License:        GPL-3.0-or-later
URL:            https://jugit.fz-juelich.de/mlz/libformfactor
Source0:        https://jugit.fz-juelich.de/mlz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(LibHeinz)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
A C++ library for the efficient computation of scattering form factors
(Fourier shape transforms) of arbitrary polyhedra according to Joachim Wuttke,
[J Appl Cryst 54, 580-587 (2021)](https://doi.org/10.1107/S1600576721001710).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

sed -i 's|DESTINATION lib|DESTINATION %{_libdir}|g' ff/CMakeLists.txt
sed -i 's|DESTINATION cmake|DESTINATION %{_libdir}/cmake/formfactor|g' CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libformfactor-devel -f %{oreon_filedir}/libformfactor-devel.list

%changelog

%autochangelog
