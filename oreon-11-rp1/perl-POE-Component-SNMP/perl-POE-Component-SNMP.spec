%global source0_hash d1586a581d82096de6e522d7aee5dc24f570f55293a3eeb79c232dc5e6ff10df

Name:           perl-POE-Component-SNMP
Version:        1.1006
Release:        43%{?dist}
Summary:        POE interface to Net::SNMP 
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-SNMP
Source0:        https://cpan.metacpan.org/authors/id/R/RD/RDB/POE-Component-SNMP-%{version}.tar.gz        
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Net::SNMP)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Kernel)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
Requires:  perl(Net::SNMP)

%description
POE::Component::SNMP is a POE-ized wrapper around the the Net::SNMP module.
Most of its arguments aren't even evaluated by POE, except for -alias and 
-callback_args, as described in the manpage.

If you want to make non-blocking calls with Net::SNMP in a POE application,
this is the module to do it with.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-SNMP-%{version}
chmod -x eg/*

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes NOTES README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
