%global source0_hash 3c994a4b63e6e4e836c6f79a93f51921cab77c90c9753fe0f8b5429220d516b9

Name:           perl-Locale-PO
Version:        0.27
Release:        31%{?dist}
Summary:        Perl module for manipulating .po entries from GNU gettext
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-PO
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COSIMO/Locale-PO-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module simplifies management of GNU gettext .po files and is an
alternative to using emacs po-mode. It provides an object-oriented
interface in which each entry in a .po file is a Locale::PO object.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-PO-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
