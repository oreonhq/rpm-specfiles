%global source0_hash a0dedf9fff66d8e29e7c25d23c1f42beda2089fb4eac1b36e6acd8a29edfbd1f

Summary:        Rsync remote-delta algorithm library
Name:           librsync
Version:        2.3.4
Release:        8%{?dist}
License:        LGPL-2.1-or-later
URL:            https://librsync.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/librsync-%{version}.tar.gz
BuildRequires:  cmake >= 3.6
BuildRequires:  gcc
BuildRequires:  popt-devel
# Compression isn't functional: https://github.com/librsync/librsync/issues/8
#BuildRequires:  bzip2-devel
#BuildRequires:  zlib-devel

%description
librsync is a library for calculating and applying network deltas, with an
interface designed to ease integration into diverse network applications.

librsync encapsulates the core algorithms of the rsync protocol, which help
with efficient calculation of the differences between two files. The rsync
algorithm is different from most differencing algorithms because it does not
require the presence of the two files to calculate the delta. Instead, it
requires a set of checksums of each block of one file, which together form a
signature for that file. Blocks at any in the other file which have the same
checksum are likely to be identical, and whatever remains is the difference.

%package devel
Summary:        Headers and development libraries for librsync
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The librsync-devel package contains header files and library necessary for
developing programs based on librsync.

%if 0%{!?_without_doc:1}
%package doc
Summary:         Documentation files for %{name}
BuildArch:       noarch
BuildRequires:   doxygen
BuildRequires:   graphviz

%description doc
librsync is a library for calculating and applying network deltas, with an
interface designed to ease integration into diverse network applications.
This package contains the API documentation for developing applications that
use librsync.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake
%cmake_build

%if 0%{!?_without_doc:1}
%cmake_build --target doc
%endif

%install
%cmake_install

%check
%cmake_build --target check

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_libdir}/%{name}.so.2*
%{_bindir}/rdiff
%{_mandir}/man1/rdiff.1*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}*
%{_mandir}/man3/%{name}.3*

%if 0%{!?_without_doc:1}
%files doc
%if 0%{?__cmake_in_source_build}%{?__cmake3_in_source_build}
%doc html
%else
%doc %{_vpath_builddir}/html
%endif
%endif

%changelog
%autochangelog
