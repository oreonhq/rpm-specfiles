%global source0_hash 23f3c01e4eabb82389923ea229b6dbd248cea512651ba9ea60ba798c4e1bc31c

%global pname   tvguide

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

Name:           vdr-tvguide
Version:        1.3.12
Release:        2%{?dist}
Summary:        TvGuide is a highly customizable 2D EPG viewer plugin
License:        GPL-2.0-or-later
URL:            https://gitlab.com/kamel5/tvguide
Source0:        https://gitlab.com/kamel5/%{pname}/-/archive/v%{version}/%{pname}-v%{version}.tar.bz2
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
VDR plugin: tvguide - %{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pname}-v%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" IMAGELIB=graphicsmagick

%install
# make install would install the themes under /etc, let's not use that
make install-lib install-i18n install-icons DESTDIR=%{buildroot}
# install the themes to the custom location used in Fedora
install -dm 755 %{buildroot}%{vdr_vardir}/themes
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/

# tvguide.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/tvguide.conf

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING HISTORY* README*
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/tvguide.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/tvguide-*.theme
%{vdr_resdir}/plugins/tvguide/

%changelog
%autochangelog
