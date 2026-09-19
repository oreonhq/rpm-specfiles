%global source0_hash 43cdb652f9638723e3577cb0f8b5468620244c9636e7659811e5b4a801603d57

Name:           perl-MooseX-Types-Structured
Version:        0.36
Release:        27%{?dist}
Summary:        Structured Type Constraints for Moose
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-Types-Structured
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-Structured-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny)
# Run-time
BuildRequires:  perl(Devel::PartialDump) >= 0.13
BuildRequires:  perl(Moose::Meta::TypeCoercion)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Parameterizable)
BuildRequires:  perl(Moose::Util::TypeConstraints) >= 1.06
BuildRequires:  perl(MooseX::Types) >= 0.22
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter) >= 0.982
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Moose) >= 1.08
BuildRequires:  perl(MooseX::Types::DateTime)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Sub::Exporter::ForMethods)
Requires:       perl(Devel::PartialDump) >= 0.13
Requires:       perl(Moose) >= 1.08
Requires:       perl(Moose::Meta::TypeCoercion)
Requires:       perl(Moose::Meta::TypeConstraint)
Requires:       perl(Moose::Meta::TypeConstraint::Parameterizable)
# hidden from PAUSE, but need to be available
Provides:       perl(MooseX::Meta::TypeCoercion::Structured) = %{version}
Provides:       perl(MooseX::Meta::TypeCoercion::Structured::Optional) = %{version}
Provides:       perl(MooseX::Meta::TypeConstraint::Structured) = %{version}
Provides:       perl(MooseX::Meta::TypeConstraint::Structured::Optional) = %{version}
Provides:       perl(MooseX::Types::Structured::MessageStack) = %{version}
Provides:       perl(MooseX::Types::Structured::OverflowHandler) = %{version}

%{?perl_default_filter}
# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::PartialDump\\)
%global __requires_exclude %{__requires_exclude}|^perl\\((Moose|Moose::Util::TypeConstraints)\\)$

%description
A structured type constraint is a standard container Moose type constraint,
such as an ArrayRef or HashRef, which has been enhanced to allow you to
explicitly name all the allowed type constraints inside the structure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-Structured-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
%autochangelog
