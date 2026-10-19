%global source0_hash 45fe57c22b25a53066fa728d54c22e13272c0e5a83fc0dd54727d7e3cf6874ac
%bcond acceptance_c 1
%bcond acceptance_cpp 1
%bcond acceptance_python 1
Name:           gherkin
Version:        42.0.1
%global cpp_soversion 39
%global c_soversion 39
Release:        1%{?dist}
Summary:        A parser and compiler for the Gherkin language
License:        MIT
URL:            https://github.com/cucumber/gherkin
Source0:        https://github.com/cucumber/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       gherkin.1
Source11:       gherkin-generate-tokens.1
Patch:          %{url}/pull/546.patch
ExcludeArch:    %{ix86}
%if %{with acceptance_c} || %{with acceptance_cpp} || %{with acceptance_python}
%endif
%global common_description %{expand:
Gherkin is a parser and compiler for the Gherkin language.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13.0
BuildRequires:  python3dist(uv-build) >= 0.12.0
Requires:       python3-gherkin = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package data
Summary:        Data files shared among multiple Gherkin implementations
BuildArch:      noarch
%description data %{common_description}

This package contains data files shared among multiple Gherkin implementations.

%package c-libs
Summary:        Libraries implementing Gherkin in C
%description c-libs %{common_description}

This package contains libraries implementing Gherkin in C.

%package c-devel
Summary:        Development files for using the C implementation of Gherkin
Requires:       %{name}-c-libs%{?_isa} = %{version}-%{release}
%description c-devel %{common_description}

This package contains header files and libraries for developing and building
programs that use the C implementation of Gherkin.

%package cpp-libs
Summary:        Libraries implementing Gherkin in C++
%description cpp-libs %{common_description}

This package contains libraries implementing Gherkin in C++.

%package cpp-devel
Summary:        Development files for using the C++ implementation of Gherkin
Requires:       %{name}-cpp-libs%{?_isa} = %{version}-%{release}
%description cpp-devel %{common_description}

This package contains header files and libraries for developing and building
programs that use the C++ implementation of Gherkin.

%package cpp-tools
Summary:        Command-line tools associated with the C++ implementation of Gherkin
Requires:       %{name}-cpp-libs%{?_isa} = %{version}-%{release}
%description cpp-tools %{common_description}

This package contains command-line tools associated with the C++ implementation
of Gherkin.

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
# The canonical project name is gherkin-official; the PyPI project is
# https://pypi.org/project/gherkin-official.
%package -n python3-gherkin-official
Summary:        Gherkin parser (official, by Cucumber team)
BuildArch:      noarch
%py_provides python3-gherkin
Requires:       gherkin-data = %{version}-%{release}
%description -n python3-gherkin-official %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gherkin-%{version} -p1

# Tweaks for running acceptance tests
#
# C: Don’t try to rebuild the (C) CLI; we want to use the one already built
# with CMake. This is easier than trying to convince make that the targets in
# question have already been built, which is the strategy we follow for the C++
# acceptance tests.
sed -r -i 's/^(\.run:) cli \$\(GHERKIN\)/\1/' c/Makefile
# Python: Fix unversioned python interpreter.
sed -r -i 's@python -m@%{python3} -m@' python/Makefile
# Python: Do not upper-bound (SemVer-bound) the version of uv_build; we must
# work with what we have, and compatibility across SemVer boundaries is quite
# good in practice.
sed -r -i 's/"(uv_build *>= *[^:]+), *<[^"]+"/"\1"/' python/pyproject.toml

%build

echo '==== Building C implementation ===='
pushd c
%cmake_build
popd
echo '==== Building C++ implementation ===='
pushd cpp
%cmake_build
popd
echo '==== Building Python implementation ===='
pushd python
%pyproject_wheel
popd
%install
install -t '%{buildroot}%{_datadir}/gherkin' -D -p -m 0644 \
    gherkin-languages.json
echo '==== Installing C implementation ===='
pushd c
%cmake_install
popd
echo '==== Installing C++ implementation ===='
pushd cpp
%cmake_install
popd
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}'
echo '==== Installing Python implementation ===='
pushd python
%pyproject_install
ln -s -f %{buildroot}%{_datadir}/gherkin/gherkin-languages.json \
    '%{buildroot}%{python3_sitelib}/gherkin/gherkin-languages.json'
symlinks -c -o '%{buildroot}%{python3_sitelib}/gherkin/gherkin-languages.json'
popd
%oreon_autofiles python3-gherkin-official usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

echo '==== Testing C implementation ===='
pushd c
%if %{with acceptance_c}
touch .built
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %make_build acceptance \
    GHERKIN='%{_vpath_builddir}/gherkinexe' \
    GHERKIN_GENERATE_TOKENS='%{_vpath_builddir}/gherkin_generate_tokens'
%endif
popd
echo '==== Testing C++ implementation ===='
pushd cpp
%ctest
%if %{with acceptance_cpp}
mkdir -p .built
mkdir -p stage
ln -s '%{buildroot}%{_bindir}' stage/bin
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %make_build -j1 acceptance
%endif
popd
echo '==== Testing Python implementation ===='
%pyproject_check_import
%pytest
%if %{with acceptance_python}
%{py3_test_envvars} %make_build -C python acceptance \
    GHERKIN_GENERATE_EVENTS='%{python3} scripts/generate_events.py' \
    GHERKIN_GENERATE_TOKENS='%{python3} scripts/generate_tokens.py'
%endif
%files
%files -n gherkin-data -f %{oreon_filedir}/gherkin-data.list
%files -n gherkin-c-libs -f %{oreon_filedir}/gherkin-c-libs.list
%files -n gherkin-c-devel -f %{oreon_filedir}/gherkin-c-devel.list
%files -n gherkin-cpp-libs -f %{oreon_filedir}/gherkin-cpp-libs.list
%files -n gherkin-cpp-devel -f %{oreon_filedir}/gherkin-cpp-devel.list
%files -n gherkin-cpp-tools -f %{oreon_filedir}/gherkin-cpp-tools.list
%files -n python3-gherkin-official -f %{oreon_filedir}/python3-gherkin-official.list

%changelog

%autochangelog
