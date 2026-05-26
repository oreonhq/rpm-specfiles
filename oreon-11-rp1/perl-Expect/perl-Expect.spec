# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7b1048335f327958903867cea079dc072ea07f4eafae1b40c2e6f25db21686c0
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:		perl-Expect
Version:	1.38
Release:	5%{?dist}
Summary:	Expect for Perl
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Expect
Source0:	https://cpan.metacpan.org/authors/id/J/JA/JACOBY/Expect-1.38.tar.gz

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
%oreon_verify_sources
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
