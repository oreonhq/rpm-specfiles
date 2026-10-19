%global source0_hash afd50a774cd6a82d31ec78a7cabef39b3163b400565f050d29b4f1dbb83410ad
%bcond_without perl_Inline_Filters_enables_optional_test
Name:           perl-Inline-Filters
Version:        0.20
Release:        1%{?dist}
Summary:        Common source code filters for Inline modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Inline-Filters
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Inline-Filters-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Inline_Filters_enables_optional_test}
%endif
Requires:       perl(Parse::RecDescent)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
