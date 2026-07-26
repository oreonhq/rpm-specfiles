%global source0_hash 948d7d36ef263ba91b63d791f9a9b19148123fedbb5a075375f97510abde102d

Name:           electron-cash
Version:        4.4.3
Release:        1%{?dist}
Summary:        A lightweight Bitcoin Cash client

License:        MIT
URL:            https://electroncash.org/
Source0:        https://github.com/Electron-Cash/Electron-Cash/releases/download/%{version}/electron_cash-%{version}.tar.gz
Source1:        https://github.com/Electron-Cash/keys-n-hashes/raw/master/sigs-and-sums/%{version}/win-linux/electron_cash-%{version}.tar.gz.asc

Source3:        https://raw.githubusercontent.com/Electron-Cash/Electron-Cash/refs/tags/4.4.2/electroncash/paymentrequest.proto
Source4:        https://raw.githubusercontent.com/Electron-Cash/Electron-Cash/refs/tags/4.4.2/electroncash_plugins/fusion/protobuf/fusion.proto

#Sun 15 Dec 2019, exported the upstream gpg key using the command:
#gpg2 --armor --export --export-options export-minimal D56C110F4555F371AEEFCB254FD06489EFF1DDE1 D465135F97D0047E18E99DC321810A542031C02C > gpgkey-electron-cash.gpg
Source2:        gpgkey-electron-cash.gpg

#Fedora 43+ provides a newer version, makes it possible to install.
#No guarantees that it works at runtime.
Patch0:         dateutil-no-version.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qt5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  protobuf-compiler

BuildRequires:  libappstream-glib
BuildRequires:  gnupg2

Requires:       qt5-qtbase
Requires:       qt5-qtsvg
Requires:       qt5-qtmultimedia

# Manually from contrib/requirements/requirements-binaries.txt
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

#Re-compile the protobuf description files
install -D %{SOURCE3} electroncash/paymentrequest.proto
install -D %{SOURCE4} electroncash_plugins/fusion/protobuf/fusion.proto
protoc --proto_path=electroncash/ --python_out=electroncash/ electroncash/paymentrequest.proto
protoc --proto_path=electroncash_plugins/fusion/protobuf/ --python_out=electroncash_plugins/fusion/ electroncash_plugins/fusion/protobuf/fusion.proto

%{py3_build}

%install
%{py3_install}

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
# Source: dmalcolm.fedorapeople.org/python3.spec
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.electroncash.ElectronCash.appdata.xml

%files
%doc AUTHORS
%doc README.rst
%doc RELEASE-NOTES
%license LICENCE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.electroncash.ElectronCash.appdata.xml
%{python3_sitelib}/electroncash/
%{python3_sitelib}/electroncash_gui/
%{python3_sitelib}/electroncash_plugins/
%{python3_sitelib}/Electron_Cash-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
