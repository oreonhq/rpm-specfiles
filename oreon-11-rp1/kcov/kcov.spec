%global source0_hash 4cbba86af11f72de0c7514e09d59c7927ed25df7cebdad087f6d3623213b95bf
%undefine _auto_set_build_flags
%bcond_with tests
%bcond_with tools
%if %{with tests}
%global _vpath_builddir build
%endif
%ifnarch x86_64
%global kcov_test_args --no-ptrace
%endif
Name:           kcov
Version:        43
Release:        1%{?dist}
Summary:        Code coverage tool without special compilation options
License:        GPL-2.0-only AND MIT AND (GPL-2.0-only OR MIT)
URL:            https://simonkagstrom.github.io/%{name}
Source0:        https://github.com/SimonKagstrom/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    s390 s390x
%if %{with tests}
%endif
Provides:       bundled(handlebars) = 2.0.0
Provides:       bundled(jquery) = 2.1.1
Provides:       bundled(jquery-tablesorter) = 2.17.1
# oreon:deps
BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  procps
BuildRequires:  python3
# /oreon:deps
%description
Kcov is a code coverage tester for compiled programs, Python scripts and shell
scripts.  It allows collecting code coverage information from executables
without special command-line arguments, and continuously produces output from
long-running applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

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
%oreon_autofiles main

%check

%if %{with tests}
export PYTHONPATH=tests/tools
%python3 -m libkcov build/src/kcov tmp/ build-tests/ . -v %{?kcov_test_args}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
