%global source0_hash 4f1871fed7d93271d0b737a4332627744d65139f842ce01610e7c896252ea341
Name:           perl-CPAN-Inject
Version:        1.14
Release:        40%{?dist}
Summary:        Base class for injecting distributions into CPAN sources
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Inject
Source0:        https://cpan.metacpan.org/authors/id/P/PS/PSHANGOV/CPAN-Inject-%{version}.tar.gz
Patch0:         CPAN-Inject-1.14-Restore-working-directory-after-loading-CPAN-configu.patch
Patch1:         CPAN-Inject-1.14-Expect-unknown-exception-while-loading-CPAN-configur.patch
BuildArch:      noarch
Requires:       perl(CPAN) >= 1.36
Requires:       perl(CPAN::Checksums) >= 1.05
Requires:       perl(Cwd)
Requires:       perl(File::Basename) >= 2.6
Requires:       perl(File::chmod) >= 0.30
Requires:       perl(File::Copy) >= 2.02
Requires:       perl(File::Path) >= 1.00
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(File::stat) >= 1.00
Requires:       perl(File::chmod) >= 0.30
Requires:       perl(Params::Util) >= 0.21
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(CPAN::Checksums\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::(Basename|chmod|Copy|Path|Spec|stat|chmod)\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Params::Util\\)\s*$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN)
BuildRequires:  perl(CPAN::Checksums)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::chmod)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Following the release of CPAN::Mini, the CPAN::Mini::Inject module was
created to add additional distributions into a minicpan mirror.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-Inject-%{version}
%patch -P0 -p1
%patch -P1 -p1

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

export HOME=$PWD/home
mkdir "$HOME"
make test </dev/null
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
