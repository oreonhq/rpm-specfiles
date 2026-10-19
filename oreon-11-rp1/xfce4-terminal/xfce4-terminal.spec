%global source0_hash 6874c7b975cc3dc3bd636d57ffec723de7458202defe65377593d3a7e0734b94
%global minorversion 1.2
%global xfceversion 4.20
Name:           xfce4-terminal
Version:        1.2.0
Release:        1%{?dist}
Summary:        Terminal Emulator for the Xfce Desktop environment
License:        GPL-2.0-or-later
URL:            http://docs.xfce.org/apps/terminal/start
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.xz
Requires:       dejavu-sans-mono-fonts
Provides: Terminal = %{version}-%{release}
Obsoletes: Terminal < 0.4.8-5
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  gtk3-devel
BuildRequires:  libutempter-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  meson
BuildRequires:  vte291-devel
# /oreon:deps
%description
Xfce4-terminal is a lightweight and easy to use terminal emulator application 
with many advanced features including drop down, tabs, unlimited scrolling, 
full colors, fonts, transparent backgrounds, and more.

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
  --delete-original \
  --add-category="GTK" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install \
  --delete-original \
  --add-category="GTK" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-settings.desktop
rm -rf %{buildroot}%{_datadir}/gnome-control-center
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
