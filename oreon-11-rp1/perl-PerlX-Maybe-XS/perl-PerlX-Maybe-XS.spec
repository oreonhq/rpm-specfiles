%global source0_hash 48ef97f06949e65277d1a0ac269fbc543b2cb08bd613f020de2098bed6a40bb6

Name:           perl-PerlX-Maybe-XS
Version:        1.001
Release:        27%{?dist}
Summary:        XS backend for PerlX::Maybe
# CONTRIBUTING: CC-By-SA
# LICENSE:      GPL+ or Artistic
# ppport.h:     GPL+ or Artistic
# COPYRIGHT:    Public Domain
# Automatically converted from old format: (GPL+ or Artistic) and CC-BY-SA and Public Domain - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/PerlX-Maybe-XS
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/PerlX-Maybe-XS-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
# ExtUtils::Constant or (File::Copy and File::Spec)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Copy not used
# File::Spec not used
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61

%description
This is a faster implementation of PerlX::Maybe Perl module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PerlX-Maybe-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PerlX*
%{_mandir}/man3/*

%changelog
%autochangelog
