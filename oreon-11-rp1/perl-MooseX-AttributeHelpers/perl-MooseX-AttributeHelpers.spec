%global source0_hash b0c819ec83999b258b248f82059fa5975a0cee365423abbee0efaca5401c5ec6

Name:           perl-MooseX-AttributeHelpers
Version:        0.25
Release:        30%{?dist}
Summary:        Extended Moose attribute interfaces (deprecated)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-AttributeHelpers
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-AttributeHelpers-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Module
BuildRequires:  perl(Moose) >= 0.56
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
# Test Suite
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Exception) >= 0.21
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.94
# Dependencies
Requires:       perl(Moose) >= 0.56

Provides:       perl(MooseX::AttributeHelpers)
%description
This distribution is deprecated. The features it provides have been added to
the Moose core code as Moose::Meta::Attribute::Native. This distribution should
not be used by any new code.

While Moose attributes provide you with a way to name your accessors,
readers, writers, clearers and predicates, this library provides commonly
used attribute helper methods for more specific types of data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-AttributeHelpers-%{version}

%build
perl Build.PL --installdirs=vendor
./Build
sed -i '1s,#!perl,#!%{__perl},' t/*.t

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README t/
%license LICENSE
%{perl_vendorlib}/MooseX/
%{_mandir}/man3/MooseX::AttributeHelpers.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Bool.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Collection::Array.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Collection::Bag.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Collection::Hash.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Collection::ImmutableHash.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Collection::List.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Counter.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Meta::Method::Curried.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Meta::Method::Provided.3*
%{_mandir}/man3/MooseX::AttributeHelpers::MethodProvider::Array.3*
%{_mandir}/man3/MooseX::AttributeHelpers::MethodProvider::Bag.3*
%{_mandir}/man3/MooseX::AttributeHelpers::MethodProvider::Bool.3*
%{_mandir}/man3/MooseX::AttributeHelpers::MethodProvider::Counter.3*
%{_mandir}/man3/MooseX::AttributeHelpers::MethodProvider::Hash.3*
%{_mandir}/man3/MooseX::AttributeHelpers::MethodProvider::ImmutableHash.3*
%{_mandir}/man3/MooseX::AttributeHelpers::MethodProvider::List.3*
%{_mandir}/man3/MooseX::AttributeHelpers::MethodProvider::String.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Number.3*
%{_mandir}/man3/MooseX::AttributeHelpers::String.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Base.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Collection.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Collection::Bag.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Collection::Hash.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Collection::ImmutableHash.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Collection::List.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Counter.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::String.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Bool.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Collection::Array.3*
%{_mandir}/man3/MooseX::AttributeHelpers::Trait::Number.3*

%changelog
%autochangelog
