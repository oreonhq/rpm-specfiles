%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%global source1_hash 7f0b315548b1f1e285aebefc995af9d1ef3bb00bd59e63a442ce91bd376b9881
%global source0_hash 5b49a4344c4d5608d2e30e4db5332c857ca61fd6333fb6f32c8a6c469b6d37ad
Name:       jalv
Version:    1.10.0
Release:        1%{?dist}
Summary:        A simple but fully featured LV2 host for Jack
License:    MIT
URL:        https://drobilla.net/software/%{name}.html
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:    https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:    https://drobilla.net/drobilla.gpg
Requires:       lv2 >= 1.18.0
Obsoletes:      jalv-gtkmm < 1.6.8
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  graphviz
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtkmm24-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libappstream-glib
BuildRequires:  lilv-devel
BuildRequires:  lv2-devel
BuildRequires:  mandoc
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  serd-devel
BuildRequires:  sord-devel
BuildRequires:  sratom-devel
BuildRequires:  suil-devel
# /oreon:deps
%description
%{name} is a simple but fully featured LV2 host for Jack. It runs LV2 plugins 
and exposes their ports as Jack ports, essentially making any LV2 plugin 
function as a Jack application. 

%package qt
Summary:    QT implementation of %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}
%description qt
%{name}-qt is an LV2 host for QT LV2 plugins

%package gtk
Summary:    GTK implementation of %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}
%description gtk
%{name}-gtk is an LV2 host for GTK LV2 plugins

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson -Dportaudio=disabled -Dman_html=disabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n jalv-qt -f %{oreon_filedir}/jalv-qt.list
%files -n jalv-gtk -f %{oreon_filedir}/jalv-gtk.list

%changelog

%autochangelog
