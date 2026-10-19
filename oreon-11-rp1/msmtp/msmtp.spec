%global source2_hash 4e3a0863dd448b928c5acba130974a16c1aff9a396a1b9e9cca067a198265f5e
%global source1_hash 503681da6c443708b901965ad5de50335d8cd5a43bbd57a5034637be1abfad12
%global source0_hash 84e8fe2a5a80a1ee7802013b3fbdb846a3f27a4163cf37a1c6d7c7f888873ead
Name:		msmtp
Version:	1.8.34
Release:        1%{?dist}
Summary:        SMTP client
License:	GPL-3.0-or-later
URL:		https://marlam.de/msmtp/
Source0:        https://marlam.de/msmtp/releases/%{name}-%{version}.tar.xz
Source1:	https://marlam.de/msmtp/releases/%{name}-%{version}.tar.xz.sig
Source2:	https://marlam.de/key.txt
Source3:	%{name}.rpmlintrc
Requires(post):		%{_sbindir}/alternatives /sbin/install-info
Requires(postun):	%{_sbindir}/alternatives /sbin/install-info
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/sendmail
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  libsecret-devel
BuildRequires:  make
# /oreon:deps
%description
It forwards messages to an SMTP server which does the delivery.
Features include:
  * Sendmail compatible interface (command line options and exit codes).
  * Authentication methods PLAIN,LOGIN,CRAM-MD5,DIGEST-MD5,GSSAPI,and NTLM
  * TLS/SSL both in SMTP-over-SSL mode and in STARTTLS mode.
  * Fast SMTP implementation using command pipe-lining.
  * Support for Internationalized Domain Names (IDN).
  * DSN (Delivery Status Notification) support.
  * RMQS (Remote Message Queue Starting) support (ETRN keyword).
  * IPv6 support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

gettextize -f
autoreconf -ivf
%configure --disable-rpath --with-libsecret --with-libgsasl
%make_build
%install
%make_install
%find_lang %{name}
rm -f scripts/Makefile*
rm -f %{buildroot}%{_infodir}/dir
touch %{buildroot}%{_bindir}/msmtp
rm -f %{buildroot}%{_libdir}/sendmail
mkdir -p %{buildroot}%{_prefix}/lib
touch %{buildroot}%{_prefix}/lib/sendmail
rm -f %{buildroot}%{_sbindir}/sendmail
mkdir -p %{buildroot}%{_sbindir}/sendmail
touch %{buildroot}%{_sbindir}/sendmail
rm -f %{buildroot}%{_mandir}/man1/sendmail.1*
mkdir -p %{buildroot}%{_mandir}/man8/
touch %{buildroot}%{_mandir}/man8/sendmail.8.gz
rm -f %{buildroot}%{_bindir}/newaliases %{buildroot}%{_mandir}/man1/newaliases.1* %{buildroot}%{_bindir}/mailq
%oreon_autofiles main

%post

%{_sbindir}/alternatives --install %{_sbindir}/sendmail mta %{_bindir}/msmtp 40 \
  --slave %{_prefix}/lib/sendmail mta-sendmail %{_bindir}/msmtp \
  --slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man1/msmtp.1.gz \
  --slave %{_bindir}/mailq mta-mailq %{_bindir}/msmtp \
  --slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/msmtp.1.gz
%postun

if [ $1 -eq 0 ] ; then
	%{_sbindir}/alternatives --remove mta %{_bindir}/msmtp
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
