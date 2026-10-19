%global source0_hash 00c47b56a4dd5e80aba6b15df4e86d276a2a369737c6b467be1f51a9c29af31e
%bcond_without      tests
%bcond_with         licensecheck
%global libname     libsexpp
%global soname      0
Name:          sexpp
Summary:        S-expressions parser and generator tools
Version:       0.9.2
Release:        1%{?dist}
License:       MIT
URL:           https://github.com/rnpgp/%{name}
Source0:        https://github.com/rnpgp/%{name}/archive/refs/tags/v%{version}.tar.gz
Source3:       %{name}-files-by-license.txt
ExcludeArch:    %{ix86}
%if %{with licensecheck}
%endif
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
S-expressions parser and generator tools.

%package -n %{libname}
Summary:    S-expressions parser and generator library
%description -n %{libname}
%{libname} is a C++ library for working with S-expressions.

This implementation is derived from the reference SEXP C library developed by
Professors Ronald Rivest and Butler Lampson of MIT LCS (now CSAIL).

%package -n %{libname}-devel
Summary:    Header files and development libraries for %{libname}
Requires:   %{libname}%{?_isa} = %{version}-%{release}
%description -n %{libname}-devel
This package contains the header files and development libraries
for %{libname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%if %{with licensecheck}
LST=$(mktemp)

licensecheck -r . | sed -e 's:^./::' >$LST
grep -v UNKNOWN $LST | sed -e 's/.*: //' | sort -u | while read lic
do
    echo -e "\n$lic\n------------"
    grep ": $lic\$" $LST | sed -e "s/: $lic//"
done  | tee %{SOURCE3}
rm $LST
%endif

%build

%cmake . \
%if %{with tests}
   -DWITH_SEXP_TESTS:BOOL=ON \
%else
   -DWITH_SEXP_TESTS:BOOL=OFF \
%endif
   -DDOWNLOAD_GTEST:BOOL=OFF \
   -DWITH_SEXP_CLI:BOOL=ON \
   -DWITH_SANITIZERS:BOOL=OFF \
   -DWITH_COVERAGE:BOOL=OFF \
   -DBUILD_SHARED_LIBS:BOOL=ON \
   -DDOWNLOAD_GTEST:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n libsexpp -f %{oreon_filedir}/libsexpp.list
%files -n libsexpp-devel -f %{oreon_filedir}/libsexpp-devel.list

%changelog

%autochangelog
