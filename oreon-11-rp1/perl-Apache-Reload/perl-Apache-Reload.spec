%global source0_hash f4f56508e4a9fd8f9488aea6be8e7e7180774e820aa982b1afb7a2dd33c4ba61

Name:           perl-Apache-Reload
Version:        0.14
Release:        7%{?dist}
Summary:        Reload changed Perl modules
License:        Apache-2.0
URL:            https://metacpan.org/release/Apache-Reload
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/Apache-Reload-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# Apache::Reload from ./lib is loaded
BuildRequires:  perl(Config)
# ExtUtils::MakeMaker not used because we build for mod_perl-2 only
# File::Spec not used because we build for mod_perl-2 only
BuildRequires:  perl(lib)
# mod_perl not used
BuildRequires:  perl(mod_perl2) >= 1.99022
BuildRequires:  perl(ModPerl::MM)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time:
BuildRequires:  perl(Apache2::Connection)
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::ServerUtil)
BuildRequires:  perl(ModPerl::Util)
BuildRequires:  perl(warnings)
# Tests:
# All tests will be skipped if Apache::Test 1.34, etc. or Test::More is not
# availabe.
# Apache::Constants not used
BuildRequires:  perl(Apache::Test) >= 1.34
BuildRequires:  perl(Apache::TestMM)
BuildRequires:  perl(Apache::TestRunPerl)
BuildRequires:  perl(Apache::TestRequest)
BuildRequires:  perl(Apache::TestUtil)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
# The mod_perl2 1.99022 is not used, pick for example ModPerl::Util to
# constrain the version.
Requires:       perl(ModPerl::Util) >= 1.99022
Conflicts:      mod_perl < 2.0.10-4

# Fiter-underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ModPerl::Util\\)$

%description
This mod_perl extension allows to reload Perl modules that changed on the disk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-Reload-%{version}

%build
# MOD_PERL_2_BUILD=1 requires MP_APXS variable set to the apxs executable.
# Use MOD_PERL=2 argument instead.
unset MOD_PERL_2_BUILD
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 MOD_PERL=2
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
# RELEASE is not for users
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
