%global source0_hash e26ade6842f070e307eb2bf13040a75050fac69af8f7eca322f75a64b4455c06
Name:           perl-Net-Amazon
Version:        0.62
Release:        36%{?dist}
Summary:        Framework for accessing amazon.com via REST
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Amazon
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOUMENOT/Net-Amazon-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cache::MemoryCache)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Log::Log4perl::Level)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
