%global source0_hash 28c768ac2a9ae9d1883386f1cca2130420058b77dd7d4a48337a45513d7d0128

Name:           perl-POE-Component-Client-LDAP
Version:        0.04        
Release:        52%{?dist}
Summary:        Async LDAP access for POE
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-LDAP            
Source0: https://cpan.metacpan.org/authors/id/H/HA/HACHI/POE-Component-Client-LDAP-%{version}.tar.gz        
Patch0:         POE-Component-Client-LDAP-0.04-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::ASN)
BuildRequires:  perl(Net::LDAP::Constant)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Wheel::Null)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  dos2unix

%description
POE::Component::Client::LDAP->new() starts up a new POE::Session and
POE::Wheel to manage socket communications for an underlying Net::LDAP 
object, allowing it to be used in async mode properly within a POE program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Client-LDAP-%{version}
%patch -P0 -p1
# fix line endings...
dos2unix scripts/search.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
chmod -R u+w %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README Todo scripts
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
