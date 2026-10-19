%global source0_hash 829e4dd3f2895b39f58237770821b76ef0b6aa4d432b3e310dd486eb89614eeb
%{bcond_without perl_MooseX_AttributeShortcuts_enables_optional_test}
Name:           perl-MooseX-AttributeShortcuts
Version:        0.037
Release:        1%{?dist}
Summary:        Shorthand for common Moose attribute options
License:        LicenseRef-Callaway-LGPLv2
URL:            http://metacpan.org/release/MooseX-AttributeShortcuts/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-AttributeShortcuts-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_MooseX_AttributeShortcuts_enables_optional_test}
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Meta::TypeConstraint::Mooish)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::SemiAffordanceAccessor)
BuildRequires:  perl(MooseX::Types::Common::String)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(MooseX::Util)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::Moose::More)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(aliased)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Ever find yourself repeatedly specifying writers and builders, because there's
no good shortcut to specify them? Sometimes you want an attribute to have
a read-only public interface, but a private writer. And wouldn't it be easier
to just say "builder => 1" and have the attribute construct the canonical
"_build_$name" builder name for you?

This package causes an attribute trait to be applied to all attributes defined
to the using class. This trait extends the attribute option processing to
handle the above variations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-AttributeShortcuts-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
