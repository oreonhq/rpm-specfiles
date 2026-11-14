# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d597af221628571cbecf35b44520148c44798dfc8a9867774e60453f79d25ff7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-IO-Tty
Version:        1.31
Release:        1%{?dist}
Summary:        Perl interface to pseudo ttys
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Tty
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Tty-%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Provides:       perl(IO::Tty) = %{version}
Provides:       perl(IO::Pty) = %{version}
Provides:       perl(IO::Tty::Constant) = %{version}

%description
IO::Tty and IO::Pty provide an interface to pseudo ttys.

%prep
%oreon_sha256
%autosetup -n IO-Tty-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete

%check
make test

%files
%license LICENSE
%doc README.md ChangeLog
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{_mandir}/man3/IO::Pty.3*
%{_mandir}/man3/IO::Tty.3*
%{_mandir}/man3/IO::Tty::Constant.3*

%changelog
%autochangelog
