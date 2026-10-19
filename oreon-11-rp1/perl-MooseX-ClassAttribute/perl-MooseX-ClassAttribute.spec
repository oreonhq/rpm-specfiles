%global source0_hash 6144c77c52770d4f831cadb6cada37125c80b3e4ffcb246da7ee9d55922ee725
Name:           perl-MooseX-ClassAttribute
Summary:        Declare class attributes Moose-style
Version:        0.29
Release:        28%{?dist}
License:        Artistic-2.0
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-ClassAttribute-%{version}.tar.gz
URL:            https://metacpan.org/release/MooseX-ClassAttribute
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module allows you to declare class attributes in exactly the same way as
object attributes, using class_has() instead of has().

You can use any feature of Moose's attribute declarations, including overriding
a parent's attributes, delegation (handles), and attribute metaclasses, and it
should just work. The one exception is the "required" flag, which is not
allowed for class attributes.

The accessor methods for class attribute may be called on the class directly,
or on objects of that class. Passing a class attribute to the constructor will
not set it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-ClassAttribute-%{version}

# silence rpmlint warnings
sed -i '1s,#!.*perl,#!%{__perl},' t/*.t

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
