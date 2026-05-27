%global source0_hash 27bf01d20692e534a8963f96c6ca797df2b4ba6551db0379510c376558d75e3c

%global debug_package %{nil}

Name:           catch1
Version:        1.12.2
Release:        %autorelease
Summary:        A modern, C++-native, header-only, framework for unit-tests, TDD and BDD

License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
Source0:        https://github.com/catchorg/Catch2/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/catchorg/Catch2/issues/2178
Patch0:         catch1-sigstksz.patch
# Update minimum cmake version for cmake 4 support
Patch1:         catch1-cmake4.patch

BuildRequires:  cmake make gcc-c++

%description
Catch stands for C++ Automated Test Cases in Headers and is a
multi-paradigm automated test framework for C++ and Objective-C (and,
maybe, C). It is implemented entirely in a set of header files, but
is packaged up as a single header for extra convenience.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
Catch stands for C++ Automated Test Cases in Headers and is a
multi-paradigm automated test framework for C++ and Objective-C (and,
maybe, C). It is implemented entirely in a set of header files, but
is packaged up as a single header for extra convenience.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p 1 -n Catch2-%{version}


%build
%cmake
%cmake_build


%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include  %{buildroot}%{_includedir}/catch


%check
%ctest


%files devel
%doc README.md catch-logo-small.png docs
%license LICENSE.txt
%{_includedir}/catch


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12.2-1
- Prepare for Oreon 11 (RP1)
