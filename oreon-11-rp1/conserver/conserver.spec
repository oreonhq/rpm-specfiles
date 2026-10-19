%global source1_hash 3e4d1c8a91c68e21c92729a2a3135c567caa0ddccae3fa500c8bbceaf62acda7
%global source0_hash 202b2ace3e14f36bca4de6ccd43cc962a99853c1d50799672ce0ffc5c02f8404
  %bcond_with libwrap
Name:           conserver
Version:        8.3.0
Release:        1%{?dist}
Summary:        Serial console server daemon/client
License:        BSD-3-Clause AND Zlib
URL:            https://www.%{name}.com
Source0:        https://github.com/bstansell/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/bstansell/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        bstansell-gpg-key.asc
Source3:        %{name}.service
Patch0:         %{name}-no-exampledir.patch
%if %{with libwrap}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freeipmi-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  krb5-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Conserver is an application that allows multiple users to watch a serial
console at the same time.  It can log the data, allows users to take
write-access of a console (one at a time), and has a variety of bells
and whistles to accentuate that basic functionality.

%package client
Summary: Serial console client
%description client
This is the client package needed to interact with a Conserver daemon.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# disable stripping of binaries
find . -name Makefile.in -exec \
       sed -i 's/@INSTALL_PROGRAM@ -s/@INSTALL_PROGRAM@/g' {} \;

%build

%configure --with-freeipmi   \
           --with-gssapi     \
%if %{with libwrap}
           --with-libwrap    \
%endif
           --with-openssl    \
           --with-pam        \
           --with-port=782   \
           --with-striprealm
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}
for cfg in conserver.{cf,passwd}; do
  sed -e 's/^/#/' "conserver.cf/$cfg" > "%{buildroot}%{_sysconfdir}/$cfg"
done
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/conserver.service
%oreon_autofiles conserver-client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build test
%post

%systemd_post conserver.service
%preun

%systemd_preun conserver.service
%postun

%systemd_postun_with_restart conserver.service
%files -f %{oreon_filedir}/main.list
%files -n conserver-client -f %{oreon_filedir}/conserver-client.list

%changelog

%autochangelog
