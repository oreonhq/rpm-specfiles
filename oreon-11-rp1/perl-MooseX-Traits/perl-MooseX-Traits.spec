%global source0_hash 74afe0c4faf4e3b97c57f289437caa60becca34cd5821f489dd4cc9da4fbe29a
Name:           perl-MooseX-Traits
Summary:        Automatically apply roles at object creation time
Version:        0.13
Release:        30%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Traits-%{version}.tar.gz
URL:            https://metacpan.org/release/MooseX-Traits
BuildArch:      noarch
Requires:       perl(Class::MOP) >= 0.84
Requires:       perl(Moose)
Requires:       perl(Moose::Role)
Requires:       perl(namespace::autoclean)
Requires:       perl(Sub::Exporter)
%{?perl_default_filter}
%{?perl_default_subpackage_tests}
# oreon:deps
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(ok)
BuildRequires:  perl-generators
# /oreon:deps
%description
MooseX::Traits allows one to arbitrarily add components to an object as
needed, w/o having to explicitly construct new classes: e.g.

    Foo->with_traits('Bar')->new(...);

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Traits-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
