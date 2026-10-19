%global source0_hash 3b07ac8a9b494c50aa87a40dccab3f879b92eb9527ac0f2ded5d4743d166b649
Name:           perl-Term-ReadLine-Gnu
Version:        1.47
Release:        5%{?dist}
Summary:        Perl extension for the GNU Readline/History Library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-ReadLine-Gnu
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-%{version}.tar.gz
Patch1:         0001-Force-TERM-vt100-for-readline-test.patch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  expect
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(locale)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  readline-devel
BuildRequires:  sed
# /oreon:deps
%description
An implementation of Term::ReadLine using the GNU Readline/History Library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Term-ReadLine-Gnu-%{version}
%oreon_prep
%build

find . -type f -exec chmod 0664 '{}' \; \
       -exec sed 's,^#! */usr/local,#!%{_prefix},' -i '{}' \;
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT
%oreon_autofiles main

%check

expect -c '
	spawn make test
	expect eof
	exit [lindex [wait] 3]
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
