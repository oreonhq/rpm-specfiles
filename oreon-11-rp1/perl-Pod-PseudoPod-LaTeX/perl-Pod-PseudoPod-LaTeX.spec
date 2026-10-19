%global source0_hash 0631326e05c4d990cce5d06245ed18f033e84448c3b92d48c648fb1117fa8292
Name:           perl-Pod-PseudoPod-LaTeX
Version:        1.20190729
Release:        1%{?dist}
Summary:        Pod::PseudoPod::LaTeX Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-PseudoPod-LaTeX
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-PseudoPod-LaTeX-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Pod::PseudoPod) >= 0.15
Patch0:         Pod-PseudoPod-LaTeX-1.20190729.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Pod::PseudoPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
