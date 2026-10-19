%global source0_hash 8cd514166c66c44ffbe2d0728583032d602b5786ef3a0b7e575f733cc5bd8b08
Name:           perl-Devel-SmallProf
Version:        2.02
Release:        52%{?dist}
Summary:        Per-line Perl profiler
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-SmallProf
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Devel-SmallProf-%{version}.tar.gz
Patch1:         Devel-SmallProf-2.02-Don-t-use-defined-array.patch
Patch2:         Devel-SmallProf-2.02-Remove-DB-sub-declaration.patch
Patch3:         Devel-SmallProf-2.02-Fix-Perl-5.26-support-without-.-in-INC.patch
BuildArch:      noarch
%global __provides_exclude ^perl\\(DB\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Devel::SmallProf profiler is focused on the time taken for a program
run on a line-by-line basis. It is intended to be as "small" in terms of
impact on the speed and memory usage of the profiled program as possible
and also in terms of being simple to use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-SmallProf-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

iconv -f iso8859-1 -t utf-8 README >README.conv && mv -f README.conv README

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
