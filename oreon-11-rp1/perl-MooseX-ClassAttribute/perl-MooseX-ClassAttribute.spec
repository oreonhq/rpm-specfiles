%global source0_hash 6144c77c52770d4f831cadb6cada37125c80b3e4ffcb246da7ee9d55922ee725

Name:           perl-MooseX-ClassAttribute
Summary:        Declare class attributes Moose-style
Version:        0.29
Release:        28%{?dist}
License:        Artistic-2.0
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-ClassAttribute-%{version}.tar.gz 
URL:            https://metacpan.org/release/MooseX-ClassAttribute
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Moose) >= 2.00
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean) >= 0.11
BuildRequires:  perl(namespace::clean) >= 0.20
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires) >= 0.05

%{?perl_default_filter}

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

%check
make test

%files
%doc Changes t/
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
