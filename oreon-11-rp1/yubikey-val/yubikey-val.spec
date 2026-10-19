%global source0_hash b6a9374a804ee93346dcfc3f8e8790c1cc3fe21867bc6a86206dadae06bdd84e
Name:       yubikey-val
Version:    2.39
Release:        16%{?dist}
Summary:        The YubiKey Validation Server
License:    BSD
URL:        https://developers.yubico.com/yubikey-val
Source0:        https://developers.yubico.com/yubikey-val/Releases/yubikey-val-%{version}.tgz
Source1:    yubikey-val.conf
Patch0:     yubikey-val-install.patch
BuildArch:  noarch
Requires:   httpd
Requires:   php php-curl php-pear php-pdo
# oreon:deps
BuildRequires:  httpd-devel
BuildRequires:  make
# /oreon:deps
%description
This is a server that validates Yubikey OTPs. It is written in PHP, for use
with web servers such as Apache

%package munin
Summary:    Munin plugins for the YubiKey Validation Server
Requires:   %{name} = %{version}-%{release}
Requires:   munin
%description munin
Munin plugins for the YubiKey Validation Server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .install

%build

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_docdir}
chmod 644 $RPM_BUILD_ROOT%{_datadir}/*/*php
mkdir -p $RPM_BUILD_ROOT%{_httpd_confdir}
install -p -m 0644 %SOURCE1 $RPM_BUILD_ROOT%{_httpd_confdir}/yubikey-val.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n yubikey-val-munin -f %{oreon_filedir}/yubikey-val-munin.list

%changelog

%autochangelog
