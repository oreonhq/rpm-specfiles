%global source0_hash 2a37e653482efd2c93b86c6a838941e056c5f94dd86c0f0b893d51933312837c
%global pkgname Catalyst-Plugin-Authorization-ACL
Name:           perl-Catalyst-Plugin-Authorization-ACL
Version:        0.16
Release:        1%{?dist}
Summary:        ACL Support for Catalyst Applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Authorization-ACL
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/Catalyst-Plugin-Authorization-ACL-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Catalyst::ClassData)
Requires:       perl(Exporter)
Requires:       perl(Moose::Object)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::ClassData)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Authorization::Roles)
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Class::Throwable)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(Tree::Simple)
BuildRequires:  perl(Tree::Simple::Visitor::FindByPath)
BuildRequires:  perl(Tree::Simple::Visitor::GetAllDescendents)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides Access Control List style path protection, with
arbitrary rules for Catalyst applications. It operates only on the
Catalyst private name space, at least at the moment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version} 

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
