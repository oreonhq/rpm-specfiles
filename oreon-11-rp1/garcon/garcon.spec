%global source0_hash 7fb8517c12309ca4ddf8b42c34bc0c315e38ea077b5442bfcc4509415feada8f
%global xfceversion 4.20
%global namespc Garcon
Name:           garcon
Version:        4.20.0
Release:        1%{?dist}
Summary:        Implementation of the freedesktop.org menu specification
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-GFDL
URL:            http://xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Source1:        Documentation.directory
Patch0:         garcon-%{xfceversion}-fedora-menus.patch
Obsoletes:      libxfce4menu < 4.6.3
Conflicts:      xfdesktop <= 4.6.2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfce4util-1.0)
# /oreon:deps
%description
Garcon is an implementation of the freedesktop.org menu specification replacing
the former Xfce menu library libxfce4menu. It is based on GLib/GIO only and 
aims at covering the entire specification except for legacy menus.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel
Requires:       pkgconfig
Obsoletes:      libxfce4menu-devel < 4.6.2
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1 -b.fedora-menus

%build

%configure --disable-static --enable-gtk-doc
%make_build
%install
%make_install
chmod 755 %{buildroot}/%{_libdir}/*.so
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/desktop-directories
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n garcon-devel -f %{oreon_filedir}/garcon-devel.list

%changelog

%autochangelog
