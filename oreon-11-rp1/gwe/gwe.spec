%global source0_hash d430b5a7cbac42d06708a6af27f013ac17773d184403e6e088bf6193a014ccb2

%global uuid    com.leinardi.%{name}

Name:           gwe
Version:        0.15.9
Release:        %autorelease
Summary:        System utility designed to provide information of NVIDIA card
BuildArch:      noarch

License:        GPL-3.0-or-later
URL:            https://gitlab.com/leinardi/gwe
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        README.fedora.md

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.56.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30
Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       libdazzle
Requires:       python3-gobject >= 3.44.2
Requires:       python3-injector >= 0.21.0
Requires:       python3-matplotlib-gtk3 >= 3.8.2
Requires:       python3-peewee >= 3.17.0
Requires:       python3-py3nvml >= 0.2.7
Requires:       python3-pyxdg %dnl >= 0.28 # Try to run with old for now https://bugzilla.redhat.com/show_bug.cgi?id=2242522
%if 0%{?fedora} >= 44
Requires:       python3-rx >= 4.0.4
%else
Requires:       python3-reactivex >= 4.0.4
%endif
Requires:       python3-requests >= 2.31.0
Requires:       python3-xlib >= 0.33
# Conditional dep for GNOME
Recommends:     (gnome-shell-extension-appindicator if gnome-shell)
Recommends:     libappindicator-gtk3

%description
GWE is/was a GTK system utility designed to provide information, control the
fans and overclock your NVIDIA video card and graphics processor.

This package require NVIDIA driver. Please read included README.Fedora file:

  xdg-open %{_docdir}/%{name}/README.fedora.md

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -m0644 -Dp %{SOURCE1} %{buildroot}%{_docdir}/%{name}/README.fedora.md
# Remove HiDPI version PNG icons since we have SVG version here
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2x/

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING.txt
%doc CHANGELOG.md README.md README.fedora.md RELEASING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/

%changelog
%autochangelog
