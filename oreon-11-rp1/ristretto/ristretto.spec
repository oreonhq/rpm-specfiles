%global source0_hash 502cf1577de14b38132dc89e56884c5e10f86f6a028d8dde379a8839110fda55
%global majorversion 0.14
%global xfceversion 4.18
Name:           ristretto
Version:        0.14.0
Release:        1%{?dist}
Summary:        Image-viewer for the Xfce desktop environment
Summary(de):    Bildbetrachter für die Xfce Desktop-Umgebung
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/ristretto/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.xz
Requires:       tumbler
# oreon:deps
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  exo-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libexif-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  meson
BuildRequires:  xfconf-devel
# /oreon:deps
%description
Ristretto is a fast and lightweight image-viewer for the Xfce desktop 
environment.

%description -l de
Ristretto ist ein schneller und leichtgewichtiger Bildbetrachter für die Xfce
Desktop-Umgebung.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --add-mime-type=image/x-bmp \
        --add-mime-type=image/x-png \
        --add-mime-type=image/x-pcx \
        --add-mime-type=image/x-tga \
        --add-mime-type=image/xpm \
        --delete-original \
        %{buildroot}%{_datadir}/applications/org.xfce.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
