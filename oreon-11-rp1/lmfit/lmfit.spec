%global source0_hash 5289b1264f82cd9a62d445848dc17d2fce1cdc0079b24594f52d87c12e1ac716
Name:           lmfit
Version:        11.0
%global         sover 10
Release:        1%{?dist}
Summary:        Levenberg-Marquardt least-squares minimization and curve fitting
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-CC-BY
URL:            https://jugit.fz-juelich.de/mlz/lmfit
Source0:        https://jugit.fz-juelich.de/mlz/lmfit/-/archive/v%{version}/lmfit-v%{version}.tar.bz2
# oreon:deps
BuildRequires:  //bin/pod2html
BuildRequires:  //bin/pod2man
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
C/C++ library for Levenberg-Marquardt least-squares minimization and curve
fitting

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}
cp -ra demo _demo

# install to libdir
sed -i 's@DESTINATION lib@DESTINATION %{_lib}@' lib/CMakeLists.txt CMakeLists.txt

%build

%{cmake}
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_mandir}/html %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/*.la
rm -rf demo
mv -f _demo demo
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n lmfit-devel -f %{oreon_filedir}/lmfit-devel.list

%changelog

%autochangelog
