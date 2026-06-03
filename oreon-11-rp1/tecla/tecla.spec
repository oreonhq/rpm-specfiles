%global source0_hash none

Name:           tecla
Version:        50.0
Release:        %autorelease
Summary:        Keyboard layout viewer

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/tecla
Source:         https://download.gnome.org/sources/tecla/50/tecla-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  /usr/bin/desktop-file-validate

%description
Tecla is a keyboard layout viewer. It uses GTK/Libadwaita for UI, and
libxkbcommon to deal with keyboard maps.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains a pkg-config file for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n tecla-%{version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang tecla


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Tecla.desktop
%meson_test


%files -f tecla.lang
%license LICENSE
%doc NEWS README.md
%{_bindir}/tecla
%{_datadir}/applications/org.gnome.Tecla.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Tecla.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tecla-symbolic.svg


%files devel
%{_datadir}/pkgconfig/tecla.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Import
