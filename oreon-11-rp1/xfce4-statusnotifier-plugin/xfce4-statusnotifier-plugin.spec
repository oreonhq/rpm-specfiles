%global source0_hash 4c905944d510a7a460246660c6c7a648a3a5fa0d638276b9bf2380d3654a2cfa

%global _icondir %{_datadir}/icons/hicolor
%global basever 0.2

Name:           xfce4-statusnotifier-plugin
Version:        0.2.2
Release:        16%{?dist}
Summary:        Panel area status notifier plugin for Xfce4
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{basever}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  xfce4-dev-tools
BuildRequires:  libtool
BuildRequires:  gtk3-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  xfce4-panel-devel
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

%description
This plugin provides a panel area for status notifier items (application
indicators). Applications may use these items to display their status and
interact with user. This technology is a modern alternative to systray and
has the freedesktop.org specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure 
%make_build

%install
%make_install
find %{buildroot} -name \*.la -exec rm {} \;
if [ ! -d %{buildroot}/%{_libdir} ]; then
mv %{buildroot}/usr/lib %{buildroot}/%{_libdir}
fi

%find_lang %{name}

%files -f %{name}.lang
%{_libdir}/xfce4/panel/plugins/libstatusnotifier.*
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/icons/hicolor/*/apps/xfce4-statusnotifier-plugin.png
%{_datadir}/icons/hicolor/*/apps/xfce4-statusnotifier-plugin.svg
%{_datadir}/xfce4/panel/plugins/statusnotifier.desktop

%changelog
%autochangelog
