%global source0_hash 37f071a2cf4ba8f090a2297c6482b7a2c509eb52dcd6ce5d8035d4ee2c6824b1

Name:		perl-IO-Socket-Socks
Version:	0.74
Release:	25%{?dist}
Summary:	Provides a way to create socks (4 or 5) client or server
# See https://rt.cpan.org/Public/Bug/Display.html?id=44047 for license discussion
License:	LGPL-2.0-or-later
URL:		https://metacpan.org/release/IO-Socket-Socks
Source0:	https://www.cpan.org/modules/by-module/IO/IO-Socket-Socks-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant) >= 1.03
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket::IP) >= 0.36
BuildRequires:	perl(overload)
BuildRequires:	perl(Socket) >= 1.94
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Time::HiRes)
# Dependencies
# IPv6 support requires perl(IO::Socket::IP) ≥ 0.36
Requires:	perl(constant) >= 1.03
Requires:	perl(IO::Socket::IP) >= 0.36
Requires:	perl(Socket) >= 1.94

%description
IO::Socket::Socks connects to a SOCKS proxy and tells it to open a connection
to a remote host/port when the object is created. The object you receive can be
used directly as a socket (with IO::Socket interface) for sending and receiving
data to and from the remote host. In addition to creating a socks client, this
module could be used to create a socks server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Socket-Socks-%{version}

# Don't want executable documentation
chmod -c -x examples/*.pl

# Fix up shellbangs too
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|' examples/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
SOCKS_SLOW_TESTS=1 make test

%files
%doc Changes examples/ README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Socket::Socks.3*

%changelog
%autochangelog
