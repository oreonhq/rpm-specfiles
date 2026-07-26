%global source0_hash 76ee12701df4c177dcf3c4f3e87c62cb1ca87643f025c177230ba0d8cddf1c9b

Name:           perl-CPAN-Releases-Latest
Version:        0.08
Release:        27%{?dist}
Summary:        Find latest release of all distributions on CPAN
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Releases-Latest
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/CPAN-Releases-Latest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(MetaCPAN::Client) >= 2.006000
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
# Time::Duration::Parse not used at tests
# Tests:
# File::Copy not used
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Time::Duration::Parse)

%description
This Perl module constructs a list of all distributions on CPAN, by default
using the MetaCPAN API. The generated index is cached locally. It will let you
iterate over the index, either release by release, or distribution by
distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-Releases-Latest-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
