%global source0_hash 7b1048335f327958903867cea079dc072ea07f4eafae1b40c2e6f25db21686c0

Name:		perl-Expect
Version:	1.38
Release:	5%{?dist}
Summary:	Expect for Perl
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Expect
Source0:        https://cpan.metacpan.org/modules/by-module/Expect/Expect-%{version}.tar.gz



BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Pty) >= 1.11
BuildRequires:	perl(IO::Tty) >= 1.11
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More) >= 0.98
# Dependencies
# (none)

%description
This module provides Expect-like functionality to Perl. Expect is
a tool for automating interactive applications such as telnet, ftp,
passwd, fsck, rlogin, tip, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Expect-%{version}
sed -i 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' examples/kibitz/kibitz tutorial/[2-6].*
chmod -c a-x Changes examples/*.pl examples/kibitz/* lib/Expect.pm LICENSE README.md tutorial/*

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README.md examples/ tutorial/
%{perl_vendorlib}/Expect.pm
%{_mandir}/man3/Expect.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.38-5
- Prepare for Oreon 11 (RP1)
