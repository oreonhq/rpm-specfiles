%global source0_hash 468915fa3a04dcf6574fc957eff495915e24569434970c91ee8e4e1459fc9114
Name:           perl-Socket6
Version:        0.29
Release:        27%{?dist}
Summary:        IPv6 related part of the C socket.h defines and structure manipulators
License:        BSD-3-Clause
URL:            https://metacpan.org/release/Socket6
Source0:        https://cpan.metacpan.org/modules/by-module/Socket6/Socket6-%{version}.tar.gz
Patch0:         Socket6-0.29-remove_support_of_gethostname2.patch
%{?perl_default_filter}
Provides:       perl(Socket6)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module supports getaddrinfo() and getnameinfo() to intend to enable
protocol independent programming. If your environment supports IPv6, IPv6
related defines such as AF_INET6 are included.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Socket6-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.29-27
- Prepare for Oreon 11 (RP1)
