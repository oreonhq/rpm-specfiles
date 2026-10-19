%global source0_hash c540ff5c24618f76a0d92bd08bdeeb3a8d1bda4f57728c6ef2e4d3cbf373ded5
%bcond_with debug
%global pname   osd2web
%global rname   vdr-plugin-osd2web
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$
%global vdr_version 2.6.9
Name:           vdr-%{pname}
Version:        0.3.2
Release:        24%{?dist}
Summary:        VDR skin interface for the browser
License:        GPL-2.0-or-later
URL:            https://github.com/horchi/vdr-plugin-osd2web
Source0:        https://github.com/horchi/vdr-plugin-osd2web/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  jansson-devel
BuildRequires:  libexif-devel
BuildRequires:  libuuid-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  vdr-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
osd2web is a VDR skin interface for the browser, which displays the OSD
and allows all interactions which are possible on the OSD.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{rname}-%{version}

## Optimization flags in 'Make.config' file
sed -i \
    -e 's|PREFIX   = /usr/local|PREFIX   =  %{_prefix}|' \
    -e 's|CXXFLAGS += -O3|CXXFLAGS += %{optflags}|' \
    -e 's|@@OPTFLAGS | %{optflags}|' \
    Make.config

%if %{without debug}
sed -i -e 's|DEBUG = 1||' Make.config
%endif

%build

%make_build
%install
%make_install
install -Dpm 644 %{SOURCE1} \
  %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{name}.conf
chmod 0755 %{buildroot}/%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
rm -rf %{buildroot}/%{vdr_configdir}/plugins/osd2web/startBrowser.sh
install -Dpm 755 scripts/startBrowser.sh %{buildroot}%{vdr_plugindir}/bin/startBrowser.sh
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
