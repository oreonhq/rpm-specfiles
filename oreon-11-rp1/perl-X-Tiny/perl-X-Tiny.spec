%global source0_hash 6fe1bff536117bd9369753d3b892ed7bf1a2209b59634e9a6198c9c483fb5e4f

Name:           perl-X-Tiny
Version:        0.22
Release:        6%{?dist}
Summary:        Base class for a bare-bones exception factory
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/X-Tiny
Source0:        https://www.cpan.org/authors/id/F/FE/FELIPE/X-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(overload)

# lib/X/Tiny/Base.pm has an override for debugger
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)$

%description
This stripped-down exception framework provides a baseline of functionality
for distributions that want to expose exception hierarchies with minimal
fuss. It's a pattern that I implemented in some other distributions I
created and didn't want to copy/paste around.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n X-Tiny-%{version}
# https://github.com/FGasper/p5-X-Tiny/pull/3
perl -pi -e '$_="" if(/Test::Simple/)' Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md
%license LICENSE
%dir %{perl_vendorlib}/X
%{perl_vendorlib}/X/Tiny*
%{_mandir}/man3/X::Tiny*

%changelog
%autochangelog
