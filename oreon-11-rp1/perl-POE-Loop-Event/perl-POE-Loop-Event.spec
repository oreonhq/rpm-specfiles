%global source0_hash 94f20744a44726eda3f04b30f22807e0a14adb083628656a25d5458871b51f34

Name:           perl-POE-Loop-Event
Version:        1.305
Release:        30%{?dist}
Summary:        Bridge that allows POE to be driven by Event.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Loop-Event

Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Loop-Event-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE::Test::Loops) >= 1.352
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Event) >= 1.21
BuildRequires:  perl(POE) >= 1.356
BuildRequires:  perl(POE::Loop::PerlSignals)
BuildRequires:  perl(vars)

# Testing
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket::GetAddrInfo)
BuildRequires:  perl(Term::Size)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)

Requires:       perl(Event) >= 1.21
Requires:       perl(POE) >= 1.356

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl\\(Event\\)
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}perl\\(POE::Kernel\\)

%description
POE::Loop::Event implements the interface documented in POE::Loop.
Therefore it has no documentation of its own. Please see POE::Loop for
more details.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Loop-Event-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor --default
# skip network tests
touch run_network_tests

make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
