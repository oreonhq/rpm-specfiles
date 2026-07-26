%global source0_hash c728e2b7d4425ae81b54e1e07a3d3c8a4bd6377a63cffa43006045bceaa92e90

%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-goocanvas2
Version:        2.0.4
Release:        18%{?dist}
Summary:        MinGW Windows canvas library for GTK+

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/GooCanvas
Source0:        https://download.gnome.org/sources/goocanvas/%{release_version}/goocanvas-%{version}.tar.xz
# Fix initialization from incompatible pointer type
Patch0:         goocanvas-incompat-pointer-type.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal and glib-mkenums
BuildRequires:  glib2-devel

%description
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing.

This package contains the MinGW Windows cross compiled GooCanvas 2.0 library.

%package -n mingw32-goocanvas2
Summary:        MinGW Windows canvas library for GTK+

%description -n mingw32-goocanvas2
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing.

This package contains the MinGW Windows cross compiled GooCanvas 2.0 library.

%package -n mingw64-goocanvas2
Summary:        MinGW Windows canvas library for GTK+

%description -n mingw64-goocanvas2
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing.

This package contains the MinGW Windows cross compiled GooCanvas 2.0 library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n goocanvas-%{version}

%build
export lt_cv_deplibs_check_method="pass_all"
%mingw_configure \
  --disable-static \
  --enable-python=no

%mingw_make_build

%install
%mingw_make_install

# Remove .la files
rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la

# Remove documentation which duplicates Fedora native
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc

%mingw_find_lang goocanvas2

%files -n mingw32-goocanvas2 -f mingw32-goocanvas2.lang
%doc COPYING
%{mingw32_bindir}/libgoocanvas-2.0-9.dll
%{mingw32_includedir}/goocanvas-2.0/
%{mingw32_libdir}/libgoocanvas-2.0.dll.a
%{mingw32_libdir}/pkgconfig/goocanvas-2.0.pc

%files -n mingw64-goocanvas2 -f mingw64-goocanvas2.lang
%doc COPYING
%{mingw64_bindir}/libgoocanvas-2.0-9.dll
%{mingw64_includedir}/goocanvas-2.0/
%{mingw64_libdir}/libgoocanvas-2.0.dll.a
%{mingw64_libdir}/pkgconfig/goocanvas-2.0.pc

%changelog
%autochangelog
