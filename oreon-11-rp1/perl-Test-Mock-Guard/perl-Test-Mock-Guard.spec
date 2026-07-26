%global source0_hash 7f228a63f8d6ceb92aa784080a13e85073121b2835eca06d794f9709950dbd3d

Name:           perl-Test-Mock-Guard
Version:        0.10
Release:        29%{?dist}
Summary:        Simple mock test library using RAII
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Mock-Guard
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAICRON/Test-Mock-Guard-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(Exporter) >= 5.63
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl-generators
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Exporter) >= 5.63

%description
Test::Mock::Guard is mock test library using RAII. This module is able to
change method behavior by each scope. See SYNOPSIS's sample code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Mock-Guard-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes cpanfile META.json minil.toml README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
