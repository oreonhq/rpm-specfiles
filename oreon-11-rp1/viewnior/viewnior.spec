%global source0_hash b9319171ebca23929e6ea8039c194b1595d92e764db5e3890836fb5c36e233b0

Name:           viewnior
Version:        1.8
Release:        %autorelease
Summary:        Elegant image viewer

License:        GPL-3.0-or-later
URL:            http://siyanpanayotov.com/project/viewnior/
Source:         https://github.com/hellosiyan/Viewnior/archive/%{name}-%{version}.tar.gz
Patch:          0001-Fix-build-with-exiv2-0.28.0-raise-minimum-to-0.27.0.patch

BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-2.0) >= 2.32
BuildRequires:  pkgconfig(shared-mime-info) >= 0.20
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.4.0
BuildRequires:  pkgconfig(exiv2) >= 0.21
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  gnome-common
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
Requires:       webp-pixbuf-loader

%description 
Viewnior is an image viewer program. Created to be simple, fast and elegant. 
It's minimalistic interface provides more screen space for your images. Among 
its features are:

* Fullscreen & Slideshow
* Rotate, flip, save, delete images
* Animation support
* Browse only selected images
* Navigation window
* Simple interface
* Configurable mouse actions

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Viewnior-%{name}-%{version} -p1

%build
%meson

%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS TODO
%{_bindir}/%{name}
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_mandir}/man*/%{name}*

%changelog
%autochangelog
