%global source0_hash af83b92185e642695913ff138efe819752e80857759996deafcaab2700ad5db5
Name:           perl-Expect-Simple
Version:        0.04
Release:        1%{?dist}
Summary:        Wrapper around the Expect module
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Expect-Simple
Source0:        https://cpan.metacpan.org/authors/id/D/DJ/DJERIUS/Expect-Simple-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Expect)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Expect::Simple is a wrapper around the Expect module which should
suffice for simple applications. It hides most of the Expect
machinery; the Expect object is available for tweaking if need be.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Expect-Simple-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
