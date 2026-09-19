%global source0_hash da2ff30cd81e5c2e2689ce426a0cd72e06ad5b1feacdb107041c8bccc385a156

%global         git b737f60
Summary:        A top clone for MySQL
Name:           mytop
Version:        1.7
Release:        34.%{git}%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://jeremy.zawodny.com/mysql/mytop
# Tarball created by
# $ git clone git://github.com/jzawodn/mytop.git
# $ cd mytop
# $ git archive --format=tar --prefix=mytop-1.7/ %{git} | xz > mytop-1.7-%{git}.tar.xz
Source0:        mytop-%{version}-%{git}.tar.xz
Patch01:        mytop-1.7-long.patch
Patch02:        mytop-1.7-undef-resolv.patch
Requires:       perl(DBD::mysql) >= 1
Requires:       perl(Term::ReadKey) >= 2.1
Requires:       perl(Term::ANSIColor) perl(Time::HiRes)
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(DBD::mysql) >= 1
BuildRequires:  perl(DBI) >= 1.13
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Term::ReadKey) >= 2.1
BuildArch:      noarch

%description 
mytop is a console-based tool for monitoring the threads and overall
performance of MySQL servers. The user interface is modeled after
familiar top application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{__perl} Makefile.PL
make

%install
install -D -m 0644 blib/man1/mytop.1 %{buildroot}%{_mandir}/man1/mytop.1
install -D -m 0755 mytop %{buildroot}%{_bindir}/mytop

%check
make test

%files
%doc Changes README
%{_bindir}/mytop
%{_mandir}/man1/mytop.1*

%changelog
%autochangelog
