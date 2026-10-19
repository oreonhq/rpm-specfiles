%global source4_hash 22b8a137176c28ecd12bb6fde8c44662b555a470e79a5203105e363abf9307da
%global source3_hash ba6a11e8a4e255d6d874785485ff497947a213da3b7ad63e737b20086f42ca30
%global source1_hash ea91c2e717667c88de290800c874844c74ec1c3266d2ddbfbbbf5290feb582a9
%global source0_hash fc21dbae10055dee5e4f11a936691576059b40b85107b701221a54c744abd7b7
Name:           electron-cash
Version:        4.4.6
Release:        1%{?dist}
Summary:        A lightweight Bitcoin Cash client
License:        MIT
URL:            https://electroncash.org/
Source0:        https://github.com/Electron-Cash/Electron-Cash/releases/download/%{version}/electron_cash-%{version}.tar.gz
Source1:        https://github.com/Electron-Cash/keys-n-hashes/raw/master/sigs-and-sums/%{version}/win-linux/electron_cash-%{version}.tar.gz.asc
Source3:        https://raw.githubusercontent.com/Electron-Cash/Electron-Cash/refs/tags/4.4.2/electroncash/paymentrequest.proto
Source4:        https://raw.githubusercontent.com/Electron-Cash/Electron-Cash/refs/tags/4.4.2/electroncash_plugins/fusion/protobuf/fusion.proto
Source2:        gpgkey-electron-cash.gpg
Patch0:         dateutil-no-version.patch
BuildArch:      noarch
ExcludeArch:    %{ix86}
Requires:       qt5-qtbase
Requires:       qt5-qtsvg
Requires:       qt5-qtmultimedia
Requires:       python3-qt5
Requires:       python3-pycryptodomex
Requires:       python3-psutil
Requires:       python3-cryptography
Requires:       python3-zxing-cpp >= 2.0.0
Recommends:     libsecp256k1-abc
Requires:       zbar
Requires:       tor
Provides:       bundled(google-noto-emoji-color-fonts)
Suggests:       python3-trezor >= 0.12
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  protobuf-compiler
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Electron Cash is an easy to use Bitcoin Cash client. It protects you from losing
coins in a backup mistake or computer failure, because your wallet can
be recovered from a secret phrase that you can write on paper or learn
by heart. There is no waiting time when you start the client, because
it does not download the Bitcoin block chain.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n electron_cash-%{version}

#pre-built bundled library
rm -v ./electroncash/*.so*

#pre-built tor binary
rm -v ./electroncash/tor/bin/tor

#budled libraries
rm -rfv ./packages/

%build

pyrcc5 icons.qrc -o electroncash_gui/qt/icons_rc.py
install -D %{SOURCE3} electroncash/paymentrequest.proto
install -D %{SOURCE4} electroncash_plugins/fusion/protobuf/fusion.proto
protoc --proto_path=electroncash/ --python_out=electroncash/ electroncash/paymentrequest.proto
protoc --proto_path=electroncash_plugins/fusion/protobuf/ --python_out=electroncash_plugins/fusion/ electroncash_plugins/fusion/protobuf/fusion.proto
%{py3_build}
%install
%{py3_install}
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)
desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.electroncash.ElectronCash.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
