# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 00e4a87e87b7e7612f519a41e491f16623b12423620006f59f5688bfd8d13b08
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
