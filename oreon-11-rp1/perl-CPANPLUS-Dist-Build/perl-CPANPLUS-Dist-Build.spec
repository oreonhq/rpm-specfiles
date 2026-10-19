%global source0_hash 2ec900ea343f9e2ab745b44514bcf0364d60c5c49a53c90138dd1c0b940fa1b8
Name:           perl-CPANPLUS-Dist-Build
Version:        0.90
Release:        1%{?dist}
Summary:        Module::Build extension for CPANPLUS
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS-Dist-Build
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/CPANPLUS-Dist-Build-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CPANPLUS) >= 0.84
Requires:       perl(deprecate)
Requires:       perl(Exporter)
Requires:       perl(IPC::Cmd) >= 0.42
Requires:       perl(Module::Build) >= 0.32
Requires:       perl(Module::Load::Conditional) >= 0.30
Requires:       perl(Params::Check) >= 0.26
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((IPC::Cmd|Module::Load::Conditional|Params::Check)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(CPANPLUS::Backend)
BuildRequires:  perl(CPANPLUS::Configure)
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(CPANPLUS::Internals::Constants)
BuildRequires:  perl(CPANPLUS::Internals::Utils)
BuildRequires:  perl(CPANPLUS::Module::Author::Fake)
BuildRequires:  perl(CPANPLUS::Module::Fake)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Installed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Packlist)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::ConfigData)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
CPANPLUS::Dist::Build is a distribution class for Module::Build related
modules. With this package, you can create, install and uninstall
Module::Build-based perl modules by calling CPANPLUS::Dist methods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPANPLUS-Dist-Build-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
