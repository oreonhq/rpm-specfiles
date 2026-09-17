%global source0_hash 0eec3d4358385fb67b369f02dbd82217c912ba0edc3533f27377ba33f90084c1

%bcond_with audacious
%bcond_without curl
%bcond_without ibm
%bcond_without imlib
%bcond_without lua_cairo
%bcond_without lua_imlib
%bcond_with moc
%bcond_without mpd
%bcond_without ncurses
%bcond_with nvidia
%bcond_without portmon
%bcond_without rss
%bcond_without wayland
%bcond_without weather
%bcond_without weather_xoap
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 8
%bcond_with wlan
%else
%bcond_without wlan
%endif
%bcond_without xdbe
%bcond_without xinerama

Name:           conky
Version:        1.22.2
Release:        3%{?dist}
Summary:        A system monitor for X

License:        GPL-3.0-or-later AND LGPL-2.1-or-later AND MIT-open-group AND BSD-3-Clause
URL:            https://github.com/brndnmtthws/conky
Source0:        https://github.com/brndnmtthws/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libXft-devel
BuildRequires:  libXt-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  lua-devel
%{?with_audacious:BuildRequires: audacious-devel < 3.5 dbus-glib-devel}
%{?with_curl:BuildRequires: curl-devel}
%{?with_imlib:BuildRequires: imlib2-devel}
%{?with_lua_cairo:BuildRequires: cairo-devel tolua++-devel}
%{?with_lua_imlib:BuildRequires: imlib2-devel tolua++-devel}
%{?with_ncurses:BuildRequires: ncurses-devel}
%{?with_nvidia:BuildRequires: libXNVCtrl-devel}
%{?with_rss:BuildRequires: curl-devel libxml2-devel}
%{?with_wayland:BuildRequires: pango-devel wayland-devel wayland-protocols-devel}
%{?with_weather:BuildRequires: curl-devel}
%{?with_weather_xoap:BuildRequires: libxml2-devel}
%{?with_wlan:BuildRequires: wireless-tools-devel}
%{?with_xinerama:BuildRequires: libXinerama-devel}
BuildRequires:  pandoc
BuildRequires:  python3-pyyaml python3-jinja2
BuildRequires:  cmake git
BuildRequires:  desktop-file-utils

%description
A system monitor for X originally based on the torsmo code. but more kickass.
It just keeps on given'er. Yeah.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# remove executable bits from files included in %{_docdir}
chmod a-x extras/convert.lua

for i in AUTHORS; do
    iconv -f iso8859-1 -t utf8 -o ${i}{_,} && touch -r ${i}{,_} && mv -f ${i}{_,}
done

%build
%cmake \
                            -DBUILD_DOCS=ON \
                            -DBUILD_BUILTIN_CONFIG=OFF \
                            -DBUILD_SHARED_LIBS:BOOL=OFF \
    %{?with_audacious:      -DBUILD_AUDACIOUS=ON} \
    %{?with_curl:           -DBUILD_CURL=ON} \
    %{!?with_ibm:           -DBUILD_IBM=OFF} \
    %{?with_imlib:          -DBUILD_IMLIB2=ON} \
    %{?with_lua_cairo:      -DBUILD_LUA_CAIRO=ON} \
    %{?with_lua_imlib:      -DBUILD_LUA_IMLIB2=ON} \
    %{!?with_moc:           -DBUILD_MOC=OFF} \
    %{!?with_mpd:           -DBUILD_MPD=OFF} \
    %{!?with_ncurses:       -DBUILD_NCURSES=OFF} \
    %{?with_nvidia:         -DBUILD_NVIDIA=ON} \
    %{!?with_portmon:       -DBUILD_PORT_MONITORS=OFF} \
    %{?with_rss:            -DBUILD_RSS=ON} \
    %{?with_wayland:        -DBUILD_WAYLAND=ON} \
    %{?with_weather:        -DBUILD_WEATHER_METAR=ON} \
    %{?with_weather_xoap:   -DBUILD_WEATHER_XOAP=ON} \
    %{?with_wlan:           -DBUILD_WLAN=ON} \
    %{?with_xdbe:           -DBUILD_XDBE=ON} \
    %{?!with_xinerama:      -DBUILD_XINERAMA=OFF} \
    ;

%cmake_build

%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/conky
install -m644 -p data/conky.conf $RPM_BUILD_ROOT%{_sysconfdir}/conky
rm -rf $RPM_BUILD_ROOT%{_docdir}/conky-*
rm -f $RPM_BUILD_ROOT%{_libdir}/libtcp-portmon.a
rm -f $RPM_BUILD_ROOT/usr/lib/libconky_core.a

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/conky.desktop

%files
%doc AUTHORS COPYING README.md extras/*
%dir %{_sysconfdir}/conky
%config %{_sysconfdir}/conky/conky.conf
%{_bindir}/conky
%if %{with lua_cairo} || %{with lua_imlib}
%{_libdir}/conky
%endif
%{_datadir}/applications/conky.desktop
%{_datadir}/icons/hicolor/*/apps/conky*
%{_mandir}/man1/conky.1*

%changelog
%autochangelog
