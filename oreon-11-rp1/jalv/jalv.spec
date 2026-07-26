%global source0_hash 6dfa7f8709047c8ed944541dc093a6b5762990a9f49dce4c6a8bf1f922243bf4

Name:       jalv
Version:    1.8.0
Release:    1%{?dist}
Summary:    A simple but fully featured LV2 host for Jack

License:    MIT
URL:        https://drobilla.net/software/%{name}.html
Source0:    https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:    https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:    https://drobilla.net/drobilla.gpg

BuildRequires:  python3
BuildRequires:  meson
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gnupg2
BuildRequires:  lilv-devel >= 0.26.0
BuildRequires:  suil-devel >= 0.10.0
BuildRequires:  serd-devel >= 0.30.2
BuildRequires:  sord-devel >= 0.16.16
BuildRequires:  sratom-devel >= 0.6.4
BuildRequires:  lv2-devel >= 1.18.0
BuildRequires:  jack-audio-connection-kit-devel >= 1.9.10
BuildRequires:  gtk2-devel >= 2.18.0
BuildRequires:  gtk3-devel >= 3.0.0
BuildRequires:  gtkmm24-devel >= 2.20.0
BuildRequires:  qt5-qtbase-devel >= 5.1.0
BuildRequires:  qt6-qtbase-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  mandoc
BuildRequires:  libappstream-glib
Requires:       lv2 >= 1.18.0

# gtkmm is no longer supported
Obsoletes:      jalv-gtkmm < 1.6.8

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

%check
%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_libdir}/jack/%{name}.so
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/*.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files qt
%{_bindir}/%{name}.qt*
%{_mandir}/man1/%{name}.qt*.1.*

%files gtk
%{_bindir}/%{name}.gtk3
%{_mandir}/man1/%{name}.gtk3.1.*

%changelog
%autochangelog
