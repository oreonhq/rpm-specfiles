%global source0_hash 4065c3a83c8dec000f0756b5d8346eeb56af310e7c9bff8dca0bc97bb9cb7b94

Name:           perl-Text-Textile
Version:        2.13
Release:        31%{?dist}
Summary:        A humane web text generator
# <https://github.com/bradchoate/text-textile/issues/15>
# lib/Text/Textile.pm:      GPL+ or Artistic 2.0
# ARTISTIC:                 text of Artistic 1.0
License:        GPL-1.0-or-later OR Artistic-2.0
URL:            https://metacpan.org/release/Text-Textile
Source0:        https://cpan.metacpan.org/authors/id/B/BC/BCHOATE/Text-Textile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(vars)
# Optional run-time:
BuildRequires:  perl(charnames)
# File::Spec not used at tests
BuildRequires:  perl(HTML::Entities)
# Image::Size not used at tests
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
# Optional run-time:
Requires:       perl(charnames)
Requires:       perl(File::Spec)
Requires:       perl(HTML::Entities)
Requires:       perl(Image::Size)

%description
Text::Textile is a Perl-based implementation of Dean Allen's Textile syntax.
Textile is shorthand for doing common formatting tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Textile-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ARTISTIC Changes README.textile
%{_bindir}/textile
%{perl_vendorlib}/*
%{_mandir}/man1/textile.*
%{_mandir}/man3/*

%changelog
%autochangelog
