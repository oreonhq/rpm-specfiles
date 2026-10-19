%global source0_hash 14349eeca530b1a9e96092787b49167587044bea07938d4ab4a08fb5ab2209c8
Name:           perl-smartmatch
Version:        0.05
Release:        1%{?dist}
Summary:        Pluggable smart matching back-ends
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/smartmatch
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/smartmatch-%{version}-TRIAL.tar.gz
Patch0:         smartmatch-0.05-TRIAL-Fix-building-on-Perl-5.25.1.patch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B::Hooks::OP::Check)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module allows you to override the behavior of the smart match operator
("~~"). "use smartmatch $matcher" hooks into the compiler to replace the
smartmatch opcode with a call to a custom subroutine, specified either as
a coderef or as a string, which will have "smartmatch::engine::" prepended to
it and used as the name of a package in which to find a subroutine named
"match".  The subroutine will be called with two arguments, the values on the
left and right sides of the smart match operator, and should return the
result.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n smartmatch-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
