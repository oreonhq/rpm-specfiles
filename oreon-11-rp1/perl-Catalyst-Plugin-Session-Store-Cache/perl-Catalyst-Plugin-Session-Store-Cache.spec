%global source0_hash d8ac902870fbe0916aba2b4cc9b3aa2f1a12c94ef704003cc9fb1fd6153d4112

Name:           perl-Catalyst-Plugin-Session-Store-Cache
Version:        0.01
Release:        45%{?dist}
Summary:        Store sessions using a Catalyst::Plugin::Cache
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-Store-Cache
Source0:        https://cpan.metacpan.org/authors/id/L/LB/LBR/Catalyst-Plugin-Session-Store-Cache-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.06
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Catalyst::Plugin::Session) >= 0.06

%description
This plugin will store your session data in whatever cache module you have
configured.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-Store-Cache-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
