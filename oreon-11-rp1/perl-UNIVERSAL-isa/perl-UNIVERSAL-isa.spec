%global source0_hash d16956036cb01c819dec7d294f6ef891be0bb64876989601354b293164da7f2b
Name:           perl-UNIVERSAL-isa
Version:        1.20171012
Release:        1%{?dist}
Summary:        Hack around module authors using UNIVERSAL::isa as a function
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-isa
Source0:        https://cpan.metacpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-isa-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(UNIVERSAL::isa)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Whenever you use "isa" in UNIVERSAL as a function, a kitten using
Test::MockObject dies. Normally, the kittens would be helpless, but
if they use UNIVERSAL::isa (the module whose docs you are reading),
the kittens can live long and prosper.

This module replaces UNIVERSAL::isa with a version that makes sure
that if it's called as a function on objects which override isa,
isa will be called on those objects as a method.

In all other cases the real UNIVERSAL::isa is just called directly.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n UNIVERSAL-isa-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20171012-25
- Prepare for Oreon 11 (RP1)
