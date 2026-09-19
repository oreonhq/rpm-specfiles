%global source0_hash ff2eabc78106f009b4fb2def2d76fb0ca9e12acf624cbbfad9b3eb390d931313

# spec file for ssdeep
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

Name:      ssdeep
Version:   2.14.1
Release:   22%{?dist}
Summary:   Compute context triggered piecewise hashes

License:   GPL-2.0-or-later
URL:       https://ssdeep-project.github.io/ssdeep/
Source0:   https://github.com/ssdeep-project/ssdeep/releases/download/release-%{version}/ssdeep-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++

Requires:  %{name}-libs%{?_isa} = %{version}-%{release}

%description
ssdeep is a program for computing context triggered piecewise hashes (CTPH).
Also called fuzzy hashes, CTPH can match inputs that have homologies.
Such inputs have sequences of identical bytes in the same order, although bytes
in between these sequences may be different in both content and length.

%package devel
Summary: Development files for libfuzzy
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains library and header files for
developing applications that use libfuzzy.

%package libs
Summary: Runtime libfuzzy library

%description libs
The %{name}-libs package contains libraries needed by applications
that use libfuzzy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# avoid autotools being re-run
touch -r aclocal.m4 configure configure.ac

%build
%configure \
   --disable-auto-search \
   --disable-static

# rpath removal
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/libfuzzy.la

%files
%doc AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%files devel
%doc FILEFORMAT NEWS README TODO
%{_includedir}/fuzzy.h
%{_includedir}/edit_dist.h
%{_libdir}/libfuzzy.so

%files libs
%license COPYING
%{_libdir}/libfuzzy.so.2*

%changelog
%autochangelog
