%global source0_hash 875c9c3bda96faf050a2224649cc42129ffb662c4de33add8c0fd1fb860b47ed
%global minorversion 3.2
Name:           gtk-xfce-engine
Version:        3.2.0
Release:        1%{?dist}
Summary:        Xfce GTK theme engine
License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
