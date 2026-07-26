%global source0_hash db8f4a139e31aed0b40d62a0ff44b1bdc57308d8f5f61f54a4caa4769301e5ac

Name:           perl-Catalyst-Plugin-Session-Store-DBIC
Version:        0.14
Release:        34%{?dist}
Summary:        Store your sessions via DBIx::Class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-Store-DBIC
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-Store-DBIC-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst) >= 5.65000
BuildRequires:  perl(Catalyst::Exception)
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::Delegate) >= 0.05
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class) >= 0.07000
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Warn) >= 0.20
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
Requires:       perl(Catalyst) >= 5.65000
Requires:       perl(DBIx::Class) >= 0.07000

%{?perl_default_filter}

%description
This Catalyst::Plugin::Session storage module saves session data in your
database via DBIx::Class. It's actually just a wrapper around
Catalyst::Plugin::Session::Store::Delegate; if you need complete control
over how your sessions are stored, you probably want to use that instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-Store-DBIC-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
