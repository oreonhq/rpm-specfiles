%global source0_hash c122d6e2df6136ce9bea1e6d2b776cb9e69e00085ece995301814c7af3a8e814

Name:           perl-Class-Data-Accessor
Version:        0.04004
Release:        47%{?dist}
Summary:        Inheritable, overridable class and instance data accessor creation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Data-Accessor
Source0:        https://cpan.metacpan.org/authors/id/C/CL/CLACO/Class-Data-Accessor-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 0.65
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-podlators
BuildRequires:  sed
# Run-time
BuildRequires: perl(Carp)
BuildRequires: perl(vars)
# Tests
BuildRequires: perl(base)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(lib)
BuildRequires: perl(Test::More)
# Author tests
#BuildRequires: perl(Pod::Coverage) >= 0.14
#BuildRequires: perl(Test::CheckManifest) >= 0.09
#BuildRequires: perl(Test::NoTabs) >= 0.03
#BuildRequires: perl(Test::Pod) >= 1.00
#BuildRequires: perl(Test::Pod::Coverage) >= 1.04
#BuildRequires: perl(Test::Spelling) >= 0.11
#BuildRequires: perl(Test::Strict) >= 0.05

%description
Class::Data::Accessor is the marriage of Class::Accessor and
Class::Data::Inheritable into a single module. It is used for creating
accessors to class data that overridable in subclasses as well as in class
instances.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Data-Accessor-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

sed -i 's/\r//' t/*.t Changes
perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
# set TEST_AUTHOR=1 to enable the upstream author tests.
make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
