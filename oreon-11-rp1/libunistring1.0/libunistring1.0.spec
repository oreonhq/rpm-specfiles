%global source0_hash 5b46e74377ed7409c5b75e7a96f95377b095623b689d8522620927964a41499c
%bcond_with devel
Version:	1.4.2
Release:        1%{?dist}
Name: libunistring1.0
Summary:        Compatibility version of GNU Unicode string library
License: GPL-2.0-or-later or LGPL-3.0-or-later
URL: https://www.gnu.org/software/libunistring/
Source0:        https://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz
Provides: bundled(gnulib)
Conflicts: libunistring < 1.1
Provides: deprecated()
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

This package contains the libunistring library version 1.4.2 and is
intended for compatibility reasons only.  Users are advised to update
to a newer version of libunistring.

%if %{with devel}
%package devel
Summary: GNU Unicode string library - development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: libunistring-devel
Provides: deprecated()
%description devel
Development files for programs using libunistring.

This package contains the libunistring library version 1.4.2 and is
intended for compatibility reasons only.  Users are advised to update
to a newer version of libunistring.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libunistring-%{version}
%oreon_prep
%build

%configure --disable-static --disable-rpath
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/libunistring.la
mv $RPM_BUILD_ROOT%{_datadir}/doc/libunistring __doc
%if !%{with devel}
rm -f $RPM_BUILD_ROOT%{_infodir}/libunistring.info*
rm -f $RPM_BUILD_ROOT%{_libdir}/libunistring.so
rm -fr $RPM_BUILD_ROOT%{_includedir}/unistring
rm -f $RPM_BUILD_ROOT%{_includedir}/*.h
%oreon_autofiles main
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
