%global source0_hash dcd89f76cba7a1c42c5aa5478e091799f335ed56dbe751585137495b8d7c7fbe

%bcond_with network_tests

# TODO: BR: perl(HTTP::Tiny::Mech) and perl(WWW::Mechanize::Cached) when available

Name:		perl-MetaCPAN-Client
Version:	2.040000
Release:	1%{?dist}
Summary:	A comprehensive, DWIM-featured client to the MetaCPAN API
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://github.com/CPAN-API/metacpan-client
Source0:	http://www.cpan.org/authors/id/M/MI/MICKEY/MetaCPAN-Client-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(blib) >= 1.01
BuildRequires:	perl(ExtUtils::MakeMaker) > 7.11
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(HTTP::Tiny) >= 0.056
BuildRequires:	perl(IO::Socket::SSL) >= 1.42
BuildRequires:	perl(JSON::MaybeXS)
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(Moo)
BuildRequires:	perl(Moo::Role)
BuildRequires:	perl(Net::SSLeay) >= 1.49
BuildRequires:	perl(parent)
BuildRequires:	perl(Ref::Util)
BuildRequires:	perl(Safe::Isa)
BuildRequires:	perl(strict)
BuildRequires:	perl(Type::Tiny)
BuildRequires:	perl(Types::Standard)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(warnings)
# Test suite
BuildRequires:	perl(base)
BuildRequires:	perl(File::Spec)
%if %{with network_tests}
BuildRequires:	perl(lib)
BuildRequires:	perl(LWP::Protocol::https)
%endif
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Needs) >= 0.002005
# Optional tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
# Dependencies
Requires:	perl(HTTP::Tiny) >= 0.056
Requires:	perl(IO::Socket::SSL) >= 1.42
Requires:	perl(Net::SSLeay) >= 1.49

# Filter under-specified dependency
%global __requires_exclude ^perl\\(HTTP::Tiny\\)$

%description
This is a hopefully-complete API-compliant interface to MetaCPAN
(https://metacpan.org/) with DWIM capabilities, to make your life easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MetaCPAN-Client-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%if !%{with network_tests}
mv t/api/[a-z]*.t t/result_custom.t t/scroll.t ./
%endif

make test

%if !%{with network_tests}
mv ./result_custom.t ./scroll.t t/
mv ./[a-z]*.t t/api/
%endif

%files
%license LICENSE
%doc Changes examples/ README
%{perl_vendorlib}/MetaCPAN/
%{_mandir}/man3/MetaCPAN::Client.3*
%{_mandir}/man3/MetaCPAN::Client::Author.3*
%{_mandir}/man3/MetaCPAN::Client::Cover.3*
%{_mandir}/man3/MetaCPAN::Client::CVE.3*
%{_mandir}/man3/MetaCPAN::Client::Distribution.3*
%{_mandir}/man3/MetaCPAN::Client::DownloadURL.3*
%{_mandir}/man3/MetaCPAN::Client::Favorite.3*
%{_mandir}/man3/MetaCPAN::Client::File.3*
%{_mandir}/man3/MetaCPAN::Client::Mirror.3*
%{_mandir}/man3/MetaCPAN::Client::Module.3*
%{_mandir}/man3/MetaCPAN::Client::Package.3*
%{_mandir}/man3/MetaCPAN::Client::Permission.3*
%{_mandir}/man3/MetaCPAN::Client::Pod.3*
%{_mandir}/man3/MetaCPAN::Client::Rating.3*
%{_mandir}/man3/MetaCPAN::Client::Release.3*
%{_mandir}/man3/MetaCPAN::Client::Request.3*
%{_mandir}/man3/MetaCPAN::Client::ResultSet.3*
%{_mandir}/man3/MetaCPAN::Client::Role::Entity.3*
%{_mandir}/man3/MetaCPAN::Client::Role::HasUA.3*
%{_mandir}/man3/MetaCPAN::Client::Scroll.3*
%{_mandir}/man3/MetaCPAN::Client::Types.3*

%changelog
%autochangelog
