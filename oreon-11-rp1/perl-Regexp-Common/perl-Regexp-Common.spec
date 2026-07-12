%global source0_hash 0677afaec8e1300cefe246b4d809e75cdf55e2cc0f77c486d13073b69ab4fbdd

Name:		perl-Regexp-Common
Version:	2024080801
Release:	4%{?dist}
Summary:	Regexp::Common Perl module
# Old Artistic 1.0 is also valid, but we won't list it here since it is non-free.
# Also, it would throw off the automated license check and flag this package.
License:	Artistic-2.0 OR MIT OR BSD-3-Clause
URL:		https://metacpan.org/release/Regexp-Common
Source0:	https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Regexp-Common-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# for improved tests
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Regexp)


Provides:       perl(Regexp::Common)
%description
Regexp::Common - Provide commonly requested regular expressions

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Regexp-Common-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc TODO README
%{perl_vendorlib}/Regexp
%{_mandir}/man3/*

%changelog
%autochangelog
