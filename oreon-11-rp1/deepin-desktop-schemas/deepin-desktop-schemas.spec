%global source0_hash a7a6a5ab637e4ff666de96b091af1b351fd585b90df266b0adea125d8c5632ca
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/linuxdeepin/deepin-desktop-schemas
Version:                6.0.13
%global tag             6.0.13
%gometa -L
Name:           deepin-desktop-schemas
Release:        1%{?dist}
Summary:        GSettings deepin desktop-wide schemas
License:        CC-BY-4.0 AND CC0-1.0 AND GPL-3.0-only AND GPL-3.0-or-later
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
%if %{with check}
%endif
Requires:       dconf
Requires:       deepin-gtk-theme
Requires:       deepin-icon-theme
Requires:       deepin-sound-theme
Obsoletes:      deepin-artwork-themes <= 15.12.4
# oreon:deps
BuildRequires:  glib2
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
deepin-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

# fix default background url
sed -i "s#/usr/share/backgrounds/default_background.jpg#/usr/share/backgrounds/deepin/desktop.jpg#" \
    overrides/common/com.deepin.wrap.gnome.desktop.override \
    schemas/com.deepin.dde.appearance.gschema.xml

sed -i 's|python|python3|' Makefile tools/overrides.py
# connectivity check uri copy from /usr/lib/NetworkManager/conf.d/20-connectivity-fedora.conf
sed -i "s#'http://detect.uniontech.com', 'http://detectportal.deepin.com'#'http://fedoraproject.org/static/hotspot.txt'#" \
    schemas/com.deepin.dde.network-utils.gschema.xml
grep uniontech schemas/com.deepin.dde.network-utils.gschema.xml && exit 1 || :

%build

%global gomodulesmode GO111MODULE=on
%make_build
%install
%go_vendor_license_install -c %{S:2}
%make_install
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
