%global source0_hash 12bd4f581f82c4c805bbf19cc794f7462f9ec0e71358fbc1628fd872169295e2

Name:		classified-ads
Version:	0.16
Release:	9%{?dist}
Summary:	Classified ads is distributed, server-less messaging system

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
URL:		http://katiska.org/classified_ads/
Source0:	https://github.com/operatornormal/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://github.com/operatornormal/classified-ads/blob/graphics/preprocessed.tar.gz?raw=true#/%{name}-graphics-%{version}.tar.gz
Patch0:     %{name}-miniupnp228.patch
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	openssl-devel
BuildRequires:	libnatpmp-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
BuildRequires:	opus-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel

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

%autosetup -p1 -a 1

%build
qmake-qt5 QMAKE_STRIP=echo
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/classified-ads.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/classified-ads.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc README.TXT
%{_bindir}/classified-ads
%{_datadir}/applications/classified-ads.desktop
%dir %{_datadir}/app-install
%dir %{_datadir}/app-install/icons
%{_datadir}/app-install/icons/turt-transparent-128x128.png
%{_mandir}/man1/classified-ads.1.*
%{_datadir}/metainfo/classified-ads.appdata.xml
%license LICENSE
%{_datadir}/doc/classified-ads/examples/sysinfo.tcl
%{_datadir}/doc/classified-ads/examples/luikero.tcl
%{_datadir}/doc/classified-ads/examples/calendar.tcl

%changelog
%autochangelog
