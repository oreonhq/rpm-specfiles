%global source0_hash 9631341c82bac4a288bef951f8b26b41f69021794184ece969f8473977eaa340

%bcond ctest 1
%bcond libpfm 1

Name:           google-benchmark
Version:        1.9.5
Release:        1%{?dist}
Summary:        Microbenchmark support library
License:        Apache-2.0
URL:            https://github.com/google/benchmark
Source0:        https://github.com/google/benchmark/archive/v%{version}/benchmark-%{version}.tar.gz
Patch0:         0001-In-PerfCountersTest.MultiThreaded-serialize-worker-t.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
%if %{with libpfm}
BuildRequires:  libpfm-devel
%endif
%if %{with ctest}
BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel
BuildRequires:  glibc-langpack-en
%endif

%description
Library for benchmarking C++ functions, similar to unit tests.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n benchmark-%{version}
sed --in-place \
    --expression='/get_git_version/d' \
    --expression='/-Werror/d' \
    CMakeLists.txt

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGIT_VERSION='%{version}' \
    -DBENCHMARK_DOWNLOAD_DEPENDENCIES=OFF \
    -DBENCHMARK_ENABLE_DOXYGEN=OFF \
    -DBENCHMARK_ENABLE_GTEST_TESTS=%{?with_ctest:ON}%{?!with_ctest:OFF} \
    -DBENCHMARK_ENABLE_ASSEMBLY_TESTS=OFF \
    -DBENCHMARK_ENABLE_LIBPFM=%{?with_libpfm:ON}%{?!with_libpfm:OFF} \
    -DBENCHMARK_ENABLE_INSTALL=ON \
    -DBENCHMARK_ENABLE_TESTING=%{?with_ctest:ON}%{?!with_ctest:OFF} \
    -DBENCHMARK_INSTALL_DOCS=OFF \
    -DBENCHMARK_INSTALL_TOOLS=OFF \
    -DBENCHMARK_USE_BUNDLED_GTEST=OFF
%cmake_build

%install
%cmake_install

%check
%if %{with ctest}
%ctest --exclude-regex '^perf_counters_g?test$'
%endif

%files
%license AUTHORS CONTRIBUTORS LICENSE
%doc README.md
%{_libdir}/libbenchmark.so.1{,.*}

%files devel
%{_libdir}/libbenchmark.so
%{_includedir}/benchmark/
%{_libdir}/cmake/benchmark/
%{_libdir}/pkgconfig/benchmark*.pc
