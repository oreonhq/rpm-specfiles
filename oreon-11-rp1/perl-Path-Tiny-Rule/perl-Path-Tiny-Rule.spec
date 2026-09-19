%global source0_hash 4bc84e4f6a76139fdecca06c8eec6943fc643485289eff91f71f9a520ce7e4d9

Name:           perl-Path-Tiny-Rule
Version:        0.02
Release:        18%{?dist}
Summary:        Path::Iterator::Rule subclass that returns Path::Tiny objects
License:        Artistic-2.0
URL:            https://metacpan.org/release/Path-Tiny-Rule
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Path-Tiny-Rule-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Iterator::Rule)
BuildRequires:  perl(Path::Tiny)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(PIR)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Filename) >= 0.03
BuildRequires:  perl(Test::More) >= 0.96

%description
This module is a very thin wrapper around Path::Iterator::Rule that
always returns Path::Tiny objects instead of strings. It should otherwise
be a drop-in replacement for Path::Iterator::Rule, and any deviation from
that is a bug.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Path-Tiny-Rule-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
