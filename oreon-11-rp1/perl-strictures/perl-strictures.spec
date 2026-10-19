%global source0_hash 09d57974a6d1b2380c802870fed471108f51170da81458e2751859f2714f8d57
%{bcond_with perl_strictures_enables_optional_test}
Name:           perl-strictures
Version:        2.000006
Release:        1%{?dist}
Summary:        Turn on strict and make most warnings fatal
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/strictures
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/strictures-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_strictures_enables_optional_test}
%endif
Requires:       perl(Carp)
Provides:       perl(strictures)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package turns on strict and makes most warnings fatal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n strictures-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.000006-23
- Prepare for Oreon 11 (RP1)
