%global source0_hash 1dcf8d7f26b37520a010dcd5197014e0a58385ee66b83b4fde07eab50ad9e518

Name:           perl-Snowball-Norwegian
Version:        1.2
Release:        43%{?dist}
Summary:        Porter's stemming algorithm for Norwegian
License:        GPL-2.0-only OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Snowball-Norwegian
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASKSH/Snowball-Norwegian-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(English)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 0.42

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porter's Norwegian stemming algorithm, which can be found at the
Snowball website: http://snowball.tartarus.org/.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Snowball-Norwegian-%{version}
mv bin/stemmer-no.pl bin/stemmer-no

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
%doc Changes README examples
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*

%changelog
%autochangelog
