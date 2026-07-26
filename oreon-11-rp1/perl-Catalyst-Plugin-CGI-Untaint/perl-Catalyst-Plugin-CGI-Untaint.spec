%global source0_hash 0cb6cad02a545313b5c206ca124b04d0b09ca2bf077496d3015f0460c222e8a1

Name:           perl-Catalyst-Plugin-CGI-Untaint
Version:        0.05
Release:        50%{?dist}
Summary:        CGI::Untaint Plugin for Catalyst
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-CGI-Untaint
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJC/Catalyst-Plugin-CGI-Untaint-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst)              >= 5.5
BuildRequires:  perl(CGI::Untaint)          >= 1.2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
This module wraps CGI::Untaint up into a Catalyst plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-CGI-Untaint-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
