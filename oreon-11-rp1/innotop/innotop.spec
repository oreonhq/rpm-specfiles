%global source0_hash cfedf31ba5617a5d53ff0fedc86a8578f805093705a5e96a5571d86f2d8457c0

Name:           innotop
Version:        1.15.2
Release:        %autorelease
Summary:        A MySQL and InnoDB monitor program
BuildArch:      noarch
License:        GPL-2.0-only or Artistic-1.0-Perl
URL:            https://github.com/innotop/innotop
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?el5}
%endif

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(strict)
# Term::ANSIColor not used at tests
BuildRequires:  perl(Term::ReadKey)
# Term::ReadLine not used at tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)

Requires:       perl(DBD::mysql)
Requires:       perl(Term::ANSIColor)
Requires:       perl(Term::ReadLine)

%description
innotop connects to a MySQL database server and retrieves information from it,
then displays it in a manner similar to the UNIX top program.  innotop uses
the data from SHOW VARIABLES, SHOW GLOBAL STATUS, SHOW FULL PROCESSLIST, and
SHOW ENGINE INNODB STATUS, among other things.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
make test

%files
%license COPYING
%doc README.md
%{_bindir}/innotop
%{_mandir}/man1/innotop.1*

%changelog
%autochangelog
