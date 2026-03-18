Summary:        Google C++ testing framework
Name:           gtest
Version:        1.17.0

%global forgeurl https://github.com/google/googletest
%forgemeta

Release:        2%{?dist}
# scripts/generator/* are Apache-2.0
License:        BSD-3-Clause and Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python3-devel

%description
Framework for writing C++ tests on a variety of platforms (GNU/Linux,
Mac OS X, Windows, Windows CE, and Symbian). Based on the xUnit
architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, various options for running the tests, and XML test report
generation.

%package     -n gtest-devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gmock = %{version}-%{release}
%description -n gtest-devel
This package contains development files for %{name}.

%package     -n gmock
Summary:        Google C++ Mocking Framework
Requires:       %{name} = %{version}-%{release}
%description -n gmock
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++s
specifics in mind, Google C++ Mocking Framework (or Google Mock for
short) is a library for writing and using C++ mock classes.

Google Mock:

 o lets you create mock classes trivially using simple macros,
 o supports a rich set of matchers and actions,
 o handles unordered, partially ordered, or completely ordered
   expectations,
 o is extensible by users, and
 o works on Linux, Mac OS X, Windows, Windows Mobile, minGW, and
   Symbian.

%package     -n gmock-devel
Summary:        Development files for gmock
Requires:       gmock = %{version}-%{release}
%description -n gmock-devel
This package contains development files for gmock.

%prep
%forgeautosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON \
       -DPYTHON_EXECUTABLE=%{__python3} \
       -Dgtest_build_tests=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_libdir}/libgtest.so.%{version}
%{_libdir}/libgtest_main.so.%{version}

%files -n gtest-devel
%doc CONTRIBUTORS README.md
%doc docs/
%doc googletest/samples
%{_includedir}/gtest/
%{_libdir}/libgtest.so
%{_libdir}/libgtest_main.so
%{_libdir}/cmake/GTest/
%{_libdir}/pkgconfig/gtest.pc
%{_libdir}/pkgconfig/gtest_main.pc

%files -n gmock
%license LICENSE
%{_libdir}/libgmock.so.%{version}
%{_libdir}/libgmock_main.so.%{version}

%files -n gmock-devel
%doc CONTRIBUTORS README.md
%doc docs/
%{_includedir}/gmock/
%{_libdir}/libgmock.so
%{_libdir}/libgmock_main.so
%{_libdir}/pkgconfig/gmock.pc
%{_libdir}/pkgconfig/gmock_main.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-2
- Prepare for Oreon 11 (RP1)
