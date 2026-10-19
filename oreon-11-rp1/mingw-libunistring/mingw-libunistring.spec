%global source0_hash 5b46e74377ed7409c5b75e7a96f95377b095623b689d8522620927964a41499c
%{?mingw_package_header}
Name: mingw-libunistring
Version: 1.4.2
Release:        1%{?dist}
Summary:        MinGW port of GNU Unicode string library
License: GPL-2.0-or-later OR LGPL-3.0-or-later
Url: http://www.gnu.org/software/libunistring/
Source0:        http://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz
BuildArch: noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package -n mingw32-libunistring
Summary:        MinGW port of GNU Unicode string library
%description -n mingw32-libunistring
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package -n mingw64-libunistring
Summary:        MinGW port of GNU Unicode string library
%description -n mingw64-libunistring
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libunistring-%{version}

%build

%mingw_configure \
    --disable-static \
    --disable-rpath
%mingw_make %{?_smp_mflags}
%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{mingw32_infodir}/dir
rm -f $RPM_BUILD_ROOT%{mingw64_infodir}/dir
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
mv $RPM_BUILD_ROOT%{mingw32_datadir}/doc/libunistring __doc
mv $RPM_BUILD_ROOT%{mingw64_datadir}/doc/libunistring __doc
%oreon_autofiles mingw32-libunistring usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libunistring usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libunistring -f %{oreon_filedir}/mingw32-libunistring.list
%files -n mingw64-libunistring -f %{oreon_filedir}/mingw64-libunistring.list

%changelog

%autochangelog
