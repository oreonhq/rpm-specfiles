%global source0_hash none

%{?mingw_package_header}

Name:      mingw-gettext
Version:   0.26
Release:   2%{?dist}
Summary:   GNU libraries and utilities for producing multi-lingual messages

License:   GPL-2.0-or-later AND LGPL-2.0-or-later
URL:       http://www.gnu.org/software/gettext/
Source0:        https://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.xz

BuildArch: noarch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-termcap

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-termcap

# Possible extra BRs.  These are used if available, but
# not required just for building.
#BuildRequires: mingw32-dlfcn
#BuildRequires: mingw32-libxml2
#BuildRequires: mingw32-expat
#BuildRequires: mingw32-glib2


%description
MinGW Windows Gettext library


# Win32
%package -n mingw32-gettext
Summary:         GNU libraries and utilities for producing multi-lingual messages

%description -n mingw32-gettext
MinGW Windows Gettext library

%package -n mingw32-gettext-static
Summary:        Static version of the MinGW Windows Gettext library
Requires:       mingw32-gettext = %{version}-%{release}

%description -n mingw32-gettext-static
Static version of the MinGW Windows Gettext library.

# Win64
%package -n mingw64-gettext
Summary:         GNU libraries and utilities for producing multi-lingual messages

%description -n mingw64-gettext
MinGW Windows Gettext library

%package -n mingw64-gettext-static
Summary:        Static version of the MinGW Windows Gettext library
Requires:       mingw64-gettext = %{version}-%{release}

%description -n mingw64-gettext-static
Static version of the MinGW Windows Gettext library.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n gettext-%{version}

%build
%mingw_configure            \
    --disable-java          \
    --disable-native-java   \
    --disable-csharp        \
    --enable-static         \
    --enable-threads=win32  \
    --without-emacs         \
    --disable-openmp
%mingw_make_build


%install
%mingw_make_install

rm -f %{buildroot}%{mingw32_datadir}/locale/locale.alias
rm -f %{buildroot}%{mingw32_libdir}/charset.alias

rm -f %{buildroot}%{mingw64_datadir}/locale/locale.alias
rm -f %{buildroot}%{mingw64_libdir}/charset.alias

# Remove documentation - already available in base gettext-devel.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw32_infodir}

rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{mingw64_infodir}

# Drop some useless tools
rm -rf %{buildroot}%{mingw32_libdir}/gettext
rm -rf %{buildroot}%{mingw64_libdir}/gettext

# Drop all .la files and .a files
find %{buildroot} -name "*.la" -delete
rm %{buildroot}%{mingw32_libdir}/libgettextlib.a
rm %{buildroot}%{mingw32_libdir}/libgettextsrc.a
rm %{buildroot}%{mingw64_libdir}/libgettextlib.a
rm %{buildroot}%{mingw64_libdir}/libgettextsrc.a

# Drop javaversion.class since it's a binary blob (RHBZ#2294881)
rm %{buildroot}%{mingw32_datadir}/gettext/javaversion.class
rm %{buildroot}%{mingw64_datadir}/gettext/javaversion.class

%mingw_find_lang %{name} --all-name


# Win32
%files -n mingw32-gettext -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/autopoint
%{mingw32_bindir}/envsubst.exe
%{mingw32_bindir}/gettext.exe
%{mingw32_bindir}/gettext.sh
%{mingw32_bindir}/gettextize
%{mingw32_bindir}/libasprintf-0.dll
%{mingw32_bindir}/libgettextlib-0-26.dll
%{mingw32_bindir}/libgettextpo-0.dll
%{mingw32_bindir}/libgettextsrc-0-26.dll
%{mingw32_bindir}/libintl-8.dll
%{mingw32_bindir}/libtextstyle-0.dll
%{mingw32_bindir}/msg*.exe
%{mingw32_bindir}/ngettext.exe
%{mingw32_bindir}/printf_gettext.exe
%{mingw32_bindir}/printf_ngettext.exe
%{mingw32_bindir}/recode-sr-latin.exe
%{mingw32_bindir}/xgettext.exe
%{mingw32_includedir}/autosprintf.h
%{mingw32_includedir}/gettext-po.h
%{mingw32_includedir}/libintl.h
%{mingw32_includedir}/textstyle.h
%{mingw32_includedir}/textstyle/stdbool.h
%{mingw32_includedir}/textstyle/version.h
%{mingw32_includedir}/textstyle/woe32dll.h
%{mingw32_libdir}/libasprintf.dll.a
%{mingw32_libdir}/libgettextlib.dll.a
%{mingw32_libdir}/libgettextpo.dll.a
%{mingw32_libdir}/libgettextsrc.dll.a
%{mingw32_libdir}/libintl.dll.a
%{mingw32_libdir}/libtextstyle.dll.a
%dir %{mingw32_libexecdir}/gettext/
%{mingw32_libexecdir}/gettext/cldr-plurals.exe
%{mingw32_libexecdir}/gettext/hostname.exe
%{mingw32_libexecdir}/gettext/project-id
%{mingw32_libexecdir}/gettext/urlget.exe
%{mingw32_libexecdir}/gettext/user-email
%{mingw32_datadir}/gettext/
%{mingw32_datadir}/gettext-%{version}/
%{mingw32_datadir}/aclocal/nls.m4

%files -n mingw32-gettext-static
%{mingw32_libdir}/libasprintf.a
%{mingw32_libdir}/libgettextpo.a
%{mingw32_libdir}/libintl.a
%{mingw32_libdir}/libtextstyle.a

# Win64
%files -n mingw64-gettext -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/autopoint
%{mingw64_bindir}/envsubst.exe
%{mingw64_bindir}/gettext.exe
%{mingw64_bindir}/gettext.sh
%{mingw64_bindir}/gettextize
%{mingw64_bindir}/libasprintf-0.dll
%{mingw64_bindir}/libgettextlib-0-26.dll
%{mingw64_bindir}/libgettextpo-0.dll
%{mingw64_bindir}/libgettextsrc-0-26.dll
%{mingw64_bindir}/libintl-8.dll
%{mingw64_bindir}/libtextstyle-0.dll
%{mingw64_bindir}/msg*.exe
%{mingw64_bindir}/ngettext.exe
%{mingw64_bindir}/printf_gettext.exe
%{mingw64_bindir}/printf_ngettext.exe
%{mingw64_bindir}/recode-sr-latin.exe
%{mingw64_bindir}/xgettext.exe
%{mingw64_includedir}/autosprintf.h
%{mingw64_includedir}/gettext-po.h
%{mingw64_includedir}/libintl.h
%{mingw64_includedir}/textstyle.h
%{mingw64_includedir}/textstyle/stdbool.h
%{mingw64_includedir}/textstyle/version.h
%{mingw64_includedir}/textstyle/woe32dll.h
%{mingw64_libdir}/libasprintf.dll.a
%{mingw64_libdir}/libgettextlib.dll.a
%{mingw64_libdir}/libgettextpo.dll.a
%{mingw64_libdir}/libgettextsrc.dll.a
%{mingw64_libdir}/libintl.dll.a
%{mingw64_libdir}/libtextstyle.dll.a
%dir %{mingw64_libexecdir}/gettext/
%{mingw64_libexecdir}/gettext/cldr-plurals.exe
%{mingw64_libexecdir}/gettext/hostname.exe
%{mingw64_libexecdir}/gettext/project-id
%{mingw64_libexecdir}/gettext/urlget.exe
%{mingw64_libexecdir}/gettext/user-email
%{mingw64_datadir}/gettext/
%{mingw64_datadir}/gettext-%{version}/
%{mingw64_datadir}/aclocal/nls.m4

%files -n mingw64-gettext-static
%{mingw64_libdir}/libasprintf.a
%{mingw64_libdir}/libgettextpo.a
%{mingw64_libdir}/libintl.a
%{mingw64_libdir}/libtextstyle.a


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.26-2
- Import
