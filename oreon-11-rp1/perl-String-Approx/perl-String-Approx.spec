%global source0_hash 43201e762d8699cb0ac2c0764a5454bdc2306c0771014d6c8fba821480631342
Name:           perl-String-Approx
Version:        3.28
Release:        1%{?dist}
Summary:        Perl extension for approximate (fuzzy) matching
License:        (Artistic-2.0 OR LGPL-2.0-only) AND (LGPL-2.0-or-later)
URL:            https://metacpan.org/release/String-Approx
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHI/String-Approx-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
String::Approx lets you match and substitute strings approximately. With
this you can emulate errors: typing errors, speling errors, closely
related vocabularies (colour vs. color), genetic mutations (GAG vs. ACT),
abbreviations (McScot, MacScot).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Approx-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
