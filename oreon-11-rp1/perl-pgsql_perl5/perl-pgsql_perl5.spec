%global source0_hash 33559b6286bf795f4e89637962073fa43108b93dd04bb6657a051d1a69f0e75d
Name:           perl-pgsql_perl5
Version:        1.9.0
Release:        1%{?dist}
Summary:        Pg – Perl5 extension for PostgreSQL
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/pgsql_perl5
Source0:        https://cpan.metacpan.org/modules/by-module/Pg/pgsql_perl5-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Pg module permits you to access all functions of the Libpq interface of
PostgreSQL. Libpq is the programmer’s interface to PostgreSQL. For examples of
how to use this module, look at the file test.pl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pgsql_perl5-%{version}

# Fix shebangs and permissions on examples and tests
sed -r -i 's|^#!/usr/local/bin/perl\b|#!%{_bindir}/perl|' eg/*.pl test.pl
chmod -v a+x eg/*.pl test.pl

%conf
export POSTGRES_INCLUDE='%{_includedir}'
export POSTGRES_LIB='%{_libdir}'
perl Makefile.PL \
    INSTALLDIRS=vendor \
    NO_PACKLIST=1 \
    NO_PERLLOCAL=1 \
    OPTIMIZE="${RPM_OPT_FLAGS}"

%build

%make_build
%install
make pure_install DESTDIR='%{buildroot}' INSTALL='install -p'
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
