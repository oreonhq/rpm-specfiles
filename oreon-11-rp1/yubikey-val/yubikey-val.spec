%global source0_hash b6a9374a804ee93346dcfc3f8e8790c1cc3fe21867bc6a86206dadae06bdd84e

Name:       yubikey-val
Version:    2.39
Release:    16%{?dist}
Summary:    The YubiKey Validation Server

License:    BSD
URL:        https://developers.yubico.com/yubikey-val
Source0:    https://developers.yubico.com/yubikey-val/Releases/yubikey-val-%{version}.tgz
# Apache config file
Source1:    yubikey-val.conf
# Remove --group from install
Patch0:     yubikey-val-install.patch
BuildArch:  noarch

BuildRequires: make
BuildRequires:  httpd-devel
Requires:   httpd
Requires:   php php-curl php-pear php-pdo

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

%files
%license COPYING
%doc ChangeLog NEWS README doc/* ykval-db.sql
%dir %{_sysconfdir}/yubico
%dir %{_sysconfdir}/yubico/val
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/yubico/val/ykval-config.php
%config(noreplace) %{_httpd_confdir}/yubikey-val.conf
%{_datadir}/yubikey-val/
%{_sbindir}/*
%{_mandir}/man1/*.1*

%files munin
%{_datadir}/munin/plugins/*

%changelog
%autochangelog
