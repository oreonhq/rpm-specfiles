%global source0_hash cdebce7e9493f5cd8f77fbb74254f7687763ed839f285cf0546b240d3b2fdc54

Name:           perl-HTML-HTML5-Entities
Version:        0.004
Release:        30%{?dist}
Summary:        Drop-in replacement for HTML::Entities with HTML5 support
# CONTRIBUTING:                 GPL+ or Artistic or (Creative Commons
#                               Attribution ShareAlike 2.0 UK: England & Wales)
# lib/HTML/HTML5/Entities.pm:   GPL+ or Artistic (and copyright only by
#                               various parties)
# Automatically converted from old format: (GPL+ or Artistic) and (GPL+ or Artistic or CC-BY-SA) - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-1.0-or-later OR Artistic-1.0-Perl OR LicenseRef-Callaway-CC-BY-SA)
URL:            https://metacpan.org/release/HTML-HTML5-Entities
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Entities-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
Requires:       perl(Exporter)

%description
This is a drop-in replacement for HTML::Entities Perl module. This replacement
provides the character entities defined in HTML5.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-HTML5-Entities-%{version}

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
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
