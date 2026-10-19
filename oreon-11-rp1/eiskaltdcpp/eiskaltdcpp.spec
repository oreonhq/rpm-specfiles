%global source0_hash 2ed853a57c57aab0e87fdea273a01707184ee425a2aaf9fcd2e0a32c57a2de2c
Name:           eiskaltdcpp
Version:        2.4.2
Release:        1%{?dist}
Summary:        Direct Connect client
License:        GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/eiskaltdcpp/eiskaltdcpp
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://github.com/eiskaltdcpp/eiskaltdcpp/commit/5ab5e1137a46864b6ecd1ca302756da8b833f754.patch
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(aspell)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%find_lang %{name}-gtk
%find_lang lib%{name}
%files -f %{oreon_filedir}/main.list
%files -n eiskaltdcpp-xmlrpc -f %{oreon_filedir}/eiskaltdcpp-xmlrpc.list
%files -n eiskaltdcpp-gtk -f %{oreon_filedir}/eiskaltdcpp-gtk.list
%files -n eiskaltdcpp-qt -f %{oreon_filedir}/eiskaltdcpp-qt.list
%files -n eiskaltdcpp-data -f %{oreon_filedir}/eiskaltdcpp-data.list

%changelog

%autochangelog
