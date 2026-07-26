%global source0_hash 74b4339f7c7edfc5a218722503afea79259d11dd4b910d7acb43cbe173863d62

%global plugin_name     vnsiserver

Name:           vdr-vnsiserver
Version:        1.8.3
Release:        17%{?dist}
Summary:        VDR plugin to handle Kodi clients via VNSI
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
# 2021-05-08: FernetMenta seems to orphaned https://github.com/FernetMenta/vdr-plugin-vnsiserver.
URL:            https://github.com/vdr-projects/vdr-plugin-vnsiserver
Source:         https://github.com/vdr-projects/vdr-plugin-vnsiserver/archive/refs/tags/%{version}.tar.gz

Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Conflicts:      vdr-vnsiserver3
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= 1.5.9

%description
VDR plugin to handle Kodi (formerly known as XBMC) clients.
It is needed to use Kodi as a frontend and VDR as a backend.
With the plugin it is possible to get TV and PVR
functionality from a VDR into Kodi. It is able to handle several Kodi
clients connecting via the VNSI add-on.

In Kodi you need the PVR add-on "kodi-pvr-vdr-vnsi" to connect Kodi
with a VDR running this plugin.

See http://kodi.wiki/view/VDR for more information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n vdr-plugin-vnsiserver-%{version}

%build
make %{?_smp_mflags} CFLAGS="-fPIC %optflags" CXXFLAGS="-fPIC %{optflags}"

%install
%make_install
install -dm 755 %{buildroot}%{vdr_configdir}/plugins/%{plugin_name}
install -Dpm 644 %{plugin_name}/* %{buildroot}%{vdr_configdir}/plugins/%{plugin_name}/
%find_lang %{name}

%files -f %{name}.lang
%doc COPYING 
%doc HISTORY
%doc README

%dir %{vdr_configdir}/plugins/%{plugin_name}
%config(noreplace) %{vdr_configdir}/plugins/%{plugin_name}/*
%{vdr_plugindir}/libvdr-%{plugin_name}.so.%{vdr_apiversion}

%changelog
%autochangelog
