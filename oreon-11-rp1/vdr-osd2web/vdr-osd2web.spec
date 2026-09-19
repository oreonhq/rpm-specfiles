%global source0_hash c540ff5c24618f76a0d92bd08bdeeb3a8d1bda4f57728c6ef2e4d3cbf373ded5

## This macro activates/deactivates debug option
%bcond_with debug
%global pname   osd2web
%global rname   vdr-plugin-osd2web
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.8.1
%endif

Name:           vdr-%{pname}
Version:        0.3.2
Release:        24%{?dist}
Summary:        VDR skin interface for the browser
License:        GPL-2.0-or-later
URL:            https://github.com/horchi/vdr-plugin-osd2web
Source0:        https://github.com/horchi/vdr-plugin-osd2web/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  libwebsockets-devel
BuildRequires:  zlib-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  jansson-devel
BuildRequires:  libexif-devel
BuildRequires:  libuuid-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

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

# fix the perm due W: unstripped-binary-or-object
chmod 0755 %{buildroot}/%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

# install executable to %%{vdr_plugindir} due E: executable-marked-as-config-file
rm -rf %{buildroot}/%{vdr_configdir}/plugins/osd2web/startBrowser.sh
install -Dpm 755 scripts/startBrowser.sh %{buildroot}%{vdr_plugindir}/bin/startBrowser.sh

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE COPYING
%doc README
%dir %{vdr_configdir}/plugins/osd2web/
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{name}.conf
%{vdr_plugindir}/libvdr-%{pname}.so.%{vdr_apiversion}
%config(noreplace) %{vdr_configdir}/plugins/osd2web/*
%{vdr_plugindir}/bin/startBrowser.sh

%changelog
%autochangelog
