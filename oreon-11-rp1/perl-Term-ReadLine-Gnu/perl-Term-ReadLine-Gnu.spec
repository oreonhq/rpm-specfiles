%global source0_hash 3b07ac8a9b494c50aa87a40dccab3f879b92eb9527ac0f2ded5d4743d166b649

Name:           perl-Term-ReadLine-Gnu
Version:        1.47
Release:        5%{?dist}
Summary:        Perl extension for the GNU Readline/History Library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-ReadLine-Gnu
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-%{version}.tar.gz
Patch1:         0001-Force-TERM-vt100-for-readline-test.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  readline-devel >= 2.1
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# POSIX not used at tests
# Term::ReadLine not used at tests
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  expect
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(locale)
BuildRequires:  perl(open)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(open)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)

%{?perl_default_filter}

%description
An implementation of Term::ReadLine using the GNU Readline/History Library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Term-ReadLine-Gnu-%{version}

%build
# Fix permissions and shebang paths at one shot
find . -type f -exec chmod 0664 '{}' \; \
       -exec sed 's,^#! */usr/local,#!%{_prefix},' -i '{}' \;
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT

%check
# Expect is used so that we get a PTY, as if we were
# in a real terminal, where readline works
expect -c '
	spawn make test
	expect eof
	exit [lindex [wait] 3]
'

%files
%doc README.md
%{_bindir}/perlsh
%{perl_vendorarch}/auto/Term*
%{perl_vendorarch}/Term*
%{_mandir}/man1/perlsh.1*
%{_mandir}/man3/Term*

%changelog
%autochangelog
