%global source0_hash 022898e4e331ba20a61eee5bb519eaf5ef3a76fb13cdd30ab4b0378b9d0392fc

Name:           perl-POE-Component-Log4perl
Version:        0.03
Release:        45%{?dist}
Summary:        Logging extension for the POE environment

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl        
URL:            https://metacpan.org/release/POE-Component-Log4perl
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KESTEB/POE-Component-Log4perl-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE), perl(Log::Log4perl)
BuildRequires:  perl(Test::More), perl(Test::Pod)

%description
Log4perl encapsulation within the POE environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Log4perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
