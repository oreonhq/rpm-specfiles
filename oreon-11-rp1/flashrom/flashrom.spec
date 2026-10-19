%global source1_hash 5e43e6fe931a43684f847e61c07935bc008f639d2c6bad1cdec44a6483721bd2
%global source0_hash 654c9c61745c250cd3b5ccd0e56fc43ee76980f92a5e078420420639d66975a2
%global source2_key_fpr 6E6EF9A0BA478006E2776E4CC037BB413134D111
Name:		flashrom
Version:	1.8.0
Release:        1%{?dist}
Summary:        Simple program for reading/writing flash chips content
License:	GPL-2.0-only
URL:		https://flashrom.org
Source0:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.xz
Source1:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.xz.asc
Source2:	6E6EF9A0BA478006E2776E4CC037BB413134D111.gpg
%ifarch %{ix86} x86_64 aarch64
Requires:	dmidecode
%endif
Requires:	udev
ExcludeArch:	s390 s390x
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libusb1-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  pciutils-devel
BuildRequires:  python3-sphinx
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
flashrom is a utility for identifying, reading, writing, verifying and erasing
flash chips. It is designed to flash BIOS/EFI/coreboot/firmware/optionROM
images on mainboards, network/graphics/storage controller cards, and various
other programmer devices.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-v%{version}
# Replace GROUP="plugdev" specifiers with TAG+="uaccess"
sed -e 's/MODE="[0-9]*", GROUP="plugdev"/TAG+="uaccess"/g' util/flashrom_udev.rules -i

%build

%meson -Dtests=disabled -Ddocumentation=disabled
%meson_build
%install
%meson_install
install -D -p -m 0644 util/flashrom_udev.rules %{buildroot}/%{_udevrulesdir}/60_flashrom.rules
rm %{buildroot}/%{_libdir}/libflashrom.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n flashrom-devel -f %{oreon_filedir}/flashrom-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-3
- Prepare for Oreon 11 (RP1)
