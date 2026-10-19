%global source0_hash c7b5d1bef59ef9087ff67eb3168d2624be94ae5464469e259ad11bfb8ad8cdcd
Name:           perl-B-Hooks-OP-Check
Summary:        Wrap OP check callbacks
Version:        0.22
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Hooks-OP-Check
Source0:        https://cpan.metacpan.org/modules/by-module/B/B-Hooks-OP-Check-%{version}.tar.gz
%{?perl_default_filter}
Provides:       perl(B::Hooks::OP::Check)
Provides:       perl(B::Hooks::OP::Check)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a C API for XS modules to hook into the callbacks
of 'PL_check'.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n B-Hooks-OP-Check-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
