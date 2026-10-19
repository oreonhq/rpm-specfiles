%global source0_hash a0d26931bf731f97514da266d079d8bc7d73c65b3499ed080576ab606b21c0ce
Summary:        User configurable send-only Mail Transfer Agent
Summary(de):    Benutzerkonfigurierbarer nur versendender Mail Transfer Agent (MTA)
Name:           esmtp
Version:        1.2
Release:        1%{?dist}
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        esmtp-0.4.1-mutt
Source2:        esmtprc-mda
Url:            http://esmtp.sourceforge.net/
License:        GPL-1.0-or-later AND GPL-2.0-or-later
Requires(post):  %{_sbindir}/alternatives
Requires(preun): %{_sbindir}/alternatives
Requires:       coreutils, liblockfile
Patch0:	esmtp-1.2-cron-fix.patch
Patch1: 0001-Deliver-mail-to-user-localhost-locally-using-a-MDA.patch
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/sendmail
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libesmtp-devel
BuildRequires:  make
# /oreon:deps
%description
ESMTP is a user configurable relay-only Mail Transfer Agent (MTA) with a
sendmail-compatible syntax. It's based on libESMTP supporting the AUTH
(including the CRAM-MD5 and NTLM SASL mechanisms) and the StartTLS SMTP
extensions.

%description -l de
ESMTP ist ein benutzerkonfigurierbarer nur versendender Mail Transfer
Agent (MTA) mit einem Sendmail-kompatiblen Syntax. Es basiert auf
libESMTP und unterstützt AUTH (mit CRAM-MD5 und NTLM SASL) und StartTLS
SMTP.

%package local-delivery
Summary:        Configuration for esmtp allowing for local delivery
Requires:       %{name} = %{version}-%{release}
Requires:       procmail
Provides:       mail(local)
%description local-delivery
This packages contains the system ESMTP configuration file with local
delivery through an external mail delivery agent configured.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .cron-fix
%patch -P1 -p1 -b .localhost
cp -p %{SOURCE1} mutt-esmtp
for file in esmtp.1 esmtprc.5; do
   iconv -f ISO8859-1 -t UTF8 < $file > $file.new && touch -r $file $file.new && mv -f $file.new $file
done

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/esmtprc
install -p -m0755 esmtp-wrapper %{buildroot}%{_bindir}
rm -f %{buildroot}%{_bindir}/mailq
touch %{buildroot}%{_bindir}/mailq
rm -f %{buildroot}%{_libdir}/sendmail
mkdir -p %{buildroot}%{_prefix}/lib
touch %{buildroot}%{_prefix}/lib/sendmail
rm -f %{buildroot}%{_sbindir}/sendmail
touch %{buildroot}%{_sbindir}/sendmail
rm -f %{buildroot}%{_mandir}/man1/sendmail.1*
touch %{buildroot}%{_mandir}/man1/mailq.1.gz
mkdir -p %{buildroot}%{_mandir}/man8/
touch %{buildroot}%{_mandir}/man8/sendmail.8.gz
rm -f %{buildroot}%{_bindir}/newaliases %{buildroot}%{_mandir}/man1/newaliases.1*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%{_sbindir}/alternatives --install %{_sbindir}/sendmail mta %{_bindir}/esmtp-wrapper 30 \
  --slave %{_prefix}/lib/sendmail mta-sendmail %{_bindir}/esmtp-wrapper \
  --slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man1/esmtp.1.gz \
  --slave %{_bindir}/mailq mta-mailq %{_bindir}/esmtp-wrapper \
  --slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/esmtp.1.gz
%preun

if [ "$1" = 0 ]; then
   %{_sbindir}/alternatives --remove mta %{_bindir}/esmtp-wrapper
fi
%files -f %{oreon_filedir}/main.list
%files -n esmtp-local-delivery -f %{oreon_filedir}/esmtp-local-delivery.list

%changelog

%autochangelog
