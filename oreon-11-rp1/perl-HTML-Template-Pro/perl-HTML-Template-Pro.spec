%global source0_hash 1364bf2d2c0449f2c7d7f310f8147dcad3dbd5682d66bbb2fb7caf6adfb7d9ca

Name:           perl-HTML-Template-Pro
Version:        0.9524
Release:        16%{?dist}
Summary:        Perl/XS module to use HTML Templates from CGI scripts
# Automatically converted from old format: GPL+ or Artistic or LGPLv2+ - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl OR LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/HTML-Template-Pro
Source0:        https://cpan.metacpan.org/authors/id/V/VI/VIY/HTML-Template-Pro-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
A fast and lightweight C/Perl+XS HTML Template engine implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Template-Pro-%{version}

%build
/usr/bin/perl Makefile.PL PCRE2=1 INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc ARTISTIC Changes FAQ LGPL README README.ru
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/HTML*
%{_mandir}/man3/*

%changelog
%autochangelog
