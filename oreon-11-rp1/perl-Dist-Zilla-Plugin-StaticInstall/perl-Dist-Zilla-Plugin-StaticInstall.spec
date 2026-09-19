%global source0_hash e12f06df468beb965fdc4442c1b0496e3f76b88326fbb83f57865956b778572a

# Run optional test
%bcond_without perl_Dist_Zilla_Plugin_StaticInstall_enables_optional_test

Name:           perl-Dist-Zilla-Plugin-StaticInstall
Version:        0.012
Release:        22%{?dist}
Summary:        Identify a distribution as eligible for static installation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-StaticInstall
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-StaticInstall-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autovivification)
# This is a Dist::Zilla plugin
BuildRequires:  perl(Dist::Zilla) >= 4.300039
BuildRequires:  perl(Dist::Zilla::Role::InstallTool)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor) >= 3.00
# Tests:
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
# Test::Warnings not used
%if %{with perl_Dist_Zilla_Plugin_StaticInstall_enables_optional_test}
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Merge not helpful
BuildRequires:  perl(Dist::Zilla) >= 5.022
BuildRequires:  perl(Dist::Zilla::Plugin::ModuleBuildTiny) >= 0.011
# Module::Runtime::Conflicts not helpful
# Moose::Conflicts not helpful
%endif
Requires:       perl(autovivification)
# This is a Dist::Zilla plugin
Requires:       perl(Dist::Zilla) >= 4.300039
Requires:       perl(Dist::Zilla::Role::InstallTool)
Requires:       perl(Dist::Zilla::Role::MetaProvider)

%description
The Dist::Zilla plugin performs a number of checks against the distribution to
determine the proper value of the "x_static_install" metadata field. When set
to a true value, this indicates that it can skip a number of installation
steps (such as running Makefile.PL or Build.PL and acting on its side
effects).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-StaticInstall-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
./Build test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
