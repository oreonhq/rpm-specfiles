%global source0_hash b169e20b02476f308fec0425c75077fd6a851f578b4ea3703e6220659d73b31f

Name:           perl-String-Trim
Version:        0.005
Release:        21%{?dist}
Summary:        Trim white space from your strings
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-Trim
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOHERTY/String-Trim-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter) >= 5.57
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Builder) >= 0.94
BuildRequires:  perl(Test::More) >= 0.94
# Optional tests:
# Test::Script 1.05 not used

%description
String::Trim trims white space off your strings. chomp trims only $/
(typically, that's a new line), but trim will trim all leading and trailing
white space.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Trim-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
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
