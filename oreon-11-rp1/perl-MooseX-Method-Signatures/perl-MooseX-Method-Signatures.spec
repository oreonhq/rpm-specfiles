%global source0_hash 3a3c12bcb1d1b2e6d4bc3fbba06e242255fddab87c12c0d540366a3905193a12

Name:           perl-MooseX-Method-Signatures
Version:        0.49
Release:        30%{?dist}
Summary:        Method declarations with type constraints and no source filter
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Method-Signatures
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Method-Signatures-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(aliased)
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.10
BuildRequires:  perl(Context::Preserve)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Declare) >= 0.005011
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(metaclass)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.89
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::LazyRequire) >= 0.06
BuildRequires:  perl(MooseX::Meta::TypeConstraint::ForceCoercion)
BuildRequires:  perl(MooseX::Types) >= 0.35
BuildRequires:  perl(MooseX::Types::Moose) >= 0.19
BuildRequires:  perl(MooseX::Types::Structured) >= 0.24
BuildRequires:  perl(MooseX::Types::Util)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Parse::Method::Signatures) >= 1.003014
BuildRequires:  perl(Parse::Method::Signatures::Param::Named)
BuildRequires:  perl(Parse::Method::Signatures::Param::Placeholder)
BuildRequires:  perl(Parse::Method::Signatures::TypeConstraint)
BuildRequires:  perl(Parse::Method::Signatures::Types)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Task::Weaken)
# not yet available in Fedora
#BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Balanced)
# not automatically detected
Requires:       perl(Moose::Meta::Method)
Requires:       perl(MooseX::Types) >= 0.35

%{?perl_default_filter}

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

%check
./Build test

%files
%doc Changes README
%license LICENCE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
