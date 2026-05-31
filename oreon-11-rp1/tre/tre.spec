%global source0_hash 31d5776d8c56186704ec272b97fadf52a0a7ae9caca19487a0c3b17ef1626340

%global commit d0e0c997336b3210f05b3e1daa7bb5cb9900d274
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git 0

Name: tre
Version: 0.9.0
Release:        %{?autorelease}
License: BSD-2-Clause
%if 0%{?git}
Source0:        https://github.com/laurikari/tre/archive/v%{version}/tre-%{version}.tar.gz
%else
Source0:        https://github.com/laurikari/tre/archive/v%{version}/tre-%{version}.tar.gz
%endif
# don't force build-time LDFLAGS into tre.pc
Patch2: %{name}-ldflags.patch
Summary: POSIX compatible regexp library with approximate matching
URL: https://laurikari.net/tre/
# rebuild autotools for bug #926655
BuildRequires: make
BuildRequires: gettext-devel
# required for tests
BuildRequires: glibc-langpack-en
BuildRequires: libtool
BuildRequires: python3-devel
Requires: %{name}-common = %{version}-%{release}

%description
TRE is a lightweight, robust, and efficient POSIX compatible regexp
matching library with some exciting features such as approximate
matching.

%package common
Summary: Cross-platform files for use with the tre package
BuildArch: noarch

%description common
This package contains platform-agnostic files used by the TRE
library.

%package devel
Requires: tre = %{version}-%{release}
Summary: Development files for use with the tre package

%description devel
This package contains header files and static libraries for use when
building applications which use the TRE library.

%package -n python3-%{name}
Summary: Python bindings for the tre library

%description -n python3-%{name}
This package contains the python bindings for the TRE library.

%package -n agrep
Summary: Approximate grep utility

%description -n agrep
The agrep tool is similar to the commonly used grep utility, but agrep
can be used to search for approximate matches.

The agrep tool searches text input for lines (or records separated by
strings matching arbitrary regexps) that contain an approximate, or
fuzzy, match to a specified regexp, and prints the matching lines.
Limits can be set on how many errors of each kind are allowed, or
only the best matching lines can be output.

Unlike other agrep implementations, TRE agrep allows full POSIX
regexps of any length, any number of errors, and non-uniform costs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if 0%{?git}
%setup -q -n tre-%{commit}
%else
%setup -q
%endif
%patch -P2 -p1 -b .ldflags
# rebuild autotools for bug #926655
touch ChangeLog
autoreconf -vif

%generate_buildrequires
pushd python > /dev/null
%pyproject_buildrequires
popd > /dev/null

%build
%configure --disable-static --disable-rpath
%make_build
pushd python
%pyproject_wheel
popd

%install
%make_install
%pyproject_install
%pyproject_save_files tre
rm -v %{buildroot}%{_libdir}/*.la
%find_lang %{name}

%check
%{__make} check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%pyproject_check_import

%files
%{_libdir}/libtre.so.5{,.*}

%files common -f %{name}.lang
%license LICENSE
%doc AUTHORS ChangeLog NEWS README.md THANKS TODO
%doc doc/tre-{api,syntax}.html doc/default.css

%files devel
%{_libdir}/libtre.so
%{_libdir}/pkgconfig/tre.pc
%{_includedir}/tre/

%files -n python3-%{name} -f %{pyproject_files}

%files -n agrep
%{_bindir}/agrep
%{_mandir}/man1/agrep.1*

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.0-1
- Import tre