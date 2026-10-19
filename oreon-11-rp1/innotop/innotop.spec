%global source0_hash 45645f20e70d54adc5208b5098beb378f5f29fc5e0447237351311418cc9933b
Name:           innotop
Version:        1.16.0
Release:        1%{?dist}
Summary:        A MySQL and InnoDB monitor program
BuildArch:      noarch
License:        GPL-2.0-only or Artistic-1.0-Perl
URL:            https://github.com/innotop/innotop
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?el5}
%endif
Requires:       perl(DBD::mysql)
Requires:       perl(Term::ANSIColor)
Requires:       perl(Term::ReadLine)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
innotop connects to a MySQL database server and retrieves information from it,
then displays it in a manner similar to the UNIX top program.  innotop uses
the data from SHOW VARIABLES, SHOW GLOBAL STATUS, SHOW FULL PROCESSLIST, and
SHOW ENGINE INNODB STATUS, among other things.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
