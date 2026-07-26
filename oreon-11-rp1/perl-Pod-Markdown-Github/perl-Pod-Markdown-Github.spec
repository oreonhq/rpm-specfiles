%global source0_hash b37e2f009c4cce4924fb23ee43146e506722971bea6bced2dac15d080a3bc613

Name:           perl-Pod-Markdown-Github
Version:        0.04
Release:        22%{?dist}
Summary:        Convert POD to Github's specific markdown
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Markdown-Github
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MINIMAL/Pod-Markdown-Github-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(Pod::Usage)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.88

%description
Github flavored markdown allows for syntax highlighting using three
backticks. This Perl module inherits from Pod::Markdown and adds those
backticks and an optional language identifier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Markdown-Github-%{version}

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
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
