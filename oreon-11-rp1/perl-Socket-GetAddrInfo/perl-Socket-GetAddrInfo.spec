%global source0_hash 097c4c02bfda4f3042fb2978f6e4ca5991202ef26ceb782bb76430a01812fcbe
Name:           perl-Socket-GetAddrInfo
Version:        0.22
Release:        37%{?dist}
Summary:        RFC 2553's "getaddrinfo" and "getnameinfo" functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Socket-GetAddrInfo
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Socket-GetAddrInfo-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The RFC 2553 functions getaddrinfo and getnameinfo provide an abstracted
way to convert between a pair of host name/service name and socket
addresses, or vice versa. getaddrinfo converts names into a set of
arguments to pass to the socket() and connect() syscalls, and getnameinfo
converts a socket address back into its host name/service name pair.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Socket-GetAddrInfo-%{version}

%build

/usr/bin/perl Build.PL installdirs=vendor
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{?_with_tests:export I_CAN_HAS_INTERNETS=1}
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
