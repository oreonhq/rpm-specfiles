%global source0_hash 80e6af808a4d74d5d7358666303eb1dbfc5582313ff9fa31d1c0d3280d3bd9e7

%global debug_package %{nil}

Name:           mpark-patterns
Version:        0.3.0
Release:        %autorelease
Summary:        An experimental pattern matching library for C++17

License:        BSL-1.0
URL:            https://github.com/mpark/patterns
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# change installation path for headers
# use system gtest
# disable balance test - requires lots of ram
Patch:          cmake.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel

%description
%{summary}.

%package        devel
Summary:        Header files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n patterns-%{version} -p1

%build
%cmake -DMPARK_PATTERNS_INCLUDE_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/mpark/
%{_datadir}/cmake/mpark_patterns/

%changelog
%autochangelog
