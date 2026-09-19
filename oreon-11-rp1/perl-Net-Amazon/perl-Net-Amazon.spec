%global source0_hash e26ade6842f070e307eb2bf13040a75050fac69af8f7eca322f75a64b4455c06

Name:           perl-Net-Amazon
Version:        0.62
Release:        36%{?dist}
Summary:        Framework for accessing amazon.com via REST
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Amazon
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOUMENOT/Net-Amazon-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Log::Log4perl) >= 0.3
BuildRequires:  perl(LWP::UserAgent) >= 5.814
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Simple) >= 2.08
# Tests
BuildRequires:  perl(Cache::MemoryCache)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Log::Log4perl::Level)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
Net::Amazon provides an object-oriented interface to amazon.com's REST
interface. This way it's possible to create applications using Amazon's vast
amount of data via a functional interface, without having to worry about the
underlying communication mechanism.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Amazon-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
