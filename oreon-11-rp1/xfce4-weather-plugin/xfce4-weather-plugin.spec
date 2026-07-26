%global source0_hash 002d1fe63906d2f3a012f3cb58cceff1dfbcc466759e36c76d3b03dd01c0dc57

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173105

%global minorversion 0.11

%global xfceversion 4.16

Name:           xfce4-weather-plugin
Version:        0.11.3
Release:        %autorelease
Summary:        Weather plugin for the Xfce panel

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-weather-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libsoup-devel >= 2.26.0
BuildRequires:  upower-devel >= 0.9.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  json-c-devel
Requires:       xfce4-panel >= %{xfceversion}

%description
A weather plugin for the Xfce panel. It shows the current temperature and 
weather condition, using weather data provided by xoap.weather.com.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/weather

%changelog
%autochangelog
