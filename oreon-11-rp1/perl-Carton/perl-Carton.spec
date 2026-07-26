%global source0_hash 9c4558ca97cd08b69fdfb52b28c3ddc2043ef52f0627b90e53d05a4087344175

Name:           perl-Carton
Version:        1.0.35
Release:        11%{?dist}
Summary:        Perl module dependency manager (aka Bundler for Perl)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Carton
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Carton-v%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# NOTE: there's no real non-interactive test suite
# BuildRequires:  perl(App::FatPacker)
# BuildRequires:  perl(Carp)
# BuildRequires:  perl(Class::Tiny) >= 1.001
# BuildRequires:  perl(Config)
# BuildRequires:  perl(constant)
# BuildRequires:  perl(CPAN::Meta) >= 2.120921
# BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
# BuildRequires:  perl(File::Find)
# BuildRequires:  perl(File::pushd)
# BuildRequires:  perl(Getopt::Long) >= 2.39
# BuildRequires:  perl(JSON::PP) >= 2.27300
# BuildRequires:  perl(Menlo::CLI::Compat) >= 1.9018
# BuildRequires:  perl(Module::CoreList)
# BuildRequires:  perl(Module::CPANfile) >= 0.9031
# BuildRequires:  perl(overload)
# BuildRequires:  perl(parent) >= 0.223
# BuildRequires:  perl(Path::Tiny) >= 0.033
# BuildRequires:  perl(Scalar::Util)
# BuildRequires:  perl(subs)
# BuildRequires:  perl(Try::Tiny) >= 0.09
# BuildRequires:  perl(version)
# Optional run-time
# BuildRequires:  perl(IO::Compress::Gzip)
# Tests only
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(CPAN::Meta) >= 2.120921
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Getopt::Long) >= 2.39
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(Menlo::CLI::Compat) >= 1.9018
Requires:       perl(Module::CPANfile) >= 0.9031
Requires:       perl(parent) >= 0.223
Requires:       perl(Path::Tiny) >= 0.033
Requires:       perl(Try::Tiny) >= 0.09
# See the docs
Recommends:     perl
Suggests:       perl(IO::Compress::Gzip)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::Tiny\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::Requirements\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Getopt::Long\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Module::CPANfile\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Path::Tiny\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Try::Tiny\\)$
%global __requires_exclude %__requires_exclude|^perl\\(parent\\)$

%description
carton is a command line tool to track the Perl module dependencies for
your Perl application.  Dependencies are declared using cpanfile format,
and the managed dependencies are tracked in a cpanfile.snapshot file,
which is meant to be version controlled, and the snapshot file allows
other developers of your application to have the exact same versions of
the modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Carton-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/carton
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
