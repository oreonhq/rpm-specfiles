%global source0_hash a0be800ff4852b1567ee5500e772417ad7a360abff80c01b5b875c15d44be832
%if 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
%bcond_with perl_IO_Socket_SSL_test_unused_idn
%bcond_with perl_IO_Socket_SSL_test_IO_Socket_INET6
%else
%bcond_without perl_IO_Socket_SSL_test_unused_idn
%bcond_without perl_IO_Socket_SSL_test_IO_Socket_INET6
%endif
Name:		perl-IO-Socket-SSL
Version:	2.099
Release:        1%{?dist}
Summary:        Perl library for transparent SSL
License:	(GPL-1.0-or-later OR Artistic-1.0-Perl) AND MPL-2.0
URL:		https://metacpan.org/release/IO-Socket-SSL
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SULLR/IO-Socket-SSL-%{version}.tar.gz
Patch0:		IO-Socket-SSL-2.096-use-system-default-cipher-list.patch
Patch1:		IO-Socket-SSL-2.098-use-system-default-SSL-version.patch
Patch2:		IO-Socket-SSL-2.087-Test-client-performs-Post-Handshake-Authentication.patch
BuildArch:	noarch
%if %{with perl_IO_Socket_SSL_test_IO_Socket_INET6}
%endif
%if %{with perl_IO_Socket_SSL_test_unused_idn}
%endif
Requires:	openssl-libs >= 0.9.8
Requires:	perl(Config)
Requires:	perl(HTTP::Tiny)
Requires:	perl(IO::Socket::INET)
Requires:	perl(IO::Socket::IP) >= 0.31
Requires:	perl(Socket) >= 1.95
Requires:	perl(URI::_idna)
Provides:       perl(IO::Socket::SSL)
Provides:       perl(IO::Socket::SSL::Utils)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-libs
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Net::IDN::Encode)
BuildRequires:  perl(Net::LibIDN)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::_idna)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  procps
# /oreon:deps
%description
This module is a true drop-in replacement for IO::Socket::INET that
uses SSL to encrypt data before it is transferred to a remote server
or client. IO::Socket::SSL supports all the extra features that one
needs to write a full-featured SSL client or server application:
multiple SSL contexts, cipher selection, certificate verification, and
SSL version selection. As an extra bonus, it works perfectly with
mod_perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Socket-SSL-%{version}

# Use system-wide default cipher list to support use of system-wide
# crypto policy (#1076390, #1127577, CPAN RT#97816)
# 
%patch -P 0

# Use system-default SSL version too
%patch -P 1

# Add a test for PHA
%patch -P 2 -p1

%build

NO_NETWORK_TESTING=1 perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
