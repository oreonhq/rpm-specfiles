%global source0_hash d7eaa22f35a21b226f2bfd17782cd4226a584a2364659cd7bf8b24fe37f6fe89

Name:           perl-Tie-Cache
Version:        0.21
Release:        33%{?dist}
Summary:        LRU Cache in Memory
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-Cache

Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHAMAS/Tie-Cache-%{version}.tar.gz
%{?el5:BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)}
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Testing
BuildRequires:  perl(Benchmark)

# filter dependencies
%{?perl_default_filter}

%description
This module implements a least recently used (LRU) cache in memory
through a tie interface. Any time data is stored in the tied hash,
that key/value pair has an entry time associated with it, and as
the cache fills up, those members of the cache that are the oldest
are removed to make room for new entries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-Cache-%{version}

%if 0%{?el5}
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(Benchmark)/d' \
    -e '/perl(Tie::Cache)/d' \
    -e '/perl(Tie::Cache::LRU)/d'
EOF

%global __perl_requires %{_builddir}/Tie-Cache-%{version}/%{name}-req
chmod +x %{__perl_requires}
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%if 0%{?el5}
rm -rf %{buildroot}
%endif
make pure_install DESTDIR=%{buildroot}

# drop benchmarking tool here
rm -f %{buildroot}/%{perl_vendorlib}/Tie/tie-cache-bench.pl

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README CHANGES
%doc tie-cache-bench.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
