%global source0_hash 267ac6d02916863c8a360b192f1f36e4eaeb8945c73ae7f92116d6f801ad8184
Name:           gotcha
Version:        1.0.8
Release:        1%{?dist}
Summary:        A library for wrapping function calls to shared libraries
License:        LGPL-2.1-only
URL:            https://github.com/llnl/gotcha
Source0:        https://github.com/llnl/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  python3dist(sphinx)
# /oreon:deps
%description
Gotcha is a library that wraps functions. Tools can use gotcha to install hooks
into other libraries, for example putting a wrapper function around libc's
malloc.  It is similar to LD_PRELOAD, but operates via a programmable API. This
enables easy methods of accomplishing tasks like code instrumentation or
wholesale replacement of mechanisms in programs without disrupting their source
code.

%package devel
Summary:        A library for wrapping function calls to shared libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development header and cmake configuration files for Gotcha.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n GOTCHA-%{version}
# Use shared library for testing
sed -i 's/libcheck.a/libcheck.so/g' test/unit/CMakeLists.txt
# Use standard optimiztaion levels to enable regular build flags
sed -i 's/-O0 //g' test/hammer/CMakeLists.txt
# Broken test, reported upstream
# https://github.com/LLNL/GOTCHA/issues/136
sed -i '/symver/d' test/CMakeLists.txt

%build

%cmake -DGOTCHA_ENABLE_TESTS=ON -DDEPENDENCIES_PREINSTALLED=TRUE
%cmake_build
pushd docs
sphinx-build . -b man man
popd
%install
%cmake_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp -p docs/man/gotcha.1 %{buildroot}/%{_mandir}/man1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ctest
%files -f %{oreon_filedir}/main.list
%files -n gotcha-devel -f %{oreon_filedir}/gotcha-devel.list

%changelog

%autochangelog
