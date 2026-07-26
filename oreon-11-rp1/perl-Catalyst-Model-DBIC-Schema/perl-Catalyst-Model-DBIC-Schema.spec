%global source0_hash 1924f4c00e8f0ff1c5d1afa16efe4f856f1c5e74fe556ec2c5f8f5bf63ad0348

Name:           perl-Catalyst-Model-DBIC-Schema
Summary:        DBIx::Class::Schema Model Class
Version:        0.66
Release:        8%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBJK/Catalyst-Model-DBIC-Schema-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Model-DBIC-Schema
BuildArch:      noarch

Provides:       perl(Catalyst::Model::DBIC::Schema::Types) = %{version}

BuildRequires: make
BuildRequires:  /usr/bin/catalyst.pl
BuildRequires:  perl-generators
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Catalyst::Component::InstancePerContext)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80005
BuildRequires:  perl(Catalyst::Devel) >= 1.0
BuildRequires:  perl(CatalystX::Component::Traits) >= 0.14
BuildRequires:  perl(CPAN)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class) >= 0.08114
BuildRequires:  perl(DBIx::Class::Cursor::Cached)
BuildRequires:  perl(DBIx::Class::Schema::Loader) >= 0.04005
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose) >= 1.12
BuildRequires:  perl(MooseX::MarkAsMethods) >= 0.13
BuildRequires:  perl(MooseX::NonMoose) >= 0.16
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::LoadableClass)
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)

Requires:       perl(Catalyst::Runtime) >= 5.80005
Requires:       perl(CatalystX::Component::Traits) >= 0.14
Requires:       perl(DBIx::Class) >= 0.08114
Requires:       perl(DBIx::Class::Cursor::Cached)
Requires:       perl(DBIx::Class::Schema::Loader) >= 0.04005
Requires:       perl(Hash::Merge)
Requires:       perl(Moose) >= 1.12
Requires:       perl(MooseX::NonMoose) >= 0.16

%{?perl_default_filter}

%description
This is a Catalyst Model for DBIx::Class::Schema-based Models. See the
documentation for Catalyst::Helper::Model::DBIC::Schema for information on
generating these Models via Helper scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Model-DBIC-Schema-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 C_M_DBIC_SCHEMA_TESTAPP=1 make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
