%global source0_hash 7d508e2fa7708aa1ba91e00f6a2a7a1af641709fa374335c19ea19519ba6b90d
Name:           perl-MooseX-Role-Strict
Version:        0.05
Release:        1%{?dist}
Summary:        Use strict 'roles' in Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Role-Strict
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/MooseX-Role-Strict-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose::Meta::Role)
Requires:       perl(Moose::Meta::Role::Application::ToClass)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Meta::Role::Application::ToClass)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
When using Moose::Role, a class which provides a method a role provides will
silently override that method. This can cause strange, hard-to-debug errors
when the role's methods are not called. Simply use MooseX::Role::Strict instead
of Moose::Role and overriding a role's method becomes a composition-time
failure.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Role-Strict-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
