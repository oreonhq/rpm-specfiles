%global source0_hash 256d3f38764e96333158b14ab18257b92f3155c60d658cafb80389f72f4619ed
Name:           perl-Text-SimpleTable
Summary:        Simple Eyecandy ASCII Tables
Version:        2.07
Release:        1%{?dist}
License:        Artistic-2.0
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRAMBERG/Text-SimpleTable-%{version}.tar.gz
URL:            https://metacpan.org/release/Text-SimpleTable
BuildArch:      noarch
%{?perl_default_subpackage_tests}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Simple eye-candy ASCII tables, as seen in Catalyst.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-SimpleTable-%{version}
sed -i '1s,#!.*perl,#!%{__perl},;s/\r//;' t/* examples/simple.pl

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
