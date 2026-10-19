%global source2_hash 6efbd4c8220ef3446d7f31f7ccddbe43017e4f3f31294e06bb816a44418ba133
%global source1_hash 12dd20bfc11af3e6bcd7c16e9ede8ea7883b354ba75d83d6f77a59f942f2a4b5
%global source0_hash be34eeb297881adea4f894c7c6e4a1835bd7927f8043ddea495040df4792a7de
%undefine __cmake_in_source_build
Name:           keepassxc
Version:        2.7.12
Release:        1%{?dist}
Summary:        Cross-platform password manager
License:        BSL-1.0 AND LicenseRef-Callaway-BSD AND CC0-1.0 AND GPL-3.0-only AND LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-LGPLv2+ AND LGPL-3.0-or-later AND LicenseRef-Callaway-Public-Domain
URL:            https://keepassxc.org/
Source0:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz
Source1:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz.sig
Source2:        https://keepassxc.org/keepassxc_master_signing_key.asc
%if 0%{?el8} || 0%{?el9}
%else
%endif
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Provides: bundled(ykcore)
Recommends: (wl-clipboard if gnome-shell)
# oreon:deps
BuildRequires:  botan2-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glibc-langpack-en
BuildRequires:  gnupg2
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  libappstream-glib
BuildRequires:  libargon2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libsodium-devel
BuildRequires:  libusb1-devel
BuildRequires:  libyubikey-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  qrencode-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  readline-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  zlib-devel
# /oreon:deps
%description
KeePassXC is a community fork of KeePassX
KeePassXC is an application for people with extremely high demands on secure
personal data management.
KeePassXC saves many different information e.g. user names, passwords, urls,
attachemts and comments in one single database. For a better management
user-defined titles and icons can be specified for each single entry.
Furthermore the entries are sorted in groups, which are customizable as well.
The integrated search function allows to search in a single group or the
complete database.
KeePassXC offers a little utility for secure password generation. The password
generator is very customizable, fast and easy to use. Especially someone who
generates passwords frequently will appreciate this feature.
The complete database is always encrypted either with AES (alias Rijndael) or
Twofish encryption algorithm using a 256 bit key. Therefore the saved
information can be considered as quite safe.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%setup -q
%autopatch -p1

# Older version of appstream-util can't parse some url types

# Older version of desktop-file-utils before 0.26 don't know about some fields
# Remove when desktop-file-utils 0.26 is available in EPEL8

%build

%cmake \
    %{?flatpak:-DKEEPASSXC_DIST_TYPE=Flatpak} \
    -DCMAKE_BUILD_TYPE=Release \
    -DKEEPASSXC_BUILD_TYPE=Release \
    -DWITH_XC_ALL=ON \
    -DWITH_XC_DOCS=ON \
    -DWITH_XC_UPDATECHECK=OFF
%cmake_build
%install
%cmake_install
%if %{defined flatpak}
install -m0755 utils/keepassxc-flatpak-wrapper.sh %{buildroot}%{_bindir}/keepassxc-wrapper
%endif
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original \
    --add-mime-type application/x-keepassxc \
    %{buildroot}%{_datadir}/applications/org.%{name}.KeePassXC.desktop
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

export LC_ALL=en_US.UTF-8
%ctest --exclude-regex testcli
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.KeePassXC.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.%{name}.KeePassXC.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
