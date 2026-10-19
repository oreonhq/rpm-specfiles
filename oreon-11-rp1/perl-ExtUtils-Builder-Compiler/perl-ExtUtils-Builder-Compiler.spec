%global source0_hash 79890f72ebe447ed8bf9b4ae9216a0f5fae460f424845f2467e2d2e4edb85b07
Name:           perl-ExtUtils-Builder-Compiler
Version:        0.035
Release:        1%{?dist}
Summary:        Interface around different compilers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-Builder-Compiler
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/ExtUtils-Builder-Compiler-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(ExtUtils::Builder) >= 0.016
Requires:       perl(ExtUtils::Builder::Planner) >= 0.007
Requires:       perl(DynaLoader)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Builder)
BuildRequires:  perl(ExtUtils::Builder::Action::Command)
BuildRequires:  perl(ExtUtils::Builder::Node)
BuildRequires:  perl(ExtUtils::Builder::Planner)
BuildRequires:  perl(ExtUtils::Builder::Planner::Extension)
BuildRequires:  perl(ExtUtils::Builder::Util)
BuildRequires:  perl(ExtUtils::Config)
BuildRequires:  perl(ExtUtils::Helpers)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(sort)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is an interface wrapping around different compilers. It's usually not
used directly but by a portability layer like
ExtUtils::Builder::Autodetect::C.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-Builder-Compiler-%{version}

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
