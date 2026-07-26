%global source0_hash 6973ee582b193479ccb0e7d375ad208051236ee0318a17071d263397a2823189

# SNMP enabled by default
%bcond_without snmp

Summary:        Email filter with virus scanner and spamassassin support
Name:           amavis
Version:        2.14.0
Release:        4%{?dist}
# LDAP schema is GFDL-1.2-or-later, some helpers are BSD-2-Clause, core is GPL-2.0-or-later
License:        GPL-2.0-or-later AND BSD-2-Clause AND GFDL-1.2-or-later
URL:            https://gitlab.com/amavis/amavis
Source0:        https://gitlab.com/amavis/amavis/-/archive/v%{version}/amavis-v%{version}.tar.bz2
Source2:        amavis-clamd.conf
Source4:        README.fedora
Source5:        README.quarantine
Source8:        amavisd-tmpfiles.conf
Source9:        amavisd.service
Source10:       amavisd-snmp.service
Source11:       amavis.sysusers
Source12:       amavisd.sysconfig
Patch0:         amavis-conf.patch
BuildArch:      noarch
%if 0%{?fedora}
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
%if 0%{?rhel} > 7 || 0%{?fedora} > 24
Suggests:       %{name}-doc
Recommends:     clamav-server-systemd
Recommends:     clamav
Recommends:     binutils
Recommends:     arj
Recommends:     bzip2
Recommends:     cabextract
Recommends:     pax
Recommends:     freeze
Recommends:     gzip
Recommends:     lzop
Recommends:     nomarch
Recommends:     p7zip, p7zip-plugins
Recommends:     tar
Recommends:     unzoo
Recommends:     perl(DBD::SQLite)
Recommends:     perl(Convert::TNEF)
Recommends:     perl(Convert::UUlib)
%else
Requires:       binutils
Requires:       arj
Requires:       bzip2
Requires:       cabextract
Requires:       pax
Requires:       freeze
Requires:       gzip
Requires:       lzop
Requires:       nomarch
Requires:       p7zip, p7zip-plugins
Requires:       tar
Requires:       unzoo
Requires:       perl(DBD::SQLite)
%endif
Requires:       perl-Amavis = %{version}-%{release}
Requires:       clamav-filesystem
Requires:       altermime
Requires:       file
Requires:       perl(Archive::Tar)
Requires:       perl(Authen::SASL)
Requires:       perl(Compress::Raw::Zlib) >= 2.017
Requires:       perl(File::LibMagic)
Requires:       perl(IO::Socket::IP)
Requires:       perl(MIME::Body)
Requires:       perl(MIME::Decoder::Base64)
Requires:       perl(MIME::Decoder::Binary)
Requires:       perl(MIME::Decoder::Gzip64)
Requires:       perl(MIME::Decoder::NBit)
Requires:       perl(MIME::Decoder::QuotedPrint)
Requires:       perl(MIME::Decoder::UU)
Requires:       perl(MIME::Head)
Requires:       perl(Mail::Field)
Requires:       perl(Mail::Header)
Requires:       perl(Mail::Internet) >= 1.58
Requires:       perl(Mail::SPF)
Requires:       perl(Net::DNS)
Requires:       perl(Net::LibIDN2)
Requires:       perl(Net::SSLeay)
Requires:       perl(NetAddr::IP)
Requires:       perl(Razor2::Client::Version)
Requires:       perl(Socket)
Requires:       perl(URI)
Obsoletes:      amavisd-new-zeromq <= 2.11.0-5
Obsoletes:      amavisd-new-snmp-zeromq <= 2.11.0-5
Provides:       amavisd-new = %{version}-%{release}
Obsoletes:      amavisd-new < 2.12.0-3

%package -n perl-Amavis
Summary:        Amavis perl module

%if %{with snmp}
%package snmp
Summary:        Exports amavis SNMP data
Requires:       %{name} = %{version}-%{release}
Provides:       amavisd-new-snmp = %{version}-%{release}
Obsoletes:      amavisd-new-snmp < 2.12.0-3
%endif

%package doc
Summary:        Amavis doc files
Provides:       amavisd-new-doc = %{version}-%{release}
Obsoletes:      amavisd-new-doc < 2.12.0-3

%description -n perl-Amavis
Amavis perl module used by the amavis mail scanner service.

%description
amavis is a high-performance and reliable interface between mailer
(MTA) and one or more content checkers: virus scanners, and/or
Mail::SpamAssassin Perl module. It is written in Perl, assuring high
reliability, portability and maintainability. It talks to MTA via (E)SMTP
or LMTP, or by using helper programs. No timing gaps exist in the design
which could cause a mail loss.

%if %{with snmp}
%description snmp
This package contains the program amavisd-snmp-subagent, which can be
used as a SNMP AgentX, exporting amavisd statistical counters database
(snmp.db) as well as a child process status database (nanny.db) to a
SNMP daemon supporting the AgentX protocol (RFC 2741), such as NET-SNMP.

It is similar to combined existing utility programs amavisd-agent and
amavisd-nanny, but instead of writing results as text to stdout, it
exports data to a SNMP server running on a host (same or remote), making
them available to SNMP clients (such a Cacti or mrtg) for monitoring or
alerting purposes.
%endif

%description doc
Documentation files for amavis

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}
install -p -m 644 %{SOURCE4} %{SOURCE5} README_FILES/

%build

%install
mkdir -p -m 0755 %{buildroot}%{perl_vendorlib}
cp -pr lib/* %{buildroot}%{perl_vendorlib}/

install -D -p -m 755 bin/amavisd %{buildroot}%{_sbindir}/amavisd
%if %{?with_snmp}
install -D -p -m 755 bin/amavisd-snmp-subagent %{buildroot}%{_sbindir}/amavisd-snmp-subagent
%endif

mkdir -p %{buildroot}%{_bindir}
install -p -m 755 bin/amavisd-{agent,nanny,release,signer,submit} %{buildroot}%{_bindir}/

install -D -p -m 644 %{SOURCE9} %{buildroot}%{_unitdir}/amavisd.service
%if %{with snmp}
install -D -p -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/amavisd-snmp.service
%endif

mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/clamd.d
install -D -p -m 644 conf/amavisd.conf %{buildroot}%{_sysconfdir}/amavisd/amavisd.conf
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/clamd.d/amavisd.conf

mkdir -p %{buildroot}%{_localstatedir}/spool/amavisd/{tmp,db,quarantine}
mkdir -p %{buildroot}%{_rundir}/{clamd.amavisd,amavisd}

install -D -m 644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/amavisd.conf

install -p -D -m 0644 %{SOURCE11} %{buildroot}%{_sysusersdir}/amavis.conf

install -p -D -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/sysconfig/amavisd

%preun
%systemd_preun amavisd.service

%if %{with snmp}
%preun snmp
%systemd_preun amavisd-snmp.service
%endif

%post
%systemd_post amavisd.service

%if %{with snmp}
%post snmp
%systemd_post amavisd-snmp.service
%endif

%postun
%systemd_postun_with_restart amavisd.service

%if %{with snmp}
%postun snmp
%systemd_postun_with_restart amavisd-snmp.service
%endif

%files
%license LICENSE
%dir %{_sysconfdir}/amavisd/
%{_unitdir}/amavisd.service
%dir %{_sysconfdir}/clamd.d
%config(noreplace) %{_sysconfdir}/amavisd/amavisd.conf
%config(noreplace) %{_sysconfdir}/clamd.d/amavisd.conf
%{_sbindir}/amavisd
%{_bindir}/amavisd-agent
%{_bindir}/amavisd-nanny
%{_bindir}/amavisd-release
%{_bindir}/amavisd-signer
%{_bindir}/amavisd-submit
%dir %attr(750,amavis,amavis) %{_localstatedir}/spool/amavisd
%dir %attr(750,amavis,amavis) %{_localstatedir}/spool/amavisd/tmp
%dir %attr(750,amavis,amavis) %{_localstatedir}/spool/amavisd/db
%dir %attr(750,amavis,amavis) %{_localstatedir}/spool/amavisd/quarantine
%{_tmpfilesdir}/amavisd.conf
%{_sysusersdir}/amavis.conf
%dir %attr(755,amavis,amavis) %{_rundir}/amavisd
%dir %attr(770,amavis,clamupdate) %{_rundir}/clamd.amavisd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/amavisd

%files -n perl-Amavis
%license LICENSE
%{perl_vendorlib}/*

%if %{with snmp}
%files snmp
%doc AMAVIS-MIB.txt
%{_unitdir}/amavisd-snmp.service
%{_sbindir}/amavisd-snmp-subagent
%endif

%files doc
%license LICENSE
%doc AAAREADME.first contrib/LDAP.schema contrib/LDAP.ldif RELEASE_NOTES TODO
%doc README_FILES conf/amavisd.conf-* conf/amavisd-custom.conf

%changelog
%autochangelog
