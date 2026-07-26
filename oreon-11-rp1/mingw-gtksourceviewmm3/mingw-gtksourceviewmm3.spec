%global source0_hash dbb00b1c28e0407cc27d8b07a2ed0b4ea22f92e4b3e3006431cbd6726b6256b5

%{?mingw_package_header}

%global pkgname gtksourceviewmm3

Name:          mingw-%{pkgname}
Version:       3.21.3
Release:       8%{?dist}
Summary:       MinGW Windows GtkSourceViewmm library
License:       LGPL-2.0-or-later
BuildArch:     noarch
URL:           https://wiki.gnome.org/Projects/GtkSourceView
Source0:       http://download.gnome.org/sources/gtksourceviewmm/3.21/gtksourceviewmm-%{version}.tar.xz

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-gtkmm30
BuildRequires: mingw32-gtksourceview3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-gtkmm30
BuildRequires: mingw64-gtksourceview3

%description
MinGW Windows GtkSourceViewmm library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GtkSourceViewmm library

%description -n mingw32-%{pkgname}
MinGW Windows GtkSourceViewmm library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GtkSourceViewmm library

%description -n mingw64-%{pkgname}
MinGW Windows GtkSourceViewmm library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtksourceviewmm-%{version}

%build
%mingw_configure --disable-documentation --disable-static
%mingw_make_build

%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libgtksourceviewmm-3.0-0.dll
%{mingw32_includedir}/gtksourceviewmm-3.0/
%{mingw32_libdir}/gtksourceviewmm-3.0/
%{mingw32_libdir}/libgtksourceviewmm-3.0.dll.a
%{mingw32_libdir}/pkgconfig/gtksourceviewmm-3.0.pc

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libgtksourceviewmm-3.0-0.dll
%{mingw64_includedir}/gtksourceviewmm-3.0/
%{mingw64_libdir}/gtksourceviewmm-3.0/
%{mingw64_libdir}/libgtksourceviewmm-3.0.dll.a
%{mingw64_libdir}/pkgconfig/gtksourceviewmm-3.0.pc

%changelog
%autochangelog
