%global source0_hash b2ed849d2f4cdd66467512daa3f143266d6df810c5fae9175b252c57bc1536dc

Name:           perl-Package-Variant
Version:        1.003002
Release:        29%{?dist}
Summary:        Parameterizable packages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Package-Variant
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Package-Variant-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Import::Into) >= 1
BuildRequires:  perl(Module::Runtime) >= 0.013
BuildRequires:  perl(strictures) >= 2
# Optional runtime
BuildRequires:  perl(Sub::Name)
# Tests only
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
Recommends:     perl(Sub::Name)

%description
This module allows you to build packages that return different variations
depending on what parameters are given.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Package-Variant-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
