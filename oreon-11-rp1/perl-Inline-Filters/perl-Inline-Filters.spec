%global source0_hash afd50a774cd6a82d31ec78a7cabef39b3163b400565f050d29b4f1dbb83410ad

# Run optional test
%bcond_without perl_Inline_Filters_enables_optional_test

Name:           perl-Inline-Filters
Version:        0.20
Release:        29%{?dist}
Summary:        Common source code filters for Inline modules
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Inline-Filters
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Inline-Filters-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
# Tests only
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
# Required indirectly, optional Inline dependency
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
%if %{with perl_Inline_Filters_enables_optional_test}
# Optional tests only
# Class::XSAccessor not used
# List::MoreUtil not used
# Test::Kwalitee not used
BuildRequires:  perl(Test::Pod) >= 1.00
# Text::CSV_XS not used
%endif
Requires:       perl(Parse::RecDescent)

%description
Inline::Filters provide common source code filters to Inline language
modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Inline-Filters-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=true
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
