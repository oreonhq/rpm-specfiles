%global source0_hash 418a212808f9d0b8bb330ac905096d2dd364976753d4c71534dab9836a63194d

Name:           perl-Unicode-CaseFold
Version:        1.01
Release:        29%{?dist}
Summary:        Unicode case-folding for case-insensitive lookups
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Unicode-CaseFold
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/Unicode-CaseFold-%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

Requires:       perl(XSLoader)

Provides:       perl(Unicode::CaseFoldPP) = %{version}

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Unicode::CaseFold\\)$

%description
This module provides Unicode case-folding for Perl. Case-folding is a tool
that allows a program to make case-insensitive string comparisons or do case-
insensitive lookups.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Unicode-CaseFold-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes eg README TODO
%license LICENSE
%{perl_vendorarch}/auto/Unicode*
%{perl_vendorarch}/Unicode*
%{_mandir}/man3/Unicode*

%changelog
%autochangelog
