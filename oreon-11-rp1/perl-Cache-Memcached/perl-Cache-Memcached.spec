%global source0_hash 31b3c51ec0eaaf03002e2cc8e3d7d5cbe61919cfdada61c008eb9853acac42a9

Name:           perl-Cache-Memcached
Version:        1.30
Release:        39%{?dist}
Summary:        Perl client for memcached

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Cache-Memcached
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/Cache-Memcached-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Storable) perl(Time::HiRes) perl(String::CRC32) perl(Test::More)

%{?perl_default_filter}

%description
Cache::Memcached - client library for memcached (memory cache daemon)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cache-Memcached-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

#% check
# This requires a running memcached on the local host, which isn't very
# convenient or suitable. YMMV. BR's are there if we REALLY want this.
#make test

%files
%doc README ChangeLog
%dir %{perl_vendorlib}/Cache/
%dir %{perl_vendorlib}/Cache/Memcached/
%{perl_vendorlib}/Cache/Memcached.pm
%{perl_vendorlib}/Cache/Memcached/GetParser.pm
%{_mandir}/man3/Cache::Memcached.3*

%changelog
%autochangelog
