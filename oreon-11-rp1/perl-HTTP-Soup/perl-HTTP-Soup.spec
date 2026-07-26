%global source0_hash f672c4809f4611690c99ad3051e8f35900174a1713a9a652d1323d245ded6b05

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Glib\\)$
Name:           perl-HTTP-Soup
Version:        0.01
Release:        40%{?dist}
Summary:        HTTP client/server library for GNOME
# Automatically converted from old format: LGPLv2 or Artistic 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 OR Artistic-2.0
URL:            https://metacpan.org/release/HTTP-Soup
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POTYL/HTTP-Soup-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libsoup-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib) >= 1.00
BuildRequires:  perl(Glib::CodeGen)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Glib) >= 1.00

%description
This module provides the Perl bindings for the C library libsoup.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Soup-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes COPYING README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/HTTP*
%{_mandir}/man3/*

%changelog
%autochangelog
