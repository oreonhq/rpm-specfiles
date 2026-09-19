%global source0_hash e329a0da0b6dd888916046535ff86a6aa144644561937954e560bb1810ab6702

Name:           reaver
Version:        1.6.6
Release:        17%{?dist}
Summary:        Brute force attack against Wifi Protected Setup

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/t6x/reaver-wps-fork-t6x
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         reaver-lwe-unbundle.patch
# rhbz#2031312
# https://github.com/t6x/reaver-wps-fork-t6x/issues/349
Patch1:         reaver-1.6.6-switch-to-libnl3.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  sqlite-devel
BuildRequires:  libnl3-devel
# https://fedorahosted.org/fpc/ticket/418
Provides:       bundled(wpa_supplicant) = 0.7.3
# change to requires once pixiewps will get stable
Recommends:     pixiewps

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

%files
%doc docs/README docs/README.REAVER docs/README.WASH
%license docs/LICENSE
%{_bindir}/reaver
%{_bindir}/wash
%ghost %{_localstatedir}/lib/reaver/reaver.db
%{_mandir}/man1/*.1*

%changelog
%autochangelog
