%global source0_hash da2ff30cd81e5c2e2689ce426a0cd72e06ad5b1feacdb107041c8bccc385a156
%global         git b737f60
Summary:        A top clone for MySQL
Name:           mytop
Version:        1.7
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            http://jeremy.zawodny.com/mysql/mytop
Source0:        %{name}-%{version}-%{git}.tar.xz
Patch01:        mytop-1.7-long.patch
Patch02:        mytop-1.7-undef-resolv.patch
Requires:       perl(DBD::mysql) >= 1
Requires:       perl(Term::ReadKey) >= 2.1
Requires:       perl(Term::ANSIColor) perl(Time::HiRes)
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl-generators
# /oreon:deps
%description 
mytop is a console-based tool for monitoring the threads and overall
performance of MySQL servers. The user interface is modeled after
familiar top application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{__perl} Makefile.PL
make
%install
install -D -m 0644 blib/man1/mytop.1 %{buildroot}%{_mandir}/man1/mytop.1
install -D -m 0755 mytop %{buildroot}%{_bindir}/mytop
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
