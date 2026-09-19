%global source0_hash 257c27367634b03e737be024f0d7ba12c279a5801fae347ce8039e9935c32a3e

Name:           perl-Sentry-Raven
Version:        1.14
Release:        15%{?dist}
Summary:        Perl sentry client
License:        MIT
URL:            https://metacpan.org/pod/Sentry::Raven
Source0:        https://cpan.metacpan.org/authors/id/Q/QR/QRRY/Sentry-Raven-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Sys::Hostname)
# Not available
#BuildRequires:  perl(Test::CPAN::Changes::ReallyStrict)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Perl::Critic) >= 1.03
BuildRequires:  perl(Test::Warn) >= 0.30
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI)
BuildRequires:  perl(UUID::Tiny)
Requires:       perl(LWP::Protocol::https)

%description
This module implements the recommended raven interface for posting events
to a sentry service.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sentry-Raven-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
