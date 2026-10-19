%global source0_hash a6acac3fee318a804b439de54acbc7c27f0b44cfdad8551bbc9cd45986abc201
Name:           perl-Menlo-Legacy
Version:        1.9022
Release:        1%{?dist}
Summary:        Legacy internal and client support for Menlo
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Menlo-Legacy
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Menlo-Legacy-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Archive::Tar)
Requires:       perl(Archive::Zip)
Requires:       perl(Capture::Tiny)
Requires:       perl(CPAN::Common::Index::LocalPackage)
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta)
Requires:       perl(CPAN::Meta::Check)
Requires:       perl(CPAN::Meta::Requirements)
Requires:       perl(CPAN::Meta::YAML)
Requires:       perl(Digest::SHA)
Requires:       perl(ExtUtils::Manifest)
Requires:       perl(File::HomeDir)
Requires:       perl(File::pushd)
Requires:       perl(HTTP::Tinyish)
Requires:       perl(JSON::PP)
Requires:       perl(local::lib)
Requires:       perl(Menlo) >= 1.9018
Requires:       perl(Menlo::Builder::Static)
Requires:       perl(Menlo::Index::MetaCPAN)
Requires:       perl(Menlo::Index::MetaDB)
Requires:       perl(Menlo::Index::Mirror)
Requires:       perl(Module::CoreList)
Requires:       perl(Module::CPANfile)
Requires:       perl(Module::Metadata)
Requires:       perl(Module::Signature)
Requires:       perl(Parse::PMFile)
Requires:       perl(Safe)
Requires:       perl(version::vpp)
Conflicts:      perl-Menlo < 1.9019
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Menlo\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Menlo)
BuildRequires:  perl(Menlo::Dependency)
BuildRequires:  perl(Menlo::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Menlo::Legacy is a package to install Menlo::CLI::Compat which is a
compatibility library that implements the classic version of cpanminus
internals and behavios. This is so that existing users of cpanm and API
clients such as Carton, Carmel and App::cpm) can rely on the stable
features and specific behaviors of cpanm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Menlo-Legacy-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
