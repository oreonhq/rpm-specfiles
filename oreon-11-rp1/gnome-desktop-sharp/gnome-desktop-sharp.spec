%global source0_hash 577148d0937d91997341e8b2d2e8aadb0a5f1d898ca9bf579b114097c509aa67
Name:           gnome-desktop-sharp
Version:        2.26.0
Release:        54%{?dist}
Summary:        .NET language binding for mono
License:        LicenseRef-Callaway-LGPLv2
URL:            http://www.mono-project.com/GtkSharp
Source0:        http://ftp.gnome.org/pub/gnome/sources/%{name}/2.26/%{name}-%{version}.tar.bz2
Patch1:         %{name}-lib-target.patch
Provides:       gtksourceview2-sharp = 2:%{version}-%{release}
Obsoletes:      gtksourceview2-sharp < 2:2.20.1-2
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gnome-desktop3-devel
BuildRequires:  gnome-sharp-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  gtk2-devel
BuildRequires:  gtksourceview2-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libwnck-devel
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  vte-devel
BuildRequires:  vte291-devel
# /oreon:deps
%description
GnomeDesktop is a .NET language binding for assorted
GNOME libraries from the desktop release.

%package         devel
Summary:         Developing files for gnome-Desktop-sharp
Requires:        %{name} = %{version}-%{release}
Requires:        pkgconfig
Provides:        gtksourceview2-sharp-devel = 2:%{version}-%{release}
Obsoletes:       gtksourceview2-sharp-devel < 2:2.20.1-2
%description     devel
Package %{name}-devel provides development files for writing
%{name} applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .target
sed -i -e 's/gnome-desktop-2/gnome-desktop-3/g' configure
sed -i -e 's/VTE_REQUIRED_VERSION=.*/VTE_REQUIRED_VERSION=0.28.2/g' configure
sed -i -e 's!@libdir@!${exec_prefix}/lib/!g' gtksourceview/gtksourceview2-sharp.pc.in

# Fix permission
chmod 0644 HACKING

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-desktop-sharp-devel -f %{oreon_filedir}/gnome-desktop-sharp-devel.list

%changelog

%autochangelog
