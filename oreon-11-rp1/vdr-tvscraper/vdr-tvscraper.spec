%global source0_hash ff0ec8fcf11a740a2fd57565e0d2b019a3e2b972cc4e51c28d646c616700cb7c

%global pname   tvscraper

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
Version:        1.2.15
Release:        5%{?dist}
Summary:        Collects metadata for all available EPG events
# The entire source code is GPLv2+ except tools/curlfuncs.* which is BSD (3 clause)
License:        GPL-2.0-or-later AND MIT
URL:            https://github.com/MarkusEh/vdr-plugin-tvscraper
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/vdr-plugin-tvscraper-%{version}.tar.gz
Source1:        %{name}.conf

# Build for armv7hl failed
ExcludeArch:    armv7hl

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gumbo-parser-devel
BuildRequires:  sqlite-devel
BuildRequires:  libcurl-devel
BuildRequires:  jansson-devel
BuildRequires:  vdr-devel >= %{vdr_version} 
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
TVScraper runs in the background and collects metadata (posters,
banners, fanart, actor thumbs and roles, descriptions) for all
available EPG events on selectable channels and for recordings.
Additionally the plugin provides the collected metadata via the VDR
service interface to other plugins which deal with EPG information.

TVScraper uses the thetvdb.com API for collecting series metadata and
themoviedb.org API for movies. Check the websites of both services for
the terms of use.

Important: To avoid unnecessary traffic, only activate these channels
to be scrapped which are reasonable. After plugin installation all
channels are deactivated by default, so please consider this point when
you activate the channels you are interested in ;)

Additionally you are invited to contribute to the used web services with
providing missing data for your favorite movies and series.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n vdr-plugin-%{pname}-%{version}

# disable plugin examples
sed -i -e 's|install: install-lib install-i18n install-conf install-plugins|install: install-lib install-i18n install-conf|g' Makefile

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/tvscraper.conf
install -dm 755 %{buildroot}%{vdr_cachedir}/%{pname}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README.md
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%dir %{vdr_configdir}/plugins/%{pname}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/tvscraper.conf
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/override.conf
%config(noreplace) %{_datadir}/vdr/plugins/%{pname}/override_tvs.conf
%config(noreplace) %{_datadir}/vdr/plugins/%{pname}/networks.json
%attr(-,%{vdr_user},root) %dir %{vdr_cachedir}/%{pname}/

%changelog
%autochangelog
