%global source0_hash f2de1afb4f0c56c36e6d5260aa0bd2c8f18e4d85009dcf5842204ea2a7fbc3df
%if ! 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_without perl_YAML_Syck_enables_optional_test
%else
%bcond_with perl_YAML_Syck_enables_optional_test
%endif
Name:           perl-YAML-Syck
Version:        1.45
Release:        1%{?dist}
Summary:        Fast, lightweight YAML loader and dumper
License:        GPL-2.0-or-later AND MIT
URL:            https://metacpan.org/release/YAML-Syck
Source0:        https://cpan.metacpan.org/modules/by-module/YAML/YAML-Syck-%{version}.tar.gz
%if %{with perl_YAML_Syck_enables_optional_test}
%endif
%{?perl_default_filter}
Provides:       perl(YAML::Syck)
Provides:       perl(YAML::Syck)
Provides:       perl(JSON::Syck)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Leak)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Mksymlists)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a Perl interface to the libsyck data serialization
library. It exports the Dump and Load functions for converting Perl data
structures to YAML strings, and the other way around.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n YAML-Syck-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
  OPTIMIZE="%{optflags} -DI_STDLIB=1 -DI_STRING=1"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.45-1
- Import
