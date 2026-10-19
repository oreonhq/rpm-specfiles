%global source0_hash 2e39be4ee015c7ec47c2b067858018a7406e38d5121d655c8a46874adfa9a056
Name:           perl-Lingua-Stem-Snowball-Da
Version:        1.01
Release:        1%{?dist}
Summary:        Porter's stemming algorithm for Danish
License:        GPL-2.0-only
URL:            https://metacpan.org/release/Lingua-Stem-Snowball-Da
Source0:        https://cpan.metacpan.org/authors/id/C/CI/CINE/Lingua-Stem-Snowball-Da-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porter's Danish stemming algorithm, which can be found
at the Snowball website: http://snowball.tartarus.org/.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-Stem-Snowball-Da-%{version}
# for consistency with Snowball-Norwegian and -Swedish
mv stemmer.pl stemmer-da

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
install -D -m 0755 stemmer-da %{buildroot}/%{_bindir}/stemmer-da
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
