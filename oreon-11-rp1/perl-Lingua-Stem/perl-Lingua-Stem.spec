%global source0_hash aa1a9932b6427e598253e61a8ccd0d04cc559fae9d58d8774c2027708b630264

Name:           perl-Lingua-Stem
Version:        2.31
Release:        15%{?dist}
Summary:        Stemming of words
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-Stem
Source0:        https://cpan.metacpan.org/authors/id/S/SN/SNOWHARE/Lingua-Stem-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Lingua::GL::Stemmer)
BuildRequires:  perl(Lingua::PT::Stemmer)
BuildRequires:  perl(Lingua::Stem::Fr) >= 0.02
BuildRequires:  perl(Lingua::Stem::It)
# XXX: BuildRequires:  perl(Lingua::Stem::Ru)
BuildRequires:  perl(Lingua::Stem::Snowball::Da) >= 1.01
BuildRequires:  perl(Lingua::Stem::Snowball::No) >= 1.00
BuildRequires:  perl(Lingua::Stem::Snowball::Se) >= 1.01
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::German)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
# Optional tests only
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Lingua::Stem::Snowball::Da) >= 1.01
Requires:       perl(Lingua::Stem::Snowball::No) >= 1.00
Requires:       perl(Lingua::Stem::Snowball::Se) >= 1.01
Requires:       perl(Lingua::Stem::Fr) >= 0.02
Requires:       perl(Lingua::Stem::It)
Requires:       perl(Lingua::Stem::Ru)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Lingua::Stem::Snowball::Da\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Lingua::Stem::Snowball::No\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Lingua::Stem::Snowball::Se\\)$

%description
This routine applies stemming algorithms to its parameters, returning the
stemmed words as appropriate to the selected locale.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-Stem-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
TEST_POD_COVERAGE=1 ./Build test

%files
# The LICENSE file doesn't contain license texts
%license Artistic_License.txt GPL_License.txt
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
