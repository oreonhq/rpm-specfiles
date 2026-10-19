%global source0_hash c43ddbb22fd42b06118fe6357f53700fbd77f531ba3c427faafbf303cbf4eaf0
Name:           perl-CPAN-Common-Index
Version:        0.010
Release:        25%{?dist}
Summary:        Common library for searching CPAN modules, authors and distributions
License:        Apache-2.0
URL:            https://metacpan.org/release/CPAN-Common-Index
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Common-Index-%{version}.tar.gz
BuildArch:      noarch
Recommends:     perl(IO::Uncompress::Gunzip)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Search::Dict)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Handle::SkipHeader)
BuildRequires:  perl(URI)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a common library for working with a variety of CPAN
index services. It is intentionally minimalist, trying to use as few non-
core modules as possible.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-Common-Index-%{version}

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
