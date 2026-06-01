%global source0_hash none

%global source2_key_fpr 6E6EF9A0BA478006E2776E4CC037BB413134D111

Name:		flashrom
Version:	1.6.0
Release:	3%{?dist}
Summary:	Simple program for reading/writing flash chips content
License:	GPL-2.0-only
URL:		https://flashrom.org

Source0:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.xz
Source1:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.xz.asc
# Find which key was used for signing the release:
#
# $ LANG=C gpg --verify flashrom-v1.3.0.tar.bz2.asc flashrom-v1.3.0.tar.bz2
# gpg: Signature made Wed Feb  8 03:57:51 2023 CET
# gpg:                using DSA key 6E6EF9A0BA478006E2776E4CC037BB413134D111
# gpg: Can't check signature: No public key
#
# Now export the key required as follows:
#
# gpg --no-default-keyring --keyring ./keyring.gpg --keyserver keyserver.ubuntu.com --recv-key 6E6EF9A0BA478006E2776E4CC037BB413134D111
# gpg --no-default-keyring --keyring ./keyring.gpg  --output 6E6EF9A0BA478006E2776E4CC037BB413134D111.gpg --export
Source2:	6E6EF9A0BA478006E2776E4CC037BB413134D111.gpg
BuildRequires:	gcc
BuildRequires:	gnupg2
%if ! 0%{?rhel}
BuildRequires:	libftdi-devel
BuildRequires:	libjaylink-devel
%endif
BuildRequires:	libusb1-devel
BuildRequires:	meson
BuildRequires:	openssl-devel
BuildRequires:	pciutils-devel
BuildRequires:	python3-sphinx
BuildRequires:	systemd
BuildRequires:	zlib-devel
%ifarch %{ix86} x86_64 aarch64
BuildRequires:	dmidecode
Requires:	dmidecode
%endif
Requires:	udev
# see rhbz #495226
ExcludeArch:	s390 s390x


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

%files
%license COPYING
%doc README.rst doc/
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.*
%{_udevrulesdir}/60_flashrom.rules
%{_datadir}/bash-completion/completions/%{name}.bash
%{_libdir}/libflashrom.so.1
%{_libdir}/libflashrom.so.1.0.0

%files devel
%{_includedir}/libflashrom.h
%{_libdir}/libflashrom.so
%{_libdir}/pkgconfig/flashrom.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-3
- Prepare for Oreon 11 (RP1)
