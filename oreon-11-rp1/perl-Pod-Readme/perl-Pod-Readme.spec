%global source0_hash d379f98976ebe5225d768ccb3a760e9b5673eb3f3d8ae8f57430ed9513f22857
Name:           perl-Pod-Readme
Version:        1.2.3
Release:        21%{?dist}
Summary:        Intelligently generate a README file from POD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Readme
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Readme-v%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Role::Tiny)
Provides:       perl(Pod::Readme)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Changes)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::HandlesVia)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Pod::Simple::Text)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module filters POD to generate a README file, by using POD commands to
specify which parts are included or excluded from the README file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Readme-v%{version}

# Fix script interpreter
sed -i -e 's|#!/usr/bin/env perl|#!/usr/bin/perl|' bin/pod2readme

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
