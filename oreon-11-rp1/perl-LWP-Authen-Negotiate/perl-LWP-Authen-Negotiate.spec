%global source0_hash 50948e19c532b7864e8aaafc6874415ca075b3ea14bc73db58235c475dac4abb

Name:           perl-LWP-Authen-Negotiate
Version:        0.08
Release:        38%{?dist}
Summary:        GSSAPI based Authentication Plugin for LWP
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Authen-Negotiate
Source0:        https://cpan.metacpan.org/modules/by-module/LWP/LWP-Authen-Negotiate-%{version}.tar.gz
# Allow requesting a mutual authentication without a delegation, bug #1685192,
# CPAN RT#128699,
Patch0:         LWP-Authen-Negotiate-0.08-Add-LWP_AUTHEN_NEGOTIATE_MUTUAL-environment-variable.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(GSSAPI) >= 0.18
BuildRequires:  perl(LWP::Debug)
BuildRequires:  perl(Test::More)
Requires:       perl(GSSAPI) >= 0.18
Requires:       perl(LWP::Debug)

%description
WWW-Negotiate supporting Webservers are IIS or Apache with 
mod_auth_kerb for example.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LWP-Authen-Negotiate-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
