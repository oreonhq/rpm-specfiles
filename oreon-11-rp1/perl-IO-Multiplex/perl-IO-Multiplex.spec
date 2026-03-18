Summary:	Manage IO on many file handles
Name:		perl-IO-Multiplex
Version:	1.16
Release:	31%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/IO-Multiplex
Source0:	https://cpan.metacpan.org/modules/by-module/IO/IO-Multiplex-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Socket)
BuildRequires:	perl(strict)
BuildRequires:	perl(Tie::Handle)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(Test)
# Dependencies
Requires:	perl(Time::HiRes)

%description
IO::Multiplex is designed to take the effort out of managing multiple file
handles. It is essentially a really fancy front end to the select system call.
In addition to maintaining the select loop, it buffers all input and output
to/from the file handles. It can also accept incoming connections on one or
more listen sockets.

%prep
%setup -q -n IO-Multiplex-%{version}

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
%doc Changes README TODO
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Multiplex.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-31
- Prepare for Oreon 11 (RP1)
