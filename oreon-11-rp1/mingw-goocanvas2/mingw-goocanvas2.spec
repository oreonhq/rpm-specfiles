%global source0_hash 670a7557fe185c2703a14a07506156eceb7cea3b4bf75076a573f34ac52b401a
%{?mingw_package_header}
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-goocanvas2
Version:        3.0.0
Release:        1%{?dist}
Summary:        MinGW Windows canvas library for GTK+
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/GooCanvas
Source0:        https://download.gnome.org/sources/goocanvas/%{release_version}/goocanvas-%{version}.tar.xz
Patch0:         goocanvas-incompat-pointer-type.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gtk3
# /oreon:deps
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
%global oreon_srcdir goocanvas-%{version}
%oreon_prep
%build

export lt_cv_deplibs_check_method="pass_all"
%mingw_configure \
  --disable-static \
  --enable-python=no
%mingw_make_build
%install
%mingw_make_install
rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc
%mingw_find_lang goocanvas2
%oreon_autofiles mingw32-goocanvas2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-goocanvas2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-goocanvas2 -f %{oreon_filedir}/mingw32-goocanvas2.list
%files -n mingw64-goocanvas2 -f %{oreon_filedir}/mingw64-goocanvas2.list

%changelog

%autochangelog
