# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7b1048335f327958903867cea079dc072ea07f4eafae1b40c2e6f25db21686c0

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-Expect
Version:        1.38
Release:        1%{?dist}
Summary:        Expect for Perl expect-like automation
License:        Artistic-1.0-Perl OR GPL-1.0-or-later
URL:            https://metacpan.org/release/Expect
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JACOBY/Expect-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Tty) >= 1.11
BuildRequires:  perl(IO::Pty) >= 1.11
BuildRequires:  perl(Test::More)
BuildRequires:  perl(File::Temp)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(IO::Tty) >= 1.11
Requires:       perl(IO::Pty) >= 1.11

Provides:       perl(Expect) = %{version}

%description
Expect.pm is a Perl implementation of the popular Tcl Expect tool for
automating interactive applications.

%prep
%oreon_sha256
%autosetup -n Expect-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Expect.pm
%{_mandir}/man3/Expect.3*

%changelog
%autochangelog
