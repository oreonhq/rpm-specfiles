%global source0_hash 468915fa3a04dcf6574fc957eff495915e24569434970c91ee8e4e1459fc9114

Name:           perl-Socket6
Version:        0.29
Release:        27%{?dist}
Summary:        IPv6 related part of the C socket.h defines and structure manipulators
License:        BSD-3-Clause
URL:            https://metacpan.org/release/Socket6
Source0:        https://cpan.metacpan.org/modules/by-module/Socket6/Socket6-%{version}.tar.gz



Patch0:         Socket6-0.29-remove_support_of_gethostname2.patch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test)
# Run-time:

# Filter the Perl extension module
%{?perl_default_filter}

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

%check
make test

%files
%doc ChangeLog README gailookup.pl
%{perl_vendorarch}/Socket6.pm
%{perl_vendorarch}/auto/Socket6/
%{_mandir}/man3/Socket6.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.29-27
- Prepare for Oreon 11 (RP1)
