%global source0_hash ee836301cbbab9a24b05fc657edfa94b7fd8578d9836e566a191d0a5b01cd7f6

Name:           perl-Memoize-ExpireLRU
Version:        0.56
Release:        27%{?dist}
Summary:        Expiry plug-in for Memoize that adds LRU cache expiration
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Memoize-ExpireLRU
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Memoize-ExpireLRU-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
# Tests only
BuildRequires:  perl(Memoize)
BuildRequires:  perl(vars)

%description
This module implements an expiry policy for Memoize that follows LRU
semantics, that is, the last n results, where n is specified as the
argument to the CACHESIZE parameter, will be cached.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Memoize-ExpireLRU-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
