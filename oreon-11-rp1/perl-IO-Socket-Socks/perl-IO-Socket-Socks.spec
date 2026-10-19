%global source0_hash 37f071a2cf4ba8f090a2297c6482b7a2c509eb52dcd6ce5d8035d4ee2c6824b1
Name:		perl-IO-Socket-Socks
Version:	0.74
Release:        25%{?dist}
Summary:        Provides a way to create socks (4 or 5) client or server
License:	LGPL-2.0-or-later
URL:		https://metacpan.org/release/IO-Socket-Socks
Source0:        https://www.cpan.org/modules/by-module/IO/IO-Socket-Socks-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(constant) >= 1.03
Requires:	perl(IO::Socket::IP) >= 0.36
Requires:	perl(Socket) >= 1.94
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

SOCKS_SLOW_TESTS=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
