Name:           perl-IO-Tty
Version:        1.20
Release:        9%{?dist}
Summary:        Perl interface to pseudo tty's
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-2-Clause
URL:            https://metacpan.org/release/IO-Tty
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Tty-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
IO::Tty and IO::Pty provide an interface to pseudo tty's.

%prep
%setup -q -n IO-Tty-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{_mandir}/man3/IO::Pty.3*
%{_mandir}/man3/IO::Tty.3*
%{_mandir}/man3/IO::Tty::Constant.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20-9
- Prepare for Oreon 11 (RP1)
