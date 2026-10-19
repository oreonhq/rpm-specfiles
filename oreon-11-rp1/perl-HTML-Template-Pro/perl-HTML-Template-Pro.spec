%global source0_hash 1364bf2d2c0449f2c7d7f310f8147dcad3dbd5682d66bbb2fb7caf6adfb7d9ca
Name:           perl-HTML-Template-Pro
Version:        0.9524
Release:        1%{?dist}
Summary:        Perl/XS module to use HTML Templates from CGI scripts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl OR LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/HTML-Template-Pro
Source0:        https://cpan.metacpan.org/authors/id/V/VI/VIY/HTML-Template-Pro-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
