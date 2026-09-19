%global source0_hash 875c9c3bda96faf050a2224649cc42129ffb662c4de33add8c0fd1fb860b47ed

%global minorversion 3.2

Name:           gtk-xfce-engine
Version:        3.2.0
Release:        25%{?dist}
Summary:        Xfce GTK theme engine

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
#VCS: git:git://git.xfce.org/xfce/gtk-xfce-engine
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.2.0
BuildRequires: make

%description
This package includes the Xfce GTK theme engine with various different themes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static --enable-gtk3

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libxfce.so
%{_libdir}/gtk-3.0/*/theming-engines/libxfce.so
%{_datadir}/themes/*

%changelog
%autochangelog
