%global source0_hash 70fc6d5c42cf34e66917743cd348d6d03db5d144d8ded6892363b12327dbec4d
Name:		perl-B-Hooks-Parser
Version:	0.21
Release:        1%{?dist}
Summary:        Interface to perl's parser variables
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/B-Hooks-Parser
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-Parser-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(B::Hooks::OP::Check)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides an API for parts of the perl parser. It can be used to
modify code while it's being parsed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n B-Hooks-Parser-%{version}

# Use American English spelling
cp LICENCE LICENSE

%build

perl Makefile.PL \
  INSTALLDIRS=vendor \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1 \
  OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
