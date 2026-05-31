%global source0_hash a295ea7d1ef241ae2640c1f7864b628f8e6f99ec14fb1da781b2f5f2168dcf09

# Perform optional tests
%bcond_without perl_Text_Template_enables_optional_test

Name:           perl-Text-Template
Version:        1.61
Release:        9%{?dist}
Summary:        Expand template text with embedded Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Template
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Text-Template-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
%if %{with perl_Text_Template_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Safe)
# Not in Fedora
# BuildRequires:  perl(Test::More::UTF8)
BuildRequires:  perl(Test::Warnings)
%endif
Requires:       perl(Carp)

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A 'template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
'fill in' a template, you evaluate the little programs and replace
them with their values.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-Template-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc README
%{perl_vendorlib}/Text/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.61-9
- Prepare for Oreon 11 (RP1)
