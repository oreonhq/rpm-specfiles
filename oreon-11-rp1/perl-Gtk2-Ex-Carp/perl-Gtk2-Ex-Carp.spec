%global source0_hash ebbbf10ef13b81aedfc4f244e53f0e1d5a164080a9b9e3c66cc99b1afdb4d5f6

Name:           perl-Gtk2-Ex-Carp
Version:        0.01
Release:        54%{?dist}
Summary:        GTK+ friendly die() and warn() functions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gtk2-Ex-Carp
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBROWN/Gtk2-Ex-Carp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::Dialog)
BuildRequires:  perl(Gtk2::Pango)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
# Locale::gettext
# Tests:
BuildRequires:  font(:lang=en)
BuildRequires:  perl(Test)
BuildRequires:  xorg-x11-server-Xvfb
Requires:       perl(warnings)

%description
This module exports four functions, of which two override the standard
die() and warn() functions, and two which allow for extended error
reporting. When called, these functions display a user-friendly message
dialog window.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Ex-Carp-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
xvfb-run -a make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
