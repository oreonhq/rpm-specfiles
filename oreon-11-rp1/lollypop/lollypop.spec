%global source0_hash cb5fda9d34c7519edf0d74393269ec3d98670e7a247c4fb08d19e089ed5d5873
%global __python %{__python3}
%global provider org.gnome.Lollypop
Name:           lollypop
Version:        1.4.45
Release:        1%{?dist}
Summary:        Music player for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/lollypop
Source0:        https://adishatz.org/lollypop/%{name}-%{version}.tar.xz
Requires:       gdk-pixbuf2
Requires:       gstreamer1-plugins-base
Requires:       gobject-introspection
Requires:       gtk3
Recommends:     kid3-common
Requires:       libnotify >= 0.7.6
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-pillow
Requires:       python3-beautifulsoup4
Requires:       python3-gstreamer1
Requires:       pango
Requires:       totem-pl-parser
Requires:       gstreamer1-plugins-good
Requires:       libhandy1 >= 1.5
%if %{undefined flatpak}
Requires:       yt-dlp
%endif
BuildArch:      noarch
Obsoletes:      lollypop-cli < 1.0.6
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
Lollypop is a new GNOME music playing application.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
sed -i -e 's|libsoup-2.4|libsoup-3.0|' meson.build

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
chmod +x %{buildroot}%{_bindir}/*%{name}*
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{provider}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
