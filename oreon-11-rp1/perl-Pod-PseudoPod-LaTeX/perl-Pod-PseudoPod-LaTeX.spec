%global source0_hash 0631326e05c4d990cce5d06245ed18f033e84448c3b92d48c648fb1117fa8292

Name:           perl-Pod-PseudoPod-LaTeX
Version:        1.20190729
Release:        19%{?dist}
Summary:        Pod::PseudoPod::LaTeX Perl module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-PseudoPod-LaTeX
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-PseudoPod-LaTeX-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(IO::String)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::PseudoPod) >= 0.15
BuildRequires:  perl(Test::More) >= 0.60
Requires:       perl(Pod::PseudoPod) >= 0.15

# The patch changes 'Verbatim' to 'verbatim' in:
#   lib/Pod/PseudoPod/LaTeX.pm
#   t/sections.t
#
Patch0:         Pod-PseudoPod-LaTeX-1.20190729.patch

%description
This module is a Pod::PseudoPod subclass, itself a Pod::Simple subclass. This
means that this is a full-fledged POD parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-PseudoPod-LaTeX-%{version}
%patch -P0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT%{_bindir}/ppod2latex

%check
make test

%files
%doc Changes dist.ini LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man1/ppod2latex.1.gz
%{_mandir}/man3/Pod::PseudoPod::LaTeX.3pm.gz
%{_bindir}/ppod2latex

%changelog
%autochangelog
