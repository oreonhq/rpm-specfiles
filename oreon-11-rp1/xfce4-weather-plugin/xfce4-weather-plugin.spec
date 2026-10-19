%global source0_hash 002d1fe63906d2f3a012f3cb58cceff1dfbcc466759e36c76d3b03dd01c0dc57
%global minorversion 0.11
%global xfceversion 4.16
Name:           xfce4-weather-plugin
Version:        0.11.3
Release:        1%{?dist}
Summary:        Weather plugin for the Xfce panel
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
Requires:       xfce4-panel >= %{xfceversion}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  json-c-devel
BuildRequires:  libsoup-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  upower-devel
BuildRequires:  xfce4-panel-devel
# /oreon:deps
%description
A weather plugin for the Xfce panel. It shows the current temperature and 
weather condition, using weather data provided by xoap.weather.com.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
