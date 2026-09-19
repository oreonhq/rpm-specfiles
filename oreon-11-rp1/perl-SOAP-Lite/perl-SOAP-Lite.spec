%global source0_hash e359106bab1a45a16044a4c2f8049fad034e5ded1517990bc9b5f8d86dddd301

Name:       perl-SOAP-Lite
Version:    1.27
Release:    28%{?dist}
Summary:    Client and server side SOAP implementation
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/SOAP-Lite
Source0:    https://cpan.metacpan.org/authors/id/P/PH/PHRED/SOAP-Lite-%{version}.tar.gz
# Remove /usr/bin/env from shebang
Patch0:     SOAP-Lite-1.22-Remove-usr-bin-env-from-shebang.patch
BuildArch:  noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# XXX: BuildRequires:  perl(Apache)
# XXX: BuildRequires:  perl(Apache::Const)
# XXX: BuildRequires:  perl(Apache::Constants)
# XXX: BuildRequires:  perl(Apache::RequestIO)
# XXX: BuildRequires:  perl(Apache::RequestRec)
# XXX: BuildRequires:  perl(Apache2::Const)
# XXX: BuildRequires:  perl(Apache2::RequestIO)
# XXX: BuildRequires:  perl(Apache2::RequestRec)
# XXX: BuildRequires:  perl(Apache2::RequestUtil)
# XXX: BuildRequires:  perl(APR::Table)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(constant)
# FIXME: Unpackaged BuildRequires:  perl(DIME::Message)
# FIXME: Unpackaged BuildRequires:  perl(DIME::Payload)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# XXX: BuildRequires:  perl(FCGI)
BuildRequires:  perl(HTTP::Daemon)
# XXX: BuildRequires:  perl(HTTP::Daemon::SSL)
# XXX: BuildRequires:  perl(HTTP::Headers)
# XXX: BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::SessionData)
BuildRequires:  perl(IO::SessionSet)
BuildRequires:  perl(IO::Socket)
# XXX: BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
# XXX: BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Net::POP3)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
# XXX: BuildRequires:  perl(URI::_server)
BuildRequires:  perl(vars)
# XXX: BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Parser::Lite)
# Tests only
# Note many tests are skipped as they require an HTTP server set up
BuildRequires:  perl(B)
BuildRequires:  perl(blib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8)
# Optional tests only
# XXX: BuildRequires:  perl(LWP::Protocol::https)
# XXX: BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::XML)
# We need HTTP::Response in case Test::MockObject gets pulled in somehow
BuildRequires:  perl(HTTP::Response)
# XXX: BuildRequires:  perl(Test::Kwalitee) >= 1.21
# XXX: BuildRequires:  perl(Test::Pod) >= 1.41
# We don't require various webserver transports (Apache*/APR, FCGI);
# this would introduced a huge dependency chain and people will generally want only one
# The server also introduces a huge dependency chain not everyone really wants.
Requires:       perl(Compress::Zlib)
# FIXME: Unpackaged Requires:       perl(DIME::Message)
# FIXME: Unpackaged Requires:       perl(DIME::Payload)
Requires:       perl(Encode)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::Protocol::http)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent)
Requires:       perl(MIME::Base64)
Requires:       perl(MIME::Entity)
Requires:       perl(URI::_server)
Requires:       perl(XML::Parser)
# Merged back into SOAP-Lite in 1.00
Provides:       perl-SOAP-Transport-TCP = %{version}-%{release}
Obsoletes:      perl-SOAP-Transport-TCP < 0.715-12

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(My::.*\\)
%global __provides_exclude %__provides_exclude|perl\\(LWP::Protocol\\)
%global __requires_exclude %{?_requires_exclude:%__requires_exclude|}perl\\(My::\\)

%description
SOAP::Lite is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both on
client and server side.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n SOAP-Lite-%{version}
find examples -type f -exec chmod -c ugo-x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes HACKING README ReleaseNotes.txt examples
%{_bindir}/SOAPsh.pl
%{_bindir}/stubmaker.pl
%{perl_vendorlib}/SOAP
%{perl_vendorlib}/Apache
%{_mandir}/man3/Apache::SOAP.3pm{,.*}
%{_mandir}/man3/SOAP::*.3pm{,.*}
%{_mandir}/man1/SOAPsh.pl.1{,.*}
%{_mandir}/man1/stubmaker.pl.1{,.*}

%changelog
%autochangelog
