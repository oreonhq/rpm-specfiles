%global source0_hash 4a85a9a0075160f131b8b90ff4c7e3182aa1e8659d71041aae3f0e8ba5508642

Name:           perl-Config-JFDI
Version:        0.065
Release:        42%{?dist}
Summary:        Just * Do it: A Catalyst::Plugin::ConfigLoader-style layer over Config::Any
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-JFDI
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROKR/Config-JFDI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(Carp::Clan::Share)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Data::Visitor) >= 0.24
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Usaginator)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)

%description
Config::JFDI is an implementation of Catalyst::Plugin::ConfigLoader that
exists outside of Catalyst.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-JFDI-%{version}

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
