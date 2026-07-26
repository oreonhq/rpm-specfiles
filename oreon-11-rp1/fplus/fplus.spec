%global source0_hash 9b5e24bbc92f43b977dc83efbc173bcf07dbe07f8718fc2670093655b56fcee3

#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# For testing
# Depends on downloading and being in a git repo
%bcond_with test

# Header only package
%global debug_package %{nil}

Summary:        Functional Programming Library for C++
Name:           fplus
License:        BSL-1.0
Version:        0.2.25
Release:        6%{?dist}

URL:            https://github.com/Dobiasd/FunctionalPlus
Source0:        %{url}/archive/v%{version}.tar.gz#/FunctionalPlus-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
FunctionalPlus is a small header-only library supporting you in
reducing code noise and in dealing with only one single level
of abstraction at a time. By increasing brevity and maintainability
of your code it can improve productivity (and fun!) in the long
run. It pursues these goals by providing pure and easy-to-use
functions that free you from implementing commonly used flows of
control over and over again.

%package devel

Summary:        Functional Programming Library for C++
Provides:       %{name}-static = %{version}-%{release}

%description devel
FunctionalPlus is a small header-only library supporting you in
reducing code noise and in dealing with only one single level
of abstraction at a time. By increasing brevity and maintainability
of your code it can improve productivity (and fun!) in the long
run. It pursues these goals by providing pure and easy-to-use
functions that free you from implementing commonly used flows of
control over and over again.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n FunctionalPlus-%{version}

# License check flags this as BSD 3-Clause
# api_search not distributed, remove to make license simpler
rm -rf api_search

%build
%cmake 
%cmake_build

%if %{with test}
%check
%ctest
%endif

%install
%cmake_install

%files devel
%dir %_includedir/%{name}
%dir %_includedir/%{name}/internal
%dir %_includedir/%{name}/internal/asserts
%license LICENSE
%doc README.md
%_includedir/%{name}/*_defines
%_includedir/%{name}/*.hpp
%_includedir/%{name}/internal/*.hpp
%_includedir/%{name}/internal/asserts/*.hpp
%_libdir/cmake/FunctionalPlus/

%changelog
%autochangelog
