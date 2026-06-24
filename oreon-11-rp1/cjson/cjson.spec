%global source0_hash none

Name:           cjson
Version:        1.7.18
Release:        5%{?dist}
Summary:        Ultralightweight JSON parser in ANSI C

# several files in tests/ are Apache-2.0 but are not packaged
License:        MIT
URL:            https://github.com/DaveGamble/cJSON
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  gcc
BuildRequires:  cmake

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

%build
%cmake -DENABLE_CJSON_TEST=ON -DENABLE_TARGET_EXPORT=ON
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.{la,a}

%check
%ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig 

%files
%license LICENSE
%doc README.md
%{_libdir}/libcjson*.so.*
 
%files devel
%doc CHANGELOG.md CONTRIBUTORS.md
%{_libdir}/libcjson.so
%{_libdir}/pkgconfig/libcjson.pc
%{_libdir}/cmake/cJSON/
%{_includedir}/cjson/

%changelog
%autochangelog

