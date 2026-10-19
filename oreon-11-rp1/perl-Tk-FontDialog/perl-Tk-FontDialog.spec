%global source0_hash 7ddce970642f087c40edeb29128e1c59c92815d3a47761c063e6f1086a6141b4
%global use_x11_tests 1
Name:           perl-Tk-FontDialog
Version:        0.19
Release:        1%{?dist}
Summary:        Font dialog widget for perl/Tk
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-FontDialog
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-FontDialog-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Tk::HList)
Requires:       perl(Tk::ItemStyle)
# oreon:deps
BuildRequires:  font(:lang=en)
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Font)
BuildRequires:  perl(Tk::HList)
BuildRequires:  perl(Tk::ItemStyle)
BuildRequires:  perl(charnames)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
# /oreon:deps
%description
This module implements a font dialog widget for perl/Tk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-FontDialog-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

    xvfb-run -d make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
