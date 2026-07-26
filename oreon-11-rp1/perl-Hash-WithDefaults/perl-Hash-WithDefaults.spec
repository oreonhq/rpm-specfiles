%global source0_hash 6e1df2778355c1a5ca4a9421ecccfd1d109d2e20fbc5f070562a8736ddfaea97

Name:           perl-Hash-WithDefaults
Version:        0.05
Release:        38%{?dist}
Summary:        Class for hashes with key-casing requirements supporting defaults
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-WithDefaults
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JENDA/Hash-WithDefaults-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
# Test
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08

%description
This module implements hashes that support "defaults". That is you may
specify several more hashes in which the data will be looked up in case it
is not found in the current hash.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-WithDefaults-%{version}
sed -i 's/\r//' Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
