%global source0_hash 4c9663136b3f0bc5eedebe7dd4fb72837c55dea9777cdc6d1fb07a15eae370c6

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

Name:           vdr-iptv
Version:        2.4.0
Release:        42%{?dist}
Summary:        IPTV plugin for VDR
License:        GPL-2.0-or-later
URL:            https://github.com/rofafor/vdr-plugin-iptv
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  gettext
BuildRequires:  libcurl-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin integrates multicast IPTV transport streams seamlessly into
VDR. You can use any IPTV channel like any other normal DVB channel for
live viewing, recording, etc. The plugin also features full section
filtering capabilities which allow for example EIT information to be
extracted from the incoming stream.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n vdr-plugin-iptv-%{version}

# Fix paths in plugin scripts as defined by Fedora
sed -i "s|^CHANNELS_CONF=.*|CHANNELS_CONF=%{vdr_configdir}/channels.conf|; \
        s|^CHANNEL_SETTINGS_DIR=.*/iptv|CHANNEL_SETTINGS_DIR=%{vdr_configdir}/plugins/%{vdr_plugin}|" \
        iptv/vlc2iptv

%build
%make_install CFLAGS="%{optflags} -fPIC" CXXFLAGS="-std=gnu++14 %{optflags} -fPIC" STRIP=:

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY README
%license COPYING
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%dir %{vdr_configdir}/plugins/iptv
%config(noreplace) %{vdr_resdir}/plugins/iptv/*.sh
%config(noreplace) %{vdr_resdir}/plugins/iptv/vlc2iptv

%changelog
%autochangelog
