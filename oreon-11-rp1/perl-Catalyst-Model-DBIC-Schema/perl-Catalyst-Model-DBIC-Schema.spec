%global source0_hash 1924f4c00e8f0ff1c5d1afa16efe4f856f1c5e74fe556ec2c5f8f5bf63ad0348
Name:           perl-Catalyst-Model-DBIC-Schema
Summary:        DBIx::Class::Schema Model Class
Version:        0.66
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBJK/Catalyst-Model-DBIC-Schema-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Model-DBIC-Schema
BuildArch:      noarch
Provides:       perl(Catalyst::Model::DBIC::Schema::Types) = %{version}
Requires:       perl(Catalyst::Runtime) >= 5.80005
Requires:       perl(CatalystX::Component::Traits) >= 0.14
Requires:       perl(DBIx::Class) >= 0.08114
Requires:       perl(DBIx::Class::Cursor::Cached)
Requires:       perl(DBIx::Class::Schema::Loader) >= 0.04005
Requires:       perl(Hash::Merge)
Requires:       perl(Moose) >= 1.12
Requires:       perl(MooseX::NonMoose) >= 0.16
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /usr/bin/catalyst.pl
BuildRequires:  make
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Catalyst::Component::InstancePerContext)
BuildRequires:  perl(Catalyst::Devel)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(CatalystX::Component::Traits)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Cursor::Cached)
BuildRequires:  perl(DBIx::Class::Schema::Loader)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::MarkAsMethods)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::LoadableClass)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

TEST_POD=1 C_M_DBIC_SCHEMA_TESTAPP=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
