%global source0_hash 127a24cde208c65b837ae978c695a00730f1094ee8b6c7d48cf58ef846eae340
Name:           rauc
Version:        1.15.2
Release:        1%{?dist}
Summary:        Safe and secure software updates for embedded Linux
License:        LGPL-2.1-or-later AND CC0-1.0
URL:            https://rauc.io/
Source0:        https://github.com/rauc/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         rauc_patch0_grub_editenv_debian_compat_fix.patch
Patch1:         rauc_patch1_disable_http_test.patch
ExcludeArch:    s390 s390x i686
Requires:       dbus-common
Recommends:     rauc-doc
# oreon:deps
BuildRequires:  dbus-daemon
BuildRequires:  dbus-devel
BuildRequires:  e2fsprogs
BuildRequires:  fakeroot
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  grub2-tools-minimal
BuildRequires:  json-glib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libfdisk-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  python3-dasbus
BuildRequires:  python3-pyasn1
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  squashfs-tools
BuildRequires:  systemd-devel
BuildRequires:  texinfo
BuildRequires:  thorvg
# /oreon:deps
%package doc
Summary:        RAUC documentation
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  thorvg
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
%description doc
Documentation for RAUC.

%description
RAUC is a lightweight update client that runs on your Embedded Linux device
and reliably controls the procedure of updating your device with a new firmware
revision. RAUC is also the tool on your host system that lets you create,
inspect and modify update artifacts for your device.
Service is not installed as that is only needed on device.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -v -N
# Debian vs. Fedora grub2 packaging difference
%patch -P 0 -b .orig
# rauc:pytest-http fails with Connection refused on 127.0.0.1
%patch -P 1 -b .orig
# Debian vs. Fedora grub2 packaging difference
cd test/bin
ln -sf grub-editenv grub2-editenv

%build

%meson \
        -Dfuzzing=false \
        -Dhtmldocs=false \
        -Dmanpages=true \
        -Dservice=false \
        -Dstreaming=false \
        -Dnetwork=false \
        -Dpkcs11_engine=false
%meson_build
pushd docs
pushd images
tvg-svg2png . || tvg_svg2png .
popd
sed -i "s/\.svg/\.png/g" *.rst
tvg-svg2png RAUC_Logo_outline.svg || tvg_svg2png RAUC_Logo_outline.svg
sed -i "s/html_logo = 'RAUC_Logo_outline.svg'/html_logo = 'RAUC_Logo_outline.png'/g" conf.py
sphinx-build . texinfo -b texinfo
pushd texinfo
makeinfo --docbook %{name}.texi
popd
popd
%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/help/en/%{name}
install -m644 docs/texinfo/%{name}.xml %{buildroot}%{_datadir}/help/en/%{name}
cp -p -r docs/texinfo/%{name}-figures %{buildroot}%{_datadir}/help/en/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n rauc-doc -f %{oreon_filedir}/rauc-doc.list

%changelog

%autochangelog
