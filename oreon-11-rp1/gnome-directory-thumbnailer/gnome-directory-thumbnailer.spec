%global source0_hash 57fba723521ff21aa2f655c22dc3e1e66586bb1effef8dbaf5de4d027f70cf9d

Name:           gnome-directory-thumbnailer
Version:        0.1.11
Release:        19%{?dist}
Summary:        Thumbnailer for directories

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GnomeDirectoryThumbnailer
Source0:        https://download.gnome.org/sources/%{name}/0.1/%{name}-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/gnome-directory-thumbnailer/-/commit/8b39714ff8fd5de6643b5fdcf7fb01da35b82334
Patch1:         0001-Update-for-gnome-desktop-43-API-change.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
Buildrequires:  pkgconfig(gtk+-3.0)
Buildrequires:  pkgconfig(gnome-desktop-3.0)

BuildRequires:  intltool
BuildRequires: make

%description
Thumbnailer for directories based on some heuristics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/gnome-directory-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gnome-directory-thumbnailer.thumbnailer
%doc AUTHORS NEWS README
%license COPYING

%changelog
%autochangelog
