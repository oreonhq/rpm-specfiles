%global source0_hash 9c0efa899e7cd575457c6f6894573e7bf0f645d4099e4ab64b6836540f5f403e

Name:           perl-Data-Pond
Version:        0.006
Release:        4%{?dist}
Summary:        Perl-based open notation for data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Data-Pond
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Data-Pond-%{version}.tar.gz

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
Requires:       perl(Exporter)
Requires:       perl(Params::Classify)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
This module is concerned with representing data structures in a textual
notation known as "Pond" (Perl-based open notation for data). The notation
is a strict subset of Perl expression syntax, but is intended to have language-
independent use. It is similar in spirit to JSON, which is based on
JavaScript, but Pond represents fewer data types directly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Pond-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor optimize="%{optimize}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
%autochangelog
