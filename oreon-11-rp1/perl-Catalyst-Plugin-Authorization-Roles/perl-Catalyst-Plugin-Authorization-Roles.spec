%global source0_hash ee4044e5e2a0d94c4ec512fad55ee0c8de144e1e3b8785207f96025cf9a40351

Name:           perl-Catalyst-Plugin-Authorization-Roles
Version:        0.09
Release:        42%{?dist}
Summary:        Role based authorization for Catalyst based on Catalyst::Plugin::Authentication
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Authorization-Roles
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Authorization-Roles-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-interpreter >= 1:5.8.0
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst::Authentication::User)
BuildRequires:  perl(Catalyst::Authentication::User::Hash)
BuildRequires:  perl(Catalyst::Plugin::Authentication) >= 0.10003
BuildRequires:  perl(Catalyst::Exception)
BuildRequires:  perl(Catalyst::Runtime) >= 5.7
BuildRequires:  perl(inc::Module::Install) >= 0.91
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Object) >= 1.14
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(UNIVERSAL::isa) >= 0.05
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)
Requires:       perl(Catalyst::Plugin::Authentication) >= 0.10003
Requires:       perl(Catalyst::Runtime) >= 5.7
Requires:       perl(Set::Object) >= 1.14
Requires:       perl(UNIVERSAL::isa) >= 0.05

%description
Role based access control is very simple: every user has a list of roles,
which that user is allowed to assume, and every restricted part of the app
makes an assertion about the necessary roles.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Authorization-Roles-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
