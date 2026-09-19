%global source0_hash efdbebfc2adfe5d491c3d88e515e0da62a647c2568670fa01d9263c21cce29ac

Name:           gnome-kra-ora-thumbnailer
Version:        1.4
Release:        18%{?dist}
Summary:        Thumbnailer for Krita and MyPaint images

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-kra-ora-thumbnailer
Source0:        http://download.gnome.org/sources/%{name}/1.4/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
Buildrequires:  pkgconfig(libarchive)
BuildRequires: make

%description
Thumbnailer for Krita and MyPaint images

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/gnome-kra-thumbnailer
%{_bindir}/gnome-openraster-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gnome-kra-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gnome-openraster-thumbnailer.thumbnailer
%license COPYING
%doc AUTHORS NEWS README

%changelog
%autochangelog
