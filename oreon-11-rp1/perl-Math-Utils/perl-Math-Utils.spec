%global source0_hash 88a20ae0736a622671b92bb2a350969af424d7610284530b277c8020235f2695

Name:           perl-Math-Utils
Version:        1.14
Release:        17%{?dist}
Summary:        Useful mathematical functions not in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Utils
Source0:        https://cpan.metacpan.org/authors/id/J/JG/JGAMBLE/Math-Utils-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
# Tests
BuildRequires:  perl(Math::BigRat)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Test::More)
# Optional tests
# Test::CheckManifest not used
BuildRequires:  perl(Test::Pod) >= 1.22

%description
Math::Utils contains implementations of commonly used mathematical
functions and operations that are not part of standard Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Utils-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
