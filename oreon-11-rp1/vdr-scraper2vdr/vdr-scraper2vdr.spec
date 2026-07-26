%global source0_hash b143be4c098f65d9d6e6e43c4aa820b42cd4a415f27c467e6dc066e967abc8d1

# https://github.com/horchi/scraper2vdr/commit/d9f6cb454ebbc951af5d1a4aa7fcc31e772f3bca
%global commit0 d9f6cb454ebbc951af5d1a4aa7fcc31e772f3bca
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global pname   scraper2vdr
%global gitdate 20190128

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

Name:           vdr-scraper2vdr
Version:        1.1.3
#Release:        15.%%{gitdate}git%%{shortcommit0}%%{?dist}
Release:        19%{?dist}
Summary:        A client plugin which provides scraped metadata from EPGD to other plugins
License:        GPL-1.0-or-later
URL:            https://github.com/horchi/scraper2vdr
#Source0:        https://github.com/horchi/scraper2vdr/archive/%%{commit0}/%%{name}-%%{commit0}.tar.gz#/%%{name}-%%{shortcommit0}.tar.gz
Source0:        https://github.com/horchi/scraper2vdr/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
# https://www.vdr-portal.de/index.php?attachment/44795-scraper2vdr-serienposter-statt-banner-diff/
Patch0:         scraper2vdr_serienposter_statt_banner.diff

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  openssl-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  libcurl-devel
BuildRequires:  imlib2-devel
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
Scraper2vdr acts as client and provides scraped metadata for tvshows and
movies from epgd to other plugins via its service interface. The plugin 
cares about caching the images locally and also cleans up the images if
not longer needed. 

epgd itself uses the thetvdb.com API for collecting series metadata and
themoviedb.org API for movies. Check the websites of both services for
the terms of use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%autosetup -p0 -n %%{pname}-%%{commit0}
%autosetup -p1 -n %{pname}-%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

# fedora specific
sed -i -e 's|#include <errmsg.h>|#include <mysql/errmsg.h>|' lib/db.c
sed -i -e 's|#include <mysql.h>|#include <mysql/mysql.h>|' lib/db.h

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" IMAGELIB=graphicsmagick

%install
%make_install
# fix the perm
chmod 0755 %{buildroot}/%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/scraper2vdr.conf

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING HISTORY* README*
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/scraper2vdr.conf
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/epg.dat

%changelog
%autochangelog
