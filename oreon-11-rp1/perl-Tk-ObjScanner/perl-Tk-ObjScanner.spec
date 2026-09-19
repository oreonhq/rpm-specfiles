%global source0_hash 1492e1491aaf1aa9c299bf39b6ac22574f0c212c9bc2553fbdbb3d230ad1ad75

Name:           perl-Tk-ObjScanner
Version:        2.018
Release:        7%{?dist}
Summary:        Tk data scanner
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Tk-ObjScanner
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Tk-ObjScanner-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# runtime requirements
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Adjuster)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Frame)
BuildRequires:  perl(Tk::HList)
BuildRequires:  perl(Tk::Menubutton)
BuildRequires:  perl(Tk::ROText)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(vars)

%{?perl_default_filter}

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

%check
# Tk-ObjScanner's tests are X-based.
# %%{make_build} test

%files
%doc Changes
%license LICENSE
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
