%global source0_hash c122d6e2df6136ce9bea1e6d2b776cb9e69e00085ece995301814c7af3a8e814
Name:           perl-Class-Data-Accessor
Version:        0.04004
Release:        1%{?dist}
Summary:        Inheritable, overridable class and instance data accessor creation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Data-Accessor
Source0:        https://cpan.metacpan.org/authors/id/C/CL/CLACO/Class-Data-Accessor-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
