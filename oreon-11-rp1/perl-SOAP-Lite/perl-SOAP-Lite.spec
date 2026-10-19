%global source0_hash e359106bab1a45a16044a4c2f8049fad034e5ded1517990bc9b5f8d86dddd301
Name:       perl-SOAP-Lite
Version:    1.27
Release:        1%{?dist}
Summary:        Client and server side SOAP implementation
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/SOAP-Lite
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/SOAP-Lite-%{version}.tar.gz
Patch0:     SOAP-Lite-1.22-Remove-usr-bin-env-from-shebang.patch
BuildArch:  noarch
Requires:       perl(Compress::Zlib)
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
Provides:       perl-SOAP-Transport-TCP = %{version}-%{release}
Obsoletes:      perl-SOAP-Transport-TCP < 0.715-12
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(My::.*\\)
%global __provides_exclude %__provides_exclude|perl\\(LWP::Protocol\\)
%global __requires_exclude %{?_requires_exclude:%__requires_exclude|}perl\\(My::\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::SessionData)
BuildRequires:  perl(IO::SessionSet)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Net::POP3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::XML)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Parser::Lite)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
