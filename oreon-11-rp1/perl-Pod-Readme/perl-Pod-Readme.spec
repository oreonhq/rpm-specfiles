%global source0_hash d379f98976ebe5225d768ccb3a760e9b5673eb3f3d8ae8f57430ed9513f22857

Name:           perl-Pod-Readme
Version:        1.2.3
Release:        21%{?dist}
Summary:        Intelligently generate a README file from POD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Readme
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Readme-v%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Method::Modifiers) >= 2.00
BuildRequires:  perl(CPAN::Changes) >= 0.30
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.56
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Moo) >= 1.004005
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::HandlesVia)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny) >= 0.018
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny) >= 1.000000
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(warnings)
# Script Runtime
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(IO::Handle)
# Test Suite
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Pod::Simple::Text)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
# Pod::Readme::Test::Kit not actually used
#BuildRequires: perl(Test::Kit)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(Role::Tiny)

Provides:       perl(Pod::Readme)
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

%check
make test

%files
%license LICENSE
%doc Changes README.pod
%{_bindir}/pod2readme
%{perl_vendorlib}/Pod/
%{_mandir}/man1/pod2readme.1*
%{_mandir}/man3/Pod::Readme.3*
%{_mandir}/man3/Pod::Readme::Filter.3*
%{_mandir}/man3/Pod::Readme::Plugin.3*
%{_mandir}/man3/Pod::Readme::Plugin::changes.3*
%{_mandir}/man3/Pod::Readme::Plugin::requires.3*
%{_mandir}/man3/Pod::Readme::Plugin::version.3*
%{_mandir}/man3/Pod::Readme::Types.3*

%changelog
%autochangelog
