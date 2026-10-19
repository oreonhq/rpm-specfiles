%global source0_hash a295ea7d1ef241ae2640c1f7864b628f8e6f99ec14fb1da781b2f5f2168dcf09
%bcond_without perl_Text_Template_enables_optional_test
Name:           perl-Text-Template
Version:        1.61
Release:        1%{?dist}
Summary:        Expand template text with embedded Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Template
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Text-Template-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Text_Template_enables_optional_test}
%endif
Requires:       perl(Carp)
Provides:       perl(Text::Template)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.61-9
- Prepare for Oreon 11 (RP1)
