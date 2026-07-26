%global source0_hash 1af0fa5d6d38e8edf6b6c5349b69f03cc541b68d700aaf782196f4e3f2bbf816

Name:           perl-Catalyst-ActionRole-ACL
Version:        0.07
Release:        38%{?dist}
Summary:        User role-based authorization action class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-ActionRole-ACL
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-ActionRole-ACL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller::ActionRole)
BuildRequires:  perl(Catalyst::Runtime) >= 5.90013
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(inc::Module::Install) >= 0.91
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(Catalyst::Runtime) >= 5.90013

%{?perl_default_filter}

%description
Provides a Catalyst reusable action role for user role-based authorization.
ACLs are applied via the assignment of attributes to application action
subroutines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-ActionRole-ACL-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
