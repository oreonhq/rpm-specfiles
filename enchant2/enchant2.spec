%bcond mingw %[%{undefined rhel} && %{undefined flatpak}]

Name:          enchant2
Version:       2.8.15
Release:       1%{?dist}
Summary:       An Enchanting Spell Checking Library

License:       LGPL-2.0-or-later
URL:           https://github.com/rrthomas/enchant
Source0:       https://github.com/rrthomas/enchant/releases/download/v%{version}/enchant-%{version}.tar.gz

%if !0%{?rhel}
# Look for aspell using pkg-config, instead of AC_CHECK_LIB which adds -laspell
# to the global LIBS and over-links libenchant (#1574893).  This patch
# can't currently go upstream, because aspell.pc is a Fedora addition
# that itself has not gone upstream.
Patch:         0001-Use-pkg-config-to-configure-Aspell.patch
%endif

BuildRequires: automake autoconf libtool
BuildRequires: gcc-c++
BuildRequires: libicu-devel
BuildRequires: make
BuildRequires: glib2-devel
BuildRequires: hunspell-devel
BuildRequires: libvoikko-devel
BuildRequires: vala

%if !0%{?rhel}
BuildRequires: aspell-devel
BuildRequires: nuspell-devel
%endif

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-glib2
BuildRequires: mingw32-icu
BuildRequires: mingw32-hunspell
%if !0%{?rhel}
BuildRequires: mingw32-nuspell
%endif


BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-glib2
BuildRequires: mingw64-icu
BuildRequires: mingw64-hunspell
%if !0%{?rhel}
BuildRequires: mingw64-nuspell
%endif
%endif

Provides:      bundled(gnulib)


%description
A library that wraps other spell checking backends.


%if !0%{?rhel}
%package aspell
Summary:       Integration with aspell for libenchant
Requires:      enchant2%{?_isa} = %{version}-%{release}
Supplements:   (enchant2 and aspell)

%description aspell
Libraries necessary to integrate applications using libenchant with aspell.

%package nuspell
Summary:       Integration with Nuspell for libenchant
Requires:      enchant2%{?_isa} = %{version}-%{release}
Supplements:   (enchant2 and nuspell)

%description nuspell
Libraries necessary to integrate applications using libenchant with Nuspell.
%endif

%package voikko
Summary:       Integration with voikko for libenchant
Requires:      enchant2%{?_isa} = %{version}-%{release}
Supplements:   (enchant2 and langpacks-fi)

%description voikko
Libraries necessary to integrate applications using libenchant with voikko.


%package devel
Summary:       Development files for %{name}
Requires:      enchant2%{?_isa} = %{version}-%{release}
Requires:      glib2-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.
%endif


%{?mingw_debug_package}


%prep
%autosetup -p1 -n enchant-%{version}

# Needed for 0001-Use-pkg-config-to-configure-Aspell.patch
autoreconf -ifv


%build
# Native build
mkdir build_native
pushd build_native
%define _configure ../configure
%configure \
%if !0%{?rhel}
    --with-aspell \
    --with-nuspell \
%endif
    --with-hunspell-dir=%{_datadir}/hunspell \
    --without-hspell \
    --disable-static \
    --docdir=%{_defaultdocdir}/%{name}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build pkgdatadir=%{_datadir}/enchant-2
popd

%if %{with mingw}
# MinGW build
MINGW32_CONFIGURE_ARGS="--with-hunspell-dir=%{mingw32_datadir}/hunspell" \
MINGW64_CONFIGURE_ARGS="--with-hunspell-dir=%{mingw64_datadir}/hunspell" \
%mingw_configure --disable-static --without-hspell --enable-relocatable

MINGW32_MAKE_ARGS="pkgdatadir=%{mingw32_datadir}/enchant-2" \
MINGW64_MAKE_ARGS="pkgdatadir=%{mingw64_datadir}/enchant-2" \
%mingw_make_build
%endif


%install
# Native build
%make_install -C build_native pkgdatadir=%{_datadir}/enchant-2

%if %{with mingw}
# MinGW build
MINGW32_MAKE_ARGS="pkgdatadir=%{mingw32_datadir}/enchant-2" \
MINGW64_MAKE_ARGS="pkgdatadir=%{mingw64_datadir}/enchant-2" \
%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/{doc,man}
rm -rf %{buildroot}%{mingw64_datadir}/{doc,man}
%endif

find %{buildroot} -name '*.la' -delete


%{?mingw_debug_install_post}


%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_bindir}/enchant-2
%{_bindir}/enchant-lsmod-2
%{_libdir}/libenchant-2.so.*
%dir %{_libdir}/enchant-2
%{_libdir}/enchant-2/enchant_hunspell.so
%{_mandir}/man1/*
%{_datadir}/enchant-2-2

%if !0%{?rhel}
%files aspell
%{_libdir}/enchant-2/enchant_aspell.so*

%files nuspell
%{_libdir}/enchant-2/enchant_nuspell.so*
%endif

%files voikko
%{_libdir}/enchant-2/enchant_voikko.so*

%files devel
%doc %{_defaultdocdir}/%{name}/enchant.html
%doc %{_defaultdocdir}/%{name}/enchant-2.html
%doc %{_defaultdocdir}/%{name}/enchant-lsmod-2.html
%{_libdir}/libenchant-2.so
%{_libdir}/pkgconfig/enchant-2.pc
%{_includedir}/enchant-2
%{_mandir}/man5/enchant.5*


%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING.LIB
%{mingw32_bindir}/enchant-lsmod-2.exe
%{mingw32_bindir}/enchant-2.exe
%{mingw32_bindir}/libenchant-2-2.dll
%{mingw32_includedir}/enchant-2/
%dir %{mingw32_libdir}/enchant-2/
%{mingw32_libdir}/enchant-2/enchant_hunspell.dll
%if !0%{?rhel}
%{mingw32_libdir}/enchant-2/enchant_nuspell.dll
%endif
%{mingw32_libdir}/libenchant-2.dll.a
%{mingw32_libdir}/pkgconfig/enchant-2.pc
%{mingw32_datadir}/enchant-2-2/

%files -n mingw64-%{name}
%license COPYING.LIB
%{mingw64_bindir}/enchant-lsmod-2.exe
%{mingw64_bindir}/enchant-2.exe
%{mingw64_bindir}/libenchant-2-2.dll
%{mingw64_includedir}/enchant-2/
%dir %{mingw64_libdir}/enchant-2/
%{mingw64_libdir}/enchant-2/enchant_hunspell.dll
%if !0%{?rhel}
%{mingw64_libdir}/enchant-2/enchant_nuspell.dll
%endif
%{mingw64_libdir}/libenchant-2.dll.a
%{mingw64_libdir}/pkgconfig/enchant-2.pc
%{mingw64_datadir}/enchant-2-2/
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.15-1
- Prepare for Oreon 11 (RP1)
