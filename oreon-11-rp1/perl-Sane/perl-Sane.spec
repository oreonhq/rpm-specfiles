%global source0_hash e0ef87fe76a3f49a9b54046771e3f79c2dfed1182d9968192459e6ebf334fd48

Name:           perl-Sane
Version:        0.05
Release:        45%{?dist}
Summary:        Perl extension for the SANE (Scanner Access Now Easy) Project
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sane
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Sane-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  pkgconfig(sane-backends) >= 1.0.19
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00

%description
This module allows you to access SANE-compatible scanners in a Perlish and
object-oriented way, freeing you from the casting and memory management in C,
yet remaining very close in spirit to original API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sane-%{version}
# Change mode on files we are going to use for %%doc files so they don't
# generate dependencies
chmod a-x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sane*
%{_mandir}/man3/*

%changelog
%autochangelog
