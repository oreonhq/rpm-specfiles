%global source0_hash 86cf0b81aa023fa93ed415653d51c96767f20b2d7334c893caba71e42654b0ae
%define glib2_version 2.26.0
%define pango_version 1.22.0
%define gtk2_version 2.20.0
Name: vte
Version: 0.84.1
Release:        1%{?dist}
Summary:        A terminal emulator
License: LGPL-2.0-or-later
URL: http://developer.gnome.org/vte/
Source0:        http://download.gnome.org/sources/vte/0.28/%{name}-%{version}.tar.xz
Patch0: vte-alt-meta-confusion.patch
Patch1: vte-python-bugfixes.patch
Patch2: vte-0.28.2-limit-arguments.patch
Patch3: http://ausil.fedorapeople.org/aarch64/vte/vte-aarch64.patch
Patch4: vte-0.28.2-control.patch
Patch5: vte-0.28.2-paste-fix.diff
Patch6: vte-0.28.2-introspection-fixes.patch
Patch7: vte-0.28.2-performance.patch
Patch8: vte-0.28.2-683730.patch
Patch9: vte-0.28.2-mouse-tracking.patch
Patch10: pointer-types.patch
Requires: systemd
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pango-devel
BuildRequires:  perl-Carp
# /oreon:deps
%description
VTE is a terminal emulator widget for use with GTK+ 2.0.

%package devel
Summary: Files needed for developing applications which use vte
Requires: %{name} = %{version}-%{release}
Requires: gtk2-devel
Requires: ncurses-devel
Requires: pkgconfig
%description devel
The vte-devel package includes the header files and developer docs
for the vte package.

Install vte-devel if you want to develop programs which will use
vte.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p2
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p0

%build

%configure \
        --enable-shared \
        --enable-static \
        --enable-introspection \
        --with-gtk=2.0 \
        --libexecdir=%{_libdir}/%{name} \
        --without-glX \
        --disable-gtk-doc \
        --disable-python
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.a
rm $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/*.a
%find_lang vte-0.0
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n vte-devel -f %{oreon_filedir}/vte-devel.list

%changelog

%autochangelog
