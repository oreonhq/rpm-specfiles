%global source0_hash 7c01fa56c78a60369aef55fe668f462a2b1d778d7d106966994f4cfaf430ed07

Name:           perl-Module-Info
Version:        0.39
Release:        4%{?dist}
Summary:        Information about Perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Info
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Module-Info-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(B::Utils) >= 0.27
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec) >= 0.8
# XXX: BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Safe)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Cwd) >= 1.1.2
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(File::Spec) >= 0.8
# XXX: Requires:       perl(IPC::Open3)
Requires:       perl(Safe)
Requires:       perl(version)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$

%description
Module::Info gives you information about Perl modules without actually loading
the module. It isn't actually specific to modules and should work on any perl
code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Info-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset RELEASE_TESTING
make test

%files
%doc Changes README
%{_bindir}/module_info
%{_bindir}/pfunc
%{perl_vendorlib}/B/*
%{perl_vendorlib}/Module/*
%{_mandir}/man1/module_info*
%{_mandir}/man1/pfunc*
%{_mandir}/man3/B::Module*
%{_mandir}/man3/Module*

%changelog
%autochangelog
