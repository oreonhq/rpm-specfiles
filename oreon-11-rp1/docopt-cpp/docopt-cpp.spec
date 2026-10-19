%global source0_hash 28af5a0c482c6d508d22b14d588a3b0bd9ff97135f99c2814a5aa3cbff1d6632
%global forgeurl0 %{url}
Name:           docopt-cpp
Version:        0.6.3
Release:        1%{?dist}
Summary:        C++11 Port of docopt
License:        MIT OR BSL-1.0
URL:            https://github.com/docopt/docopt.cpp
%forgemeta
Source0:        https://github.com/docopt/docopt.cpp/archive/v%{version}/docopt.cpp-%{version}.tar.gz
Patch1:         %{url}/pull/145.patch#/docopt-0.6.3-run-tests.patch
Patch2:         docopt-cpp-0.6.3-cmake.patch
%global common_description %{expand:docopt creates beautiful command-line interfaces
Isn't it awesome how getopt (and boost::program_options for you fancy folk!)
generate help messages based on your code?! These timeless functions have been
around for decades and have proven we don't need anything better, right?
Hell no! You know what's awesome? It's when the option parser is generated
based on the beautiful help message that you write yourself! This way you
don't need to write this stupid repeatable parser-code, and instead can
write only the help message-the way you want it.
}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  redhat-rpm-config
BuildRequires:  rpmautospec
# /oreon:deps
%description
%{common_description}
This is a port of the docopt.py module (https://github.com/docopt/docopt),
and we have tried to maintain full feature parity (and code structure)
as the original.

This port is written in C++11 and also requires a good C++11 standard library
(in particular, one with regex support).

%package devel
Summary:        Developer files for a docopt C++11 port
Requires:       cmake-filesystem
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{common_description}
Contains developer headers and a library. Install if docopt.cpp is used in
a code to be compiled.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake -DWITH_TESTS=on
%cmake_build
%install
%cmake_install
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libdocopt.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd "%{__cmake_builddir}"
%python3 run_tests
popd
%files -f %{oreon_filedir}/main.list
%files -n docopt-cpp-devel -f %{oreon_filedir}/docopt-cpp-devel.list

%changelog

%autochangelog
