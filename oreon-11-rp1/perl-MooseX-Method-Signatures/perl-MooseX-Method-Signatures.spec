%global source0_hash 3a3c12bcb1d1b2e6d4bc3fbba06e242255fddab87c12c0d540366a3905193a12
Name:           perl-MooseX-Method-Signatures
Version:        0.49
Release:        1%{?dist}
Summary:        Method declarations with type constraints and no source filter
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Method-Signatures
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Method-Signatures-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose::Meta::Method)
Requires:       perl(MooseX::Types) >= 0.35
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(Context::Preserve)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Declare)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::LazyRequire)
BuildRequires:  perl(MooseX::Meta::TypeConstraint::ForceCoercion)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(MooseX::Types::Util)
BuildRequires:  perl(Parse::Method::Signatures)
BuildRequires:  perl(Parse::Method::Signatures::Param::Named)
BuildRequires:  perl(Parse::Method::Signatures::Param::Placeholder)
BuildRequires:  perl(Parse::Method::Signatures::TypeConstraint)
BuildRequires:  perl(Parse::Method::Signatures::Types)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(aliased)
BuildRequires:  perl(metaclass)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl-generators
# /oreon:deps
%description
Provides a proper method keyword, like "sub" but specifically for making
methods and validating their arguments against Moose type constraints.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Method-Signatures-%{version}

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
