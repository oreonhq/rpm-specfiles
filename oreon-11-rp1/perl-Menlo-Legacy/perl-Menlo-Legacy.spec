%global source0_hash a6acac3fee318a804b439de54acbc7c27f0b44cfdad8551bbc9cd45986abc201

Name:           perl-Menlo-Legacy
Version:        1.9022
Release:        23%{?dist}
Summary:        Legacy internal and client support for Menlo
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Menlo-Legacy
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Menlo-Legacy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
# BuildRequires:  perl(Archive::Tar)
# BuildRequires:  perl(Archive::Zip)
# BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
# BuildRequires:  perl(CPAN::Common::Index::LocalPackage)
# BuildRequires:  perl(CPAN::DistnameInfo)
# BuildRequires:  perl(CPAN::Meta)
# BuildRequires:  perl(CPAN::Meta::Check)
# BuildRequires:  perl(CPAN::Meta::Requirements)
# BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Cwd)
# BuildRequires:  perl(Digest::SHA)
# BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
# BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
# BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
# BuildRequires:  perl(HTTP::Tinyish)
# BuildRequires:  perl(JSON::PP)
# BuildRequires:  perl(local::lib)
BuildRequires:  perl(Menlo) >= 1.9018
# BuildRequires:  perl(Menlo::Builder::Static)
BuildRequires:  perl(Menlo::Dependency)
# BuildRequires:  perl(Menlo::Index::MetaCPAN)
# BuildRequires:  perl(Menlo::Index::MetaDB)
# BuildRequires:  perl(Menlo::Index::Mirror)
BuildRequires:  perl(Menlo::Util)
# BuildRequires:  perl(Module::CoreList)
# BuildRequires:  perl(Module::CPANfile)
# BuildRequires:  perl(Module::Metadata)
# BuildRequires:  perl(Module::Signature)
# BuildRequires:  perl(Parse::PMFile)
# BuildRequires:  perl(Safe)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(version) >= 0.9905
# BuildRequires:  perl(version::vpp)
# Tests
BuildRequires:  perl(Test::More) >= 0.96
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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
