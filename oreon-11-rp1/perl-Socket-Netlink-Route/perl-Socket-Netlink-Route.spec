%global source0_hash d6b4f5b4befd70387a7a5bfbe13892b0d2c59fccda3e8c1eb02d2ff5b366076d
Name:           perl-Socket-Netlink-Route
Version:        0.05
Release:        1%{?dist}
Summary:        Interface to Linux's NETLINK_ROUTE netlink socket protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Socket-Netlink-Route
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Socket-Netlink-Route-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Socket::Netlink) >= 0.03
%{?filter_setup:
%filter_from_provides /^perl(Socket::Netlink::Route)$/d
}
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(Socket::Netlink::Route\\)$
Provides:       perl(Socket::Netlink::Route_const) == %{version}
# oreon:deps
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(ExtUtils::H2PM)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Socket::Netlink)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
