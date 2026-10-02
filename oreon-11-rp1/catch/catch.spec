%global source0_hash 0957cae5821b17ce07f0833aaa52b5137643a8382203221f363a8303c109af34

Name:           catch
Version:        3.16.0
Release:        1%{?dist}
Summary:        Modern C++ unit test and micro-benchmark framework
License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
Source0:        https://github.com/catchorg/Catch2/archive/v%{version}/Catch2-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  python3

%description
Catch2 is a C++ unit testing and micro-benchmarking framework.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Libraries and headers for applications using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Catch2-%{version}

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCATCH_BUILD_EXTRA_TESTS=ON \
    -DCATCH_ENABLE_WERROR=OFF \
    -DCATCH_INSTALL_DOCS=OFF \
    -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%{_libdir}/libCatch2.so.%{version}
%{_libdir}/libCatch2Main.so.%{version}

%files devel
%doc README.md docs
%{_includedir}/catch2/
%{_libdir}/libCatch2.so
%{_libdir}/libCatch2Main.so
%{_libdir}/cmake/Catch2/
%{_datadir}/Catch2/
%{_datadir}/pkgconfig/catch2.pc
%{_datadir}/pkgconfig/catch2-with-main.pc

%changelog
%autochangelog
