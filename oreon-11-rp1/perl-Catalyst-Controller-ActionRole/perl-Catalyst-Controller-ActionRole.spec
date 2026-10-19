%global source0_hash 21f100392d5ff80d477a391786be28e26ab4ffa0ab3a2f6b74eee3e9803182b0
Name:           perl-Catalyst-Controller-ActionRole
Summary:        Apply roles to action instances
Version:        0.17
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Catalyst-Controller-ActionRole-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Controller-ActionRole
BuildArch:      noarch
Requires:       perl(Catalyst::Controller)
Requires:       perl(Catalyst::Runtime) >= 5.80025
Requires:       perl(Class::MOP) >= 0.80
Requires:       perl(Moose) >= 0.90
%{?perl_default_filter}
%{?perl_default_subpackage_tests}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action)
BuildRequires:  perl(Catalyst::Action::REST)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module allows to apply roles to the Catalyst::Actions for different
controller methods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Controller-ActionRole-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
