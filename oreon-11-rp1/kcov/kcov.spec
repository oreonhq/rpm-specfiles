%global source0_hash 4cbba86af11f72de0c7514e09d59c7927ed25df7cebdad087f6d3623213b95bf

%undefine _auto_set_build_flags

%bcond_with tests
%bcond_with tools

%if %{with tests}
# The test suite expects a VPATH/out-of-source build with the following
# directories: build, build-tests and build-tools.
%global _vpath_builddir build
%endif

%ifnarch x86_64
# Same heuristic as upstream CI.
%global kcov_test_args --no-ptrace
%endif

Name:           kcov
Version:        43
Release:        4%{?dist}
Summary:        Code coverage tool without special compilation options

# Licenses of kcov itself and its bundled js libraries (see below)
License:        GPL-2.0-only AND MIT AND (GPL-2.0-only OR MIT)
URL:            https://simonkagstrom.github.io/%{name}
Source:         https://github.com/SimonKagstrom/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/SimonKagstrom/kcov/blob/v43/src/solib-parser/lib.c#L87-L104
ExcludeArch:    s390 s390x

BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3

%if %{with tests}
BuildRequires:  gawk
BuildRequires:  procps
%endif

# NB: Last I tried to unbundle those dependencies I hit a first roadblock in
# the sense that all three were available in Fedora but packaged differently
# and none of the versions matched:
#
# - js-jquery.noarch (compat package js-jquery2.noarch too)
# - nodejs-handlebars.noarch
# - xstatic-jquery-tablesorter-common.noarch
#
# All three packages drop files in different locations, following different
# patterns. NodeJS modules in particular look a bit more involved.
#
# Since those dependencies are merely used to slightly improve static HTML
# reports, I'd rather not spend mindless efforts unbundling things that are
# not ultimately exposed by the package. They are embedded in the kcov(1)
# program and written by `html-writer.cc` as static strings.
#
# It would make more sense to unbundle those if they were used as libraries
# instead of just assets. Here it seems overkill. I'm registering them as
# bundled provides even though they don't appear as individual files to at
# least keep awareness of what I consider a non-issue.
#
# -- dridi
Provides:       bundled(handlebars) = 2.0.0
Provides:       bundled(jquery) = 2.1.1
Provides:       bundled(jquery-tablesorter) = 2.17.1

%description
Kcov is a code coverage tester for compiled programs, Python scripts and shell
scripts.  It allows collecting code coverage information from executables
without special command-line arguments, and continuously produces output from
long-running applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# NB: the test suite is not built using the %%cmake macro, on purpose.
%if %{with tests}
cmake -S tests -B build-tests -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%make_build -C build-tests
%endif

%if %{with tools}
cmake -S tools -B build-tools -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%make_build -C build-tools
%endif

%cmake
%cmake_build

%install
%cmake_install

%check
%if %{with tests}
export PYTHONPATH=tests/tools
%python3 -m libkcov build/src/kcov tmp/ build-tests/ . -v %{?kcov_test_args}
%endif

%files
%license COPYING*
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*
%{_pkgdocdir}

%changelog
%autochangelog
