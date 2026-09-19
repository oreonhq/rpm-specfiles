%global source0_hash 9a04f4f472fbb5c30bf60402f1ca626c4a76987f867978d0b8a35d7ab3fb8fe7

Name: expected
Version: 1.3.1
Release: %autorelease

License: CC0-1.0
Summary: C++11/14/17 std::expected with functional-style extensions
URL: https://github.com/TartanLlama/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Header-only %{summary}.

std::expected is proposed as the preferred way to represent objec
which will either have an expected value, or an unexpected value
giving information about why something failed. Unfortunately,
chaining together many computations which may fail can be verbose,
as error-checking code will be mixed in with the actual programming
logic. This implementation provides a number of utilities to make
coding with expected cleaner.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXPECTED_BUILD_TESTS=OFF \
    -DEXPECTED_BUILD_PACKAGE=OFF
%cmake_build

%install
%cmake_install

%files devel
%doc README.md
%license COPYING
%{_includedir}/tl
%{_datadir}/cmake/tl-%{name}

%changelog
%autochangelog
