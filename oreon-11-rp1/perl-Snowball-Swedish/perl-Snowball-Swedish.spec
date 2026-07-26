%global source0_hash efaa923558598f4e888d97a512d60fbcc4481c1f9c5e7ded527596294560fc29

Name:           perl-Snowball-Swedish
Version:        1.2
Release:        44%{?dist}
Summary:        Porter's stemming algorithm for Swedish
License:        GPL-2.0-only OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Snowball-Swedish
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASKSH/Snowball-Swedish-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 0.42

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porter's Swedish stemming algorithm, which can be found at the Snowball
website: http://snowball.tartarus.org/.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Snowball-Swedish-%{version}
mv bin/stemmer-se.pl bin/stemmer-se

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*

%changelog
%autochangelog
