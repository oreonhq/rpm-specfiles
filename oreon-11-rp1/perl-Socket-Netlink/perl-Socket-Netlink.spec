%global source0_hash d847db59b148d08d40fe09dda2cc257ef72fb1eb5a0d68155fbedcb1f585d8bd

Name:           perl-Socket-Netlink
Version:        0.05
Release:        33%{?dist}
Summary:        Interface to Linux's PF_NETLINK socket family
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Socket-Netlink
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Socket-Netlink-%{version}.tar.gz

BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(ExtUtils::H2PM) >= 0.07
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(overload)
BuildRequires:  perl(Socket)
BuildRequires:  perl(XSLoader)
# Optional run-time:
BuildRequires:  perl(Sub::Name)
# Tests:
BuildRequires:  perl(Test::HexString)
BuildRequires:  perl(Test::More)
# Optional run-time:
Requires:       perl(Sub::Name)

## Filter unneeded Provides with RPM 4.8
%{?filter_setup:
%filter_from_provides /^perl(Socket::Netlink::Generic)$/d
}
%{?perl_default_filter}
## Filter unneeded Provides with RPM 4.9
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(Socket::Netlink::Generic\\)$

# For some reason rpmbuild picks this one up as a 'Requires', but not as
# a 'Provides'. Adding it manually or the package fails to install
Provides:       perl(Socket::Netlink::Generic_const) == %{version}

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

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Socket*
%{perl_vendorarch}/IO*
%{_mandir}/man3/*

%changelog
%autochangelog
