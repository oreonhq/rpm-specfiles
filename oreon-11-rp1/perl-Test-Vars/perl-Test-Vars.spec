%global debug_package %{nil}
%global source0_hash 56ddacbb663cf542673aa65525ef50980b53f207770e743a1d18614bd8268178
Name:           perl-Test-Vars
Version:        0.017
Release:        1%{?dist}
Summary:        Detects unused variables in perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Vars
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/Test-Vars-%{version}.tar.gz
%{?perl_default_filter}
Provides:       perl(Test::Vars)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(parent)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Detects unused variables in perl modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Vars-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
