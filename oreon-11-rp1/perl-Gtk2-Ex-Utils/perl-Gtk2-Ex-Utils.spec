%global source0_hash cd508d5cc867cc33e2523d51ddf74b83837ef2c1bd4dc670577a57c48dd561a3
Name:           perl-Gtk2-Ex-Utils
Version:        0.09
Release:        1%{?dist}
Summary:        Extra Gtk2 Utilities for working with GNOME2/GTK2 in Perl
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2-Ex-Utils
Source0:        https://cpan.metacpan.org/authors/id/K/KC/KCK/Gtk2-Ex-Utils-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Gtk2) >= 1.04
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Gtk2\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
