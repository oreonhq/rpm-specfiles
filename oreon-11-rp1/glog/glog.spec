Name:           glog
Version:        0.7.1
Release:        1%{?dist}
Summary:        A C++ application logging library
# main source code is BSD-3-Clause
# Apache-2.0
#   src/fuzz_demangle.cc
License:        BSD-3-Clause AND Apache-2.0
URL:            https://github.com/google/glog
Source0:        https://github.com/google/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 00e4a87e87b7e7612f519a41e491f16623b12423620006f59f5688bfd8d13b08
%global source0_file glog-0.7.1.tar.gz
# oreon url source checksums end

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel
BuildRequires:  cmake(gflags)


%description
Google glog is a library that implements application-level
logging. This library provides logging APIs based on C++-style
streams and various helper macros.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/glog-0.7.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "00e4a87e87b7e7612f519a41e491f16623b12423620006f59f5688bfd8d13b08" || { echo "oreon: Source0 SHA256 mismatch for glog-0.7.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup


%conf
%cmake -DWITH_PKGCONFIG=ON


%build
%cmake_build


%install
%cmake_install


%check
# upstream tests are cranky
# https://github.com/google/glog/issues/630
# https://github.com/google/glog/issues/709
# https://github.com/google/glog/issues/813
# https://github.com/google/glog/issues/887
%ctest --exclude-regex 'logging|stacktrace|symbolize'


%files
%license COPYING
%doc ChangeLog README.rst
%{_libdir}/libglog.so.%{version}
%{_libdir}/libglog.so.2


%files devel
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc
%{_includedir}/glog
%{_libdir}/cmake/glog


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.1-1
- Prepare for Oreon 11 (RP1)
