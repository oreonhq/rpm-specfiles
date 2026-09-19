%global source0_hash 54738e3ce76f8be8b66947092d28973c73d79d1ee19b5d92b057552f8ff09b4f

Name:           perl-Catalyst-Plugin-Session-Store-File
Version:        0.18
Release:        47%{?dist}
Summary:        File storage backend for session data
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-Store-File
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/Catalyst-Plugin-Session-Store-File-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter >= 1:5.8.0
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Cache::Cache) >= 1.02
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Plugin::Session::Store)
BuildRequires:  perl(Catalyst::Plugin::Session::Test::Store)
BuildRequires:  perl(Catalyst::Runtime) >= 5.7000
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Class::Data::Inheritable) >= 0.04
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(inc::Module::Install) >= 0.87
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(Cache::Cache) >= 1.02
Requires:       perl(Catalyst::Plugin::Session)
Requires:       perl(Catalyst::Runtime) >= 5.7000
Requires:       perl(Class::Data::Inheritable) >= 0.04

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess
cache. It is based on Cache::FileCache.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-Store-File-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
