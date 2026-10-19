%global source0_hash f4f56508e4a9fd8f9488aea6be8e7e7180774e820aa982b1afb7a2dd33c4ba61
Name:           perl-Apache-Reload
Version:        0.14
Release:        7%{?dist}
Summary:        Reload changed Perl modules
License:        Apache-2.0
URL:            https://metacpan.org/release/Apache-Reload
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/Apache-Reload-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(ModPerl::Util) >= 1.99022
Conflicts:      mod_perl < 2.0.10-4
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ModPerl::Util\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Apache2::Connection)
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::ServerUtil)
BuildRequires:  perl(Apache::Test)
BuildRequires:  perl(Apache::TestMM)
BuildRequires:  perl(Apache::TestRequest)
BuildRequires:  perl(Apache::TestRunPerl)
BuildRequires:  perl(Apache::TestUtil)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(ModPerl::MM)
BuildRequires:  perl(ModPerl::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(mod_perl2)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This mod_perl extension allows to reload Perl modules that changed on the disk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-Reload-%{version}

%build

unset MOD_PERL_2_BUILD
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 MOD_PERL=2
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
