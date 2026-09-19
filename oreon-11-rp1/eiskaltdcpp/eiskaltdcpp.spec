%global source0_hash 2ed853a57c57aab0e87fdea273a01707184ee425a2aaf9fcd2e0a32c57a2de2c

Name:           eiskaltdcpp
Version:        2.4.2
Release:        23%{?dist}
Summary:        Direct Connect client

# The entire source code is GPLv3+ except FlowLayout.cpp and .h which is LGPLv2+
# Automatically converted from old format: GPLv3+ and LGPLv2+ - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/eiskaltdcpp/eiskaltdcpp
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         https://github.com/eiskaltdcpp/eiskaltdcpp/commit/5ab5e1137a46864b6ecd1ca302756da8b833f754.patch

BuildRequires:  cmake >= 2.6.3
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(aspell)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  perl-generators

Requires:       %{name}-data = %{version}-%{release}

%description
EiskaltDC++ is a cross-platform program that uses the Direct Connect
(DC aka NMDC) and Advanced Direct Connect (ADC) protocols. It is compatible
with DC++, AirDC++, FlylinkDC++ and other DC clients. EiskaltDC++ also
interoperates with all common DC hub software.

%package xmlrpc
Summary:    CLI xmlrpc
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description xmlrpc
Subpackage with CLI xmlrpc for %{name}.

%package gtk
Summary:    GTK-based graphical interface
Requires:   %{name}%{?_isa} = %{version}-%{release}
Provides:   %{name}-gui%{?_isa} = %{version}-%{release}

%description gtk
GTK+ 3 interface using GTK+ 3 library.

%package qt
Summary:    Qt-based graphical interface
Requires:   %{name}%{?_isa} = %{version}-%{release}
Provides:   %{name}-gui%{?_isa} = %{version}-%{release}

%description qt
Qt-based graphical interface.

%package data
Summary:    Data files for eiskaltdcpp
Requires:   %{name} = %{version}-%{release}
Requires:   hicolor-icon-theme
BuildArch:  noarch

%description data
Necessary data files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove bundled libs
rm -rf upnp
rm -rf data/examples/*.php eiskaltdcpp-qt/qtscripts/gnome/*.php
# Correct rpmlint W: crypto-policy-non-compliance-openssl
sed -i '/SSL_CTX_set_cipher_list/d' dcpp/CryptoManager.cpp

%build
# TODO: Please submit an issue to upstream (rhbz#2380564)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
    -DUSE_ASPELL=ON \
    -DFREE_SPACE_BAR_C=ON \
    -DUSE_MINIUPNP=ON \
    -DUSE_GTK3=ON \
    -DDBUS_NOTIFY=ON \
    -DUSE_JS=ON \
    -DPERL_REGEX=ON \
    -DUSE_CLI_XMLRPC=ON \
    -DWITH_SOUNDS=ON \
    -DLUA_SCRIPT=ON \
    -DWITH_LUASCRIPTS=ON
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}-gtk
%find_lang lib%{name}

%files -f lib%{name}.lang
%doc AUTHORS ChangeLog.txt README.md TODO
%license COPYING LICENSE
%{_bindir}/%{name}-daemon
%{_libdir}/libeiskaltdcpp.so.*
%{_mandir}/man?/%{name}-daemon.1.*

%files xmlrpc
%{_bindir}/%{name}-cli-xmlrpc
%{_mandir}/man?/%{name}-cli-xmlrpc.1.*

%files gtk -f %{name}-gtk.lang
%{_bindir}/*gtk
%{_mandir}/man?/*gtk*
%{_datadir}/%{name}/gtk
%{_datadir}/applications/*gtk*.desktop

%files qt
%{_bindir}/*qt
%{_mandir}/man?/*qt*
%{_datadir}/%{name}/qt
%{_datadir}/applications/*qt*.desktop

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/cli
%{_datadir}/%{name}/luascripts
%{_datadir}/%{name}/emoticons
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/sounds
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/*.png

%changelog
%autochangelog
