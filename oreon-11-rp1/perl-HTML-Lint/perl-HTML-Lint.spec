%global source0_hash 798dc4b64d46aedb2acf233b09e48fb1c24f25274adfdd888ce7b1ee6e176052

Name:           perl-HTML-Lint
Version:        2.32
Release:        22%{?dist}
Summary:        HTML::Lint Perl module
License:        Artistic-2.0
URL:            https://metacpan.org/release/HTML-Lint
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/HTML-Lint-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser) >= 3.47
BuildRequires:  perl(HTML::Tagset) >= 3.03
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
# Optional
BuildRequires:  perl(LWP::Simple)

# For improved testing
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14

# Convenience to users looking for weblint
Provides:       weblint = %{version}-%{release}

%description
HTML::Lint Perl module, a pure-Perl HTML parser and checker for syntactic
legitmacy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Lint-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{_bindir}/weblint
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
