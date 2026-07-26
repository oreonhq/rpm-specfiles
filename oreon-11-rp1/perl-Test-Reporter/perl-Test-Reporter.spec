%global source0_hash 110064e0560a0f631f9c34444486ab628a0f21d6fa623eb4fbed062219aa163b

Name:           perl-Test-Reporter
Version:        1.62
Release:        32%{?dist}
Summary:        Sends test results to cpan-testers@perl.org
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Reporter
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Reporter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
# Mail::Send is optional
# Net::DNS is optional
# Net::Domain is optional
# Net::SMTP is optional
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
# CPAN::Meta not useful

%description
Test::Reporter reports the test results of any given distribution to the
CPAN Testers project. Test::Reporter has wide support for various perl5's
and platforms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Reporter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
