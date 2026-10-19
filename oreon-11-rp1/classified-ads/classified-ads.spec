%global source1_hash 12bd4f581f82c4c805bbf19cc794f7462f9ec0e71358fbc1628fd872169295e2
%global source0_hash 01a0a5cf470297147303c86b2b9f5c1a8eb5c6b183ee496373919b6790fc1592
Name:		classified-ads
Version:	0.16
Release:        9%{?dist}
Summary:        Classified ads is distributed, server-less messaging system
License:	LicenseRef-Callaway-LGPLv2
URL:		http://katiska.org/classified_ads/
Source0:        https://github.com/operatornormal/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://github.com/operatornormal/classified-ads/blob/graphics/preprocessed.tar.gz?raw=true#/%{name}-graphics-%{version}.tar.gz
Patch0:     %{name}-miniupnp228.patch
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libnatpmp-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Classified ads is an attempt to re-produce parts of the functionality
that went away when Usenet news ceased to exist. This attempt tries to
fix the problem of disappearing news-servers so that there is no servers
required and no service providers needed; data storage is implemented
inside client applications that users are running. Main feature is
public posting. Other features include private messages, group messages,
basic operator data, search, voice calls between nodes, UI extensions
with TCL language and general-purpose database shared between nodes of the 
application. 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

qmake-qt5 QMAKE_STRIP=echo
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/classified-ads.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/classified-ads.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
