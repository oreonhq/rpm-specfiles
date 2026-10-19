%global source0_hash efdbebfc2adfe5d491c3d88e515e0da62a647c2568670fa01d9263c21cce29ac
Name:           gnome-kra-ora-thumbnailer
Version:        1.4
Release:        18%{?dist}
Summary:        Thumbnailer for Krita and MyPaint images
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-kra-ora-thumbnailer
Source0:        http://download.gnome.org/sources/%{name}/1.4/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libarchive)
# /oreon:deps
%description
Thumbnailer for Krita and MyPaint images

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
