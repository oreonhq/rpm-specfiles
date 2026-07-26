%global source0_hash 0b5a8c2678f79e99694055684f55f134b5fffb7ae5f0016a4e48661403c6de5e

Name:           perl-Text-Table-Tiny
Version:        1.03
Release:        11%{?dist}
Summary:        Makes simple tables from two-dimensional arrays, with limited templating options
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Table-Tiny
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Table-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::TtyLength)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Text::Table::Tiny provides a single function, generate_table, which formats
a two-dimensional array of data as a text table. There are a number of options
for adjusting the output format, but the intention is that the default option
is good enough for most uses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Table-Tiny-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
