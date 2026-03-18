# Run optional test
%if ! 0%{?rhel}
%bcond_without perl_YAML_Syck_enables_optional_test
%else
%bcond_with perl_YAML_Syck_enables_optional_test
%endif

Name:           perl-YAML-Syck
Version:        1.36
Release:        2%{?dist}
Summary:        Fast, lightweight YAML loader and dumper
# gram.*: GPL-2.0-or-later
# *:      MIT
# Note that libsyck COPYING file describes itself as BSD but it's actually MIT
License:        GPL-2.0-or-later AND MIT
URL:            https://metacpan.org/release/YAML-Syck
Source0:        https://cpan.metacpan.org/modules/by-module/YAML/YAML-Syck-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Dependencies of bundled ExtUtils::HasCompiler
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Mksymlists)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
# Module Runtime
BuildRequires:  perl(constant)
# DynaLoader not used if XSLoader is available
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Optional Tests
%if %{with perl_YAML_Syck_enables_optional_test}
BuildRequires:  perl(Devel::Leak)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Symbol)
%endif
# Dependencies
# (none)

# Avoid provides for private perl objects
%{?perl_default_filter}

%description
This module provides a Perl interface to the libsyck data serialization
library. It exports the Dump and Load functions for converting Perl data
structures to YAML strings, and the other way around.

%prep
%setup -q -n YAML-Syck-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags} -DI_STDLIB=1 -DI_STRING=1 -std=gnu17"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc Changes COMPATIBILITY README.md
%{perl_vendorarch}/auto/YAML/
%{perl_vendorarch}/YAML/
%{perl_vendorarch}/JSON/
%{_mandir}/man3/JSON::Syck.3*
%{_mandir}/man3/YAML::Syck.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.36-2
- Prepare for Oreon 11 (RP1)
