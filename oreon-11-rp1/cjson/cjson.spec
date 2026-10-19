%global source0_hash 7fa616e3046edfa7a28a32d5f9eacfd23f92900fe1f8ccd988c1662f30454562
Name:           cjson
Version:        1.7.19
Release:        1%{?dist}
Summary:        Ultralightweight JSON parser in ANSI C
License:        MIT
URL:            https://github.com/DaveGamble/cJSON
Source0:        https://github.com/DaveGamble/cJSON/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
# /oreon:deps
%description
cJSON aims to be the dumbest possible parser that you can get your job
done with. It's a single file of C, and a single header file.
 
%package devel
Summary:        Development files for cJSON
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake-filesystem
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use cJSON.
  
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cJSON-%{version}
sed -i '1i #pragma GCC diagnostic ignored "-Wstringop-overread"' tests/misc_tests.c

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DENABLE_CJSON_TEST=ON -DENABLE_TARGET_EXPORT=ON -DCMAKE_C_FLAGS="-Wno-error=stringop-overread"
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.{la,a}
%oreon_autofiles cjson-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig 

%files -f %{oreon_filedir}/main.list
%files -n cjson-devel -f %{oreon_filedir}/cjson-devel.list

%changelog

%autochangelog

