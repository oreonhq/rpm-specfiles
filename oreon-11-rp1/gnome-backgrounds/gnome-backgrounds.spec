%global source0_hash none

%global tarball_version %(echo %{version} | tr '~' '.')

Name:           gnome-backgrounds
Version:        50~rc
Release:        %autorelease
Summary:        Desktop backgrounds packaged with the GNOME desktop

License:        CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/gnome-backgrounds
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{tarball_version}.tar.xz
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  meson

# svg and jxl pixbuf loaders
Requires: (librsvg2 if gdk-pixbuf2)
Requires: (jxl-pixbuf-loader if gdk-pixbuf2)

Provides:   gnome-backgrounds-extras = %{version}-%{release}
Obsoletes:  gnome-backgrounds-extras < %{version}-%{release}

%description
The gnome-backgrounds package contains the default
desktop background, known as the Adwaita background,
for the GNOME Desktop version

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/images

# all translations are merged back into xml by intltool
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/backgrounds/gnome/*.{jxl,png,svg}
%{_datadir}/gnome-background-properties/*.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50~rc-1
- Prepare for Oreon 11 (RP1)
