%global source0_hash 202b2ace3e14f36bca4de6ccd43cc962a99853c1d50799672ce0ffc5c02f8404

# rhel 8+ do not ship tcp_wrappers
%if 0%{?rhel} == 7
  %bcond_without libwrap
%else
  %bcond_with libwrap
%endif

Name:           conserver
Version:        8.3.0
Release:        1%{?dist}
Summary:        Serial console server daemon/client

License:        BSD-3-Clause AND Zlib
URL:            https://www.%{name}.com

Source0:        https://github.com/bstansell/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/bstansell/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
# gpg --keyserver pgp.mit.edu --recv-key D8D14B91ACAF41E231F8686728E4B7253029E7F6
# gpg --output bstansell-gpg-key.asc --armor --export bryan@conserver.com
Source2:        bstansell-gpg-key.asc

# Additional sources
Source3:        %{name}.service

Patch0:         %{name}-no-exampledir.patch

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
%if %{with libwrap}
BuildRequires:  tcp_wrappers-devel
%endif

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

# put commented copies of the sample configure files in the
# system configuration directory
mkdir -p %{buildroot}%{_sysconfdir}
for cfg in conserver.{cf,passwd}; do
  sed -e 's/^/#/' "conserver.cf/$cfg" > "%{buildroot}%{_sysconfdir}/$cfg"
done

# install copy of systemd service
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/conserver.service

%check
%make_build test

%post
%systemd_post conserver.service

%preun
%systemd_preun conserver.service

%postun
%systemd_postun_with_restart conserver.service

%files
%doc CHANGES FAQ PROTOCOL README.md
%doc conserver.cf/{conserver.{cf,passwd},samples/}
%license LICENSE
%config(noreplace) %{_sysconfdir}/conserver.*
%{_unitdir}/conserver.service
%{_libexecdir}/conserver
%{_mandir}/man5/conserver.cf.5*
%{_mandir}/man5/conserver.passwd.5*
%{_mandir}/man8/conserver.8*
%{_sbindir}/conserver

%files client
%license LICENSE
%{_bindir}/console
%{_mandir}/man1/console.1*

%changelog
%autochangelog
