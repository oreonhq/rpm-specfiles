%global source0_hash 3261e13248128f1ad023a6370f903dd4e09814d16abd441f807f94c0f2b385f9

Name:           perl-DBICx-Sugar
Version:        0.0200
Release:        26%{?dist}
Summary:        Just some syntax sugar for DBIx::Class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/DBICx-Sugar
Source0:        https://cpan.metacpan.org/authors/id/I/IR/IRONCAMEL/DBICx-Sugar-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Class::Schema::Loader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::LoadableClass)
BuildRequires:  perl(Test::Modern)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Just some syntax sugar for your DBIx::Class applications. This was
originally created to remove code duplication between Dancer::Plugin::DBIC
and Dancer2::Plugin::DBIC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBICx-Sugar-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%license LICENSE
%{perl_vendorlib}/DBICx*
%{_mandir}/man3/DBICx*

%changelog
%autochangelog
