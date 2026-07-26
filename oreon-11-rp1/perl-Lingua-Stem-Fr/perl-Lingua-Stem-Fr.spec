%global source0_hash 9d4f64b3a8898a185343218526d5ac68a4a1f8e6c4418d6ba95d62f5f9d5d96f

Name:           perl-Lingua-Stem-Fr
Version:        0.02
Release:        44%{?dist}
Summary:        Perl French Stemming
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-Stem-Fr
Source0:        https://cpan.metacpan.org/authors/id/S/SD/SDP/Lingua-Stem-Fr-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
# -

%description
This module use the a modified version of the Porter Stemming Algorithm to
return a stemmed words.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-Stem-Fr-%{version}
iconv -f iso-8859-1 -t utf-8 README >README.iconv
touch -r README README.iconv
mv -f README.iconv README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
