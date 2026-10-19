%global source2_hash 2e2d1246e73bef01cfce718d0e3c532a0007e9d0bc05dbd27c61464ef7182513
%global source0_hash 0b265ee3551dcddad5b62e188bdcab2cbb61a0d6a7e72107b2518a156b3ed665
Name:       dino
Version:    0.5.1
Release:        1%{?dist}
License:    GPL-3.0-only
Summary:        Modern XMPP ("Jabber") Chat Client using GTK+/Vala
URL:        https://github.com/dino/dino
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/dino-%{version}.tar.gz.asc
Source2:    https://dino.im/.well-known/openpgpkey/hu/kf5ictsogs7pr4rbewa9ie1he85r9ghc
Recommends: webp-pixbuf-loader
Requires:   filesystem
Requires:   gstreamer1-plugins-good
Requires:   hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  gpgme-devel
BuildRequires:  gspell-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgee-devel
BuildRequires:  libnice-devel
BuildRequires:  libnotify-devel
BuildRequires:  libomemo-c-devel
BuildRequires:  libsignal-protocol-c-devel
BuildRequires:  libsoup-devel
BuildRequires:  libsrtp-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(webrtc-audio-processing)
BuildRequires:  protobuf-c-devel
BuildRequires:  qrencode-devel
BuildRequires:  sqlite-devel
BuildRequires:  vala
# /oreon:deps
%description
A modern XMPP ("Jabber") chat client using GTK+/Vala.

%package devel
Summary:    Development files for dino
Requires:   dino%{?_isa} == %{version}-%{release}
%description devel
Development files for dino.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}

%build

%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%find_lang %{name}-omemo
%find_lang %{name}-openpgp
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/im.dino.Dino.desktop
%files -f %{oreon_filedir}/main.list
%files -n dino-devel -f %{oreon_filedir}/dino-devel.list

%changelog

%autochangelog
