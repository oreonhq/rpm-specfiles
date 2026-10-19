%global source0_hash d847db59b148d08d40fe09dda2cc257ef72fb1eb5a0d68155fbedcb1f585d8bd
Name:           perl-Socket-Netlink
Version:        0.05
Release:        1%{?dist}
Summary:        Interface to Linux's PF_NETLINK socket family
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Socket-Netlink
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Socket-Netlink-%{version}.tar.gz
Requires:       perl(Sub::Name)
%{?filter_setup:
%filter_from_provides /^perl(Socket::Netlink::Generic)$/d
}
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(Socket::Netlink::Generic\\)$
Provides:       perl(Socket::Netlink::Generic_const) == %{version}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(ExtUtils::H2PM)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::HexString)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module contains the low-level constants and structure handling
functions required to use Linux's PF_NETLINK socket family. It is suggested
to use the high-level object interface to this instead; see
IO::Socket::Netlink.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Socket-Netlink-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
