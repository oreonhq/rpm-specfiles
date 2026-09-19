%global source0_hash cd508d5cc867cc33e2523d51ddf74b83837ef2c1bd4dc670577a57c48dd561a3

Name:           perl-Gtk2-Ex-Utils
Version:        0.09
Release:        50%{?dist}
Summary:        Extra Gtk2 Utilities for working with GNOME2/GTK2 in Perl
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2-Ex-Utils
Source0:        https://cpan.metacpan.org/authors/id/K/KC/KCK/Gtk2-Ex-Utils-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Gtk2) >= 1.04
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Gtk2) >= 1.04

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Gtk2\\)$

%description
This module provides simple utility functions useful for GNOME2/GTK2 Perl
programming.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Ex-Utils-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes COPYRIGHT README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
