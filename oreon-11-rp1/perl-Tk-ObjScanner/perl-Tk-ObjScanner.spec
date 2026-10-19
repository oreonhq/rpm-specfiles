%global source0_hash 1492e1491aaf1aa9c299bf39b6ac22574f0c212c9bc2553fbdbb3d230ad1ad75
Name:           perl-Tk-ObjScanner
Version:        2.018
Release:        1%{?dist}
Summary:        Tk data scanner
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-ObjScanner
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Tk-ObjScanner-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Adjuster)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Frame)
BuildRequires:  perl(Tk::HList)
BuildRequires:  perl(Tk::Menubutton)
BuildRequires:  perl(Tk::ROText)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This perl module provides a GUI to scan the attributes of an object. It can
also be used to scan the elements of a hash or an array.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-ObjScanner-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
