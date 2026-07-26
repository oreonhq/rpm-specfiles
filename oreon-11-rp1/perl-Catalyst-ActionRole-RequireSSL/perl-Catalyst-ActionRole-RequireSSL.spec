%global source0_hash 6db1de9b010dceff5f56e2e35c779a7bcdd2173d5e350261e681e820350dda5b

Name:           perl-Catalyst-ActionRole-RequireSSL
Version:        1.00
Release:        6%{?dist}
Summary:        Catalyst::ActionRole::RequireSSL Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Catalyst-ActionRole-RequireSSL
Source0:        https://cpan.metacpan.org/authors/id/E/EL/ELLIOTT/Catalyst-ActionRole-RequireSSL-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
# test requirements
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Controller::ActionRole)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)

%description
Catalyst::ActionRole::RequireSSL provides a reusable Catalyst
action role to force an action to be secure only.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-ActionRole-RequireSSL-%{version}
/usr/bin/rm -rf inc

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
%autochangelog
