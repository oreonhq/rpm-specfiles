%global source0_hash cce52ef65d61a1e111de7549815aab902982cf152170e85720c1215efb699008
Name:           perl-Carmel
Version:        0.1.56
Release:        1%{?dist}
Summary:        CPAN Artifact Repository Manager
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Carmel
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Carmel-v%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carton::Dist)
Requires:       perl(Carton::Index)
Requires:       perl(Carton::Package)
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(Data::Dumper)
Requires:       perl(ExtUtils::Install) >= 1.47
Requires:       perl(ExtUtils::InstallPaths)
Requires:       perl(File::pushd) >= 1.009
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(Menlo::CLI::Compat) >= 1.9018
Requires:       perl(Module::CPANfile) >= 1.1000
Requires:       perl(Module::Metadata) >= 1.000003
Requires:       perl(Module::Runtime) >= 0.014
Requires:       perl(Path::Tiny) >= 0.068
Requires:       perl(Try::Tiny) >= 0.20
Requires:       perl(lib)
Recommends:     perl(Text::Diff)
%global __requires_exclude ^perl\\(((Class|Path|Try)::Tiny|File::pushd|Module::(CPANfile|Metadata|Runtime))
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carton)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::InstallPaths)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Menlo::CLI::Compat)
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Carmel is yet another CPAN module manager.

Unlike traditional CPAN module installer, Carmel keeps the build of your
dependencies in a central repository, then select the library paths to
include upon runtime in development.

Carmel also allows you to rollout all the files in a traditional perl
INC directory structure, which is useful to use in a production
environment, such as containers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Carmel-v%{version}
%oreon_prep
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
