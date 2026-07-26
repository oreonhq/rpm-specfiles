%global source0_hash 097c4c02bfda4f3042fb2978f6e4ca5991202ef26ceb782bb76430a01812fcbe

Name:           perl-Socket-GetAddrInfo
Version:        0.22
Release:        37%{?dist}
Summary:        RFC 2553's "getaddrinfo" and "getnameinfo" functions

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Socket-GetAddrInfo
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Socket-GetAddrInfo-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)

%{?perl_default_filter}

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

%check
%{?_with_tests:export I_CAN_HAS_INTERNETS=1}

./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Socket*
%{_bindir}/get*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
