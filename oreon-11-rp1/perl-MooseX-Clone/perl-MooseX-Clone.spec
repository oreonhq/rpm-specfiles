%global source0_hash cbd7825db9e74b053f524544a014f066fdce290316ebb568f87679181b398da7
Name:           perl-MooseX-Clone
Version:        0.06
Release:        34%{?dist}
Summary:        Fine grained cloning support for Moose objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Clone
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Clone-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Visitor::Callback)
Requires:       perl(Storable)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Visitor)
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Hash::Util::FieldHash::Compat)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Out of the box Moose only provides very bare-bones cloning support in order
to maximize flexibility.

This role provides a clone method that makes use of the low level cloning
support already in Moose and adds selective deep cloning based on
introspection on top of that. Attributes with the Clone trait will handle
cloning of data within the object, typically delegating to the attribute
value's own clone method.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Clone-%{version}

%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
