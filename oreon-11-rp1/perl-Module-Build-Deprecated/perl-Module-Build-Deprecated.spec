%global source0_hash be089313fc238ee2183473aca8c86b55fb3cf44797312cbe9b892d6362621703

Name:           perl-Module-Build-Deprecated
Version:        0.4210
Release:        33%{?dist}
Summary:        Collection of modules removed from Module-Build
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Build-Deprecated
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-Deprecated-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.3601
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.002
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(parent)
BuildRequires:  perl(version) >= 0.87
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       perl(CPAN::Meta::YAML) >= 0.002
Requires:       perl(version) >= 0.87
Conflicts:      perl-Module-Build < 0.42.07

%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}perl\\(CPAN::Meta::YAML|version\\)

Provides:       perl(Module::Build::Version)
%description
This module contains a number of module that have been removed from
Module-Build:
Module::Build::ModuleInfo - This has been superseded by Module::Metadata
Module::Build::Version - This has been replaced by version
Module::Build::YAML - This has been replaced by CPAN::Meta::YAML

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Build-Deprecated-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
