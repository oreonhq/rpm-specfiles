%global source0_hash d6b4f5b4befd70387a7a5bfbe13892b0d2c59fccda3e8c1eb02d2ff5b366076d

Name:           perl-Socket-Netlink-Route
Version:        0.05
Release:        37%{?dist}
Summary:        Interface to Linux's NETLINK_ROUTE netlink socket protocol
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Socket-Netlink-Route
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Socket-Netlink-Route-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(ExtUtils::H2PM) >= 0.07
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Socket::Netlink) >= 0.04
BuildRequires:  perl(Test::More)

Requires:       perl(Socket::Netlink) >= 0.03

## Filter unneeded Provides with RPM 4.8
%{?filter_setup:
%filter_from_provides /^perl(Socket::Netlink::Route)$/d
}
%{?perl_default_filter}
## Filter unneeded Provides with RPM 4.9
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(Socket::Netlink::Route\\)$

# For some reason rpmbuild picks this one up as a 'Requires', but not as
# a 'Provides'. Adding it manually or the package fails to install
Provides:       perl(Socket::Netlink::Route_const) == %{version}

%description
This module contains the low-level constants and structure handling
functions required to use the NETLINK_ROUTE protocol of Linux's PF_NETLINK
socket family. It is suggested to use the high-level object interface to
this protocol instead; see IO::Socket::Netlink::Route.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Socket-Netlink-Route-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes examples LICENSE README
%{perl_vendorlib}/IO
%{perl_vendorlib}/Socket
%{_mandir}/man3/*Socket::Netlink::Route*

%changelog
%autochangelog
