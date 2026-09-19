%global source0_hash aa1b85841cf9fc6fe338366bbc870a4e9304a27641e63f92a1fd96bee8ebf64c

Name:           perl-Text-Brew
Version:        0.02
Release:        33%{?dist}
Summary:        Implementation of the Brew edit distance
# License specified in README
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Text-Brew
Source0:        https://cpan.metacpan.org/authors/id/K/KC/KCIVEY/Text-Brew-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       perl(Carp)

%{?perl_default_filter}

%description
This module implements the Brew edit distance that is very close to the
dynamic programming technique used for the Wagner-Fischer (and so for the
Levenshtein) edit distance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Brew-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Text*
%{_mandir}/man3/Text*

%changelog
%autochangelog
