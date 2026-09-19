%global source0_hash 7c579f2595285e64c3dcb5540334aa9a002443e1d4c8c83ab4493b90cc51b244

%global pkgname Catalyst-Authentication-Store-DBIx-Class

Name:           perl-Catalyst-Authentication-Store-DBIx-Class
Version:        0.1506
Release:        31%{?dist}
Summary:        A storage class for Catalyst Authentication using DBIx::Class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Authentication-Store-DBIx-Class
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/%{pkgname}-%{version}.tar.gz
Patch0:         Catalyst-Authentication-Store-DBIx-Class-0.1506-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(DBIx::Class)
# required for tests
BuildRequires:  perl(Catalyst::Plugin::Authorization::Roles)
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(Try::Tiny)

%description
The Catalyst::Authentication::Store::DBIx::Class class provides access
to authentication information stored in a database via DBIx::Class.

%{?perl_default_filter}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version} 
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
