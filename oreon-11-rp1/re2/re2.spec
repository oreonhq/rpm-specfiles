# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 87f6029d2f6de8aa023654240a03ada90e876ce9a4676e258dd01ea4c26ffd67
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond ctest 1
%if 0%{?oreon}
%bcond python 0
%else
%bcond python %[ 0%{?__isa_bits} != 32 ]
%endif

Name:           re2
%global tag 2025-11-05
%global so_version 11
%global base_version %(echo '%{tag}' | tr -d -)
%global py_version 1.1.%{base_version}
Version:        %{base_version}
Epoch:          2
Release:        %{autorelease}
Summary:        C++ fast alternative to backtracking RE engines

License:        BSD-3-Clause
SourceLicense:  %{license} AND Apache-2.0
URL:            https://github.com/google/re2
Source0:        %{url}/archive/%{tag}/re2-%{tag}.tar.gz

BuildSystem:    cmake
BuildOption(conf): -DRE2_BENCHMARK:BOOL=OFF
BuildOption(conf): -DRE2_USE_ICU:BOOL=ON
BuildOption(conf): -DRE2_TEST:BOOL=%{with ctest}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake(absl)
BuildRequires:  pkgconfig(icu-uc)
%if %{with ctest}
BuildRequires:  cmake(GTest)
%endif

%if %{with python}
BuildRequires:  %{py3_dist pybind11}
BuildRequires:  pybind11-static

BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist absl-py}
%endif

%global common_description %{expand:
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python. It is a C++
library.}

%description %{common_description}

%package        devel
Summary:        C++ header files and library symbolic links for re2

Requires:       re2%{?_isa} = %{epoch}:%{base_version}-%{release}

%description    devel %{common_description}

This package contains the C++ header files and symbolic links to the shared
libraries for re2. If you would like to develop programs using re2, you will
need to install re2-devel.

%if %{with python}
%package -n python3-google-re2
Summary:        RE2 Python bindings
Version:        %{py_version}

Requires:       re2%{?_isa} = %{epoch}:%{base_version}-%{release}

Conflicts:      python3-fb-re2
Obsoletes:      python3-fb-re2 < 1.0.7-19

%py_provides python3-re2

%description -n python3-google-re2
A drop-in replacement for the re module.

It uses RE2 under the hood, of course, so various PCRE features (e.g.
backreferences, look-around assertions) are not supported. See
https://github.com/google/re2/wiki/Syntax for the canonical reference, but
known syntactic ”gotchas” relative to Python are:

  • PCRE supports \Z and \z; RE2 supports \z; Python supports \z,
    but calls it \Z. You must rewrite \Z to \z in pattern strings.

Known differences between this module’s API and the re module’s API:

  • The error class does not provide any error information as attributes.
  • The Options class replaces the re module’s flags with RE2’s options as
    gettable/settable properties. Please see re2.h for their documentation.
  • The pattern string and the input string do not have to be the same type.
    Any str will be encoded to UTF-8.
  • The pattern string cannot be str if the options specify Latin-1 encoding.
%endif

%prep -a
rm lib/git/commit-msg.hook

%if %{with python}
%generate_buildrequires -a
%pyproject_buildrequires --directory python
%endif

%if %{with python}
%conf -a
cat >> python/setup.cfg <<EOF
[build_ext]
include_dirs=${PWD}
library_dirs=${PWD}/%{_vpath_builddir}
EOF
%endif

%if %{with python}
%build -a
%pyproject_wheel --directory python
%endif

%if %{with python}
%install -a
%pyproject_install
%pyproject_save_files --assert-license re2
%endif

%if %{with python}
%check -a
ln --symbolic python/re2_test.py
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %pytest re2_test.py
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/libre2.so.%{so_version}{,.*}

%files devel
%doc doc/syntax.{html,txt}
%{_includedir}/re2/
%{_libdir}/libre2.so
%{_libdir}/pkgconfig/re2.pc
%{_libdir}/cmake/re2/

%if %{with python}
%files -n python3-google-re2 -f %{pyproject_files}
%endif

%changelog
%autochangelog
