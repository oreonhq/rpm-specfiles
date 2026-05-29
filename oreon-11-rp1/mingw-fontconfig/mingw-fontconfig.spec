%global source0_hash bc1a90697eb8ec6c3eed118105ef9cbdfdd676e563905bf1cb571a705598300e

%{?mingw_package_header}

Name:           mingw-fontconfig
Version:        2.17.1
Release:        3%{?dist}
Summary:        MinGW Windows Fontconfig library

License:        MIT
URL:            http://fontconfig.org
Source0:        https://gitlab.freedesktop.org/fontconfig/fontconfig/-/archive/2.17.1/fontconfig-2.17.1.tar.bz2

# Allow disabling tests (do not build)
Patch0:         fontconfig_tests.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-win-iconv

BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  python3

BuildRequires:  automake autoconf libtool gettext-devel


%description
MinGW Windows Fontconfig library.


# Win32
%package -n mingw32-fontconfig
Summary:        MinGW Windows Fontconfig library
Requires:       pkgconfig

%description -n mingw32-fontconfig
MinGW Windows Fontconfig library.

%package -n mingw32-fontconfig-static
Summary:       Static version of the cross compiled Fontconfig library
Requires:      mingw32-fontconfig = %{version}-%{release}

%description -n mingw32-fontconfig-static
Static version of the cross compiled Fontconfig library.

# Win64
%package -n mingw64-fontconfig
Summary:        MinGW Windows Fontconfig library
Requires:       pkgconfig

%description -n mingw64-fontconfig
MinGW Windows Fontconfig library.

%package -n mingw64-fontconfig-static
Summary:       Static version of the cross compiled Fontconfig library
Requires:      mingw64-fontconfig = %{version}-%{release}

%description -n mingw64-fontconfig-static
Static version of the cross compiled Fontconfig library.


%?mingw_debug_package


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n fontconfig-%{version}


%build
export MINGW32_CONFIGURE_ARGS="--with-arch=i686"
export MINGW64_CONFIGURE_ARGS="--with-arch=x86_64"
autoreconf -ifv
%mingw_configure --disable-docs --disable-tests --enable-static --enable-shared
%mingw_make_build


%install
%mingw_make_install

rm -f %{buildroot}/%{mingw32_libdir}/charset.alias
rm -f %{buildroot}/%{mingw64_libdir}/charset.alias

# Remove the .def file
rm -f %{buildroot}%{mingw32_libdir}/fontconfig.def
rm -f %{buildroot}%{mingw64_libdir}/fontconfig.def

# Remove .la files
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la

# Remove duplicate manpages.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Remove the docs
rm -rf %{buildroot}%{mingw32_datadir}/doc
rm -rf %{buildroot}%{mingw64_datadir}/doc


# Win32
%files -n mingw32-fontconfig
%license COPYING
%{mingw32_bindir}/fc-cache.exe
%{mingw32_bindir}/fc-cat.exe
%{mingw32_bindir}/fc-conflist.exe
%{mingw32_bindir}/fc-list.exe
%{mingw32_bindir}/fc-match.exe
%{mingw32_bindir}/fc-pattern.exe
%{mingw32_bindir}/fc-query.exe
%{mingw32_bindir}/fc-scan.exe
%{mingw32_bindir}/fc-validate.exe
%{mingw32_bindir}/libfontconfig-1.dll
%{mingw32_libdir}/libfontconfig.dll.a
%{mingw32_libdir}/pkgconfig/fontconfig.pc
%{mingw32_includedir}/fontconfig/
%{mingw32_sysconfdir}/fonts/
%{mingw32_datadir}/fontconfig/
%dir %{mingw32_datadir}/gettext
%dir %{mingw32_datadir}/gettext/its
%{mingw32_datadir}/gettext/its/fontconfig.its
%{mingw32_datadir}/gettext/its/fontconfig.loc
%{mingw32_datadir}/xml/fontconfig/

%files -n mingw32-fontconfig-static
%{mingw32_libdir}/libfontconfig.a

# Win64
%files -n mingw64-fontconfig
%license COPYING
%{mingw64_bindir}/fc-cache.exe
%{mingw64_bindir}/fc-cat.exe
%{mingw64_bindir}/fc-conflist.exe
%{mingw64_bindir}/fc-list.exe
%{mingw64_bindir}/fc-match.exe
%{mingw64_bindir}/fc-pattern.exe
%{mingw64_bindir}/fc-query.exe
%{mingw64_bindir}/fc-scan.exe
%{mingw64_bindir}/fc-validate.exe
%{mingw64_bindir}/libfontconfig-1.dll
%{mingw64_libdir}/libfontconfig.dll.a
%{mingw64_libdir}/pkgconfig/fontconfig.pc
%{mingw64_includedir}/fontconfig/
%{mingw64_sysconfdir}/fonts/
%{mingw64_datadir}/fontconfig/
%dir %{mingw64_datadir}/gettext
%dir %{mingw64_datadir}/gettext/its
%{mingw64_datadir}/gettext/its/fontconfig.its
%{mingw64_datadir}/gettext/its/fontconfig.loc
%{mingw64_datadir}/xml/fontconfig/

%files -n mingw64-fontconfig-static
%{mingw64_libdir}/libfontconfig.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.1-3
- Prepare for Oreon 11 (RP1)
