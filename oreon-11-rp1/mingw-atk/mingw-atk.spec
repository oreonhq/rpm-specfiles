%global source0_hash ac4de2a4ef4bd5665052952fe169657e65e895c5057dffb3c2a810f6191a0c36

%{?mingw_package_header}

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-atk
Version:        2.38.0
Release:        11%{?dist}
Summary:        MinGW Windows Atk library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://projects.gnome.org/accessibility/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/atk/%{release_version}/atk-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig
# Need native one too for msgfmt
BuildRequires:  gettext
# Need native one too for  glib-genmarshal
BuildRequires:  glib2-devel

%description
MinGW Windows Atk library.

# Win32
%package -n mingw32-atk
Summary:        MinGW Windows Atk library
Requires:       pkgconfig

%description -n mingw32-atk
MinGW Windows Atk library.

%package -n mingw32-atk-static
Summary:        Static version of the MinGW Windows Atk library
Requires:       mingw32-atk = %{version}-%{release}

%description -n mingw32-atk-static
Static version of the MinGW Windows Atk library.

# Win64
%package -n mingw64-atk
Summary:        MinGW Windows Atk library
Requires:       pkgconfig

%description -n mingw64-atk
MinGW Windows Atk library.

%package -n mingw64-atk-static
Summary:        Static version of the MinGW Windows Atk library
Requires:       mingw64-atk = %{version}-%{release}

%description -n mingw64-atk-static
Static version of the MinGW Windows Atk library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n atk-%{version}

%build
%mingw_meson --default-library=both -Dintrospection=false
%mingw_ninja

%install
%mingw_ninja_install

%mingw_find_lang atk10

# Win32
%files -n mingw32-atk -f mingw32-atk10.lang
%license COPYING
%{mingw32_bindir}/libatk-1.0-0.dll
%{mingw32_includedir}/atk-1.0
%{mingw32_libdir}/libatk-1.0.dll.a
%{mingw32_libdir}/pkgconfig/atk.pc

%files -n mingw32-atk-static
%{mingw32_libdir}/libatk-1.0.a

# Win64
%files -n mingw64-atk -f mingw64-atk10.lang
%license COPYING
%{mingw64_bindir}/libatk-1.0-0.dll
%{mingw64_includedir}/atk-1.0
%{mingw64_libdir}/libatk-1.0.dll.a
%{mingw64_libdir}/pkgconfig/atk.pc

%files -n mingw64-atk-static
%{mingw64_libdir}/libatk-1.0.a

%changelog
%autochangelog
