%global source0_hash d2c7fd5dba5dd010b7d8923516890bb6ccf6b5f188ccb69f35cb0fd6c031d1e8

Name:           perl-Cache-Cache
Version:        1.08
Release:        33%{?dist}
Summary:        Generic cache interface and implementations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Cache-Cache
Source0:        https://cpan.metacpan.org/modules/by-module/Cache/Cache-Cache-%{version}.tar.gz
# Bug #112967 for Cache-Cache: Digest::SHA1 -> Digest::SHA - https://rt.cpan.org/Public/Bug/Display.html?id=112967
Patch0:         Cache-Cache-1.08-Rewrite_from_SHA1_to_SHA.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::ShareLite)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
# (no additional dependencies)
# Dependencies
# (no additional dependencies)

%description
The Cache modules are designed to assist a developer in persisting data for a
specified period of time.  Often these modules are used in web applications to
store data locally to save repeated and redundant expensive calls to remote
machines or databases.  People have also been known to use Cache::Cache for
its straightforward interface in sharing data between runs of an application
or invocations of a CGI-style script or simply as an easy to use abstraction
of the filesystem or shared memory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cache-Cache-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc CHANGES CREDITS DISCLAIMER README STYLE
%{perl_vendorlib}/Cache/
%{_mandir}/man3/Cache::BaseCache.3*
%{_mandir}/man3/Cache::BaseCacheTester.3*
%{_mandir}/man3/Cache::Cache.3*
%{_mandir}/man3/Cache::CacheMetaData.3*
%{_mandir}/man3/Cache::CacheSizer.3*
%{_mandir}/man3/Cache::CacheTester.3*
%{_mandir}/man3/Cache::CacheUtils.3*
%{_mandir}/man3/Cache::FileBackend.3*
%{_mandir}/man3/Cache::FileCache.3*
%{_mandir}/man3/Cache::MemoryBackend.3*
%{_mandir}/man3/Cache::MemoryCache.3*
%{_mandir}/man3/Cache::NullCache.3*
%{_mandir}/man3/Cache::Object.3*
%{_mandir}/man3/Cache::SharedMemoryBackend.3*
%{_mandir}/man3/Cache::SharedMemoryCache.3*
%{_mandir}/man3/Cache::SizeAwareCache.3*
%{_mandir}/man3/Cache::SizeAwareCacheTester.3*
%{_mandir}/man3/Cache::SizeAwareFileCache.3*
%{_mandir}/man3/Cache::SizeAwareMemoryCache.3*
%{_mandir}/man3/Cache::SizeAwareSharedMemoryCache.3*

%changelog
%autochangelog
