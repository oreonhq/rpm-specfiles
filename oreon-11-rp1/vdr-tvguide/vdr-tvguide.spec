%global source0_hash 23f3c01e4eabb82389923ea229b6dbd248cea512651ba9ea60ba798c4e1bc31c
%global pname   tvguide
%global vdr_version 2.6.9
Name:           vdr-tvguide
Version:        1.3.12
Release:        2%{?dist}
Summary:        TvGuide is a highly customizable 2D EPG viewer plugin
License:        GPL-2.0-or-later
URL:            https://gitlab.com/kamel5/tvguide
Source0:        https://gitlab.com/kamel5/%{pname}/-/archive/v%{version}/%{pname}-v%{version}.tar.bz2
Source1:        %{name}.conf
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  vdr-devel
# /oreon:deps
%description 
VDR plugin: tvguide - %{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pname}-v%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

%build

%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" IMAGELIB=graphicsmagick
%install
make install-lib install-i18n install-icons DESTDIR=%{buildroot}
install -dm 755 %{buildroot}%{vdr_vardir}/themes
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/tvguide.conf
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
