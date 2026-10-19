%global source0_hash e329a0da0b6dd888916046535ff86a6aa144644561937954e560bb1810ab6702
Name:           reaver
Version:        1.6.6
Release:        1%{?dist}
Summary:        Brute force attack against Wifi Protected Setup
License:        GPL-2.0-only
URL:            https://github.com/t6x/reaver-wps-fork-t6x
Source0:        https://github.com/t6x/%{name}-wps-fork-t6x/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         reaver-lwe-unbundle.patch
Patch1:         reaver-1.6.6-switch-to-libnl3.patch
Provides:       bundled(wpa_supplicant) = 0.7.3
Recommends:     pixiewps
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Reaver implements a brute force attack against Wifi Protected Setup (WPS)
registrar PINs in order to recover WPA/WPA2 passphrases, as described in
http://sviehb.files.wordpress.com/2011/12/viehboeck_wps.pdf.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove executable mode from sources
find . -type f -perm /111 -regex ".*\.[ch]" -exec chmod a-x {} \;

# Unbundle wireless-tools
rm -rf src/lwe

%build

pushd src
    %configure
    %make_build
popd
%install
pushd src
    %make_install
popd
mkdir -p %{buildroot}%{_mandir}/man1
install -pm0644 docs/reaver.1 %{buildroot}%{_mandir}/man1/
touch %{buildroot}%{_localstatedir}/lib/reaver/reaver.db
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
