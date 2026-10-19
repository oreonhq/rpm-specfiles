%global source0_hash aec8571b9e31b7301e26132c132c6800952dc089c645d76954a3ad1a6b350858
Name:           perl-Test-Deep-JSON
Version:        0.05
Release:        1%{?dist}
Summary:        Compare JSON with Test::Deep
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Deep-JSON
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MOTEMEN/Test-Deep-JSON-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Exporter::Lite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::Cmp)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Deep::JSON provides json($expected) function to expect that target
can be parsed as a JSON string and matches (by cmp_deeply) with $expected.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Deep-JSON-%{version}

%build

RELEASE_TESTING=1 %{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
