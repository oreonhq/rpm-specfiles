%global source0_hash 4f9e4d2622481b79cc298e8e29de8a30943aff9f4be7992c0ebb7b22e5b4b297
Name:           perl-List-SomeUtils-XS
Version:        0.58
Release:        27%{?dist}
Summary:        XS implementation for List::SomeUtils
License:        Artistic-2.0 AND ( GPL-1.0-or-later OR Artistic-1.0-Perl )
URL:            https://metacpan.org/release/List-SomeUtils-XS
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-XS-%{version}.tar.gz
Requires:       perl(List::SomeUtils::PP)
Requires:       perl(XSLoader)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(List::SomeUtils::PP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
List::SomeUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

XS implementation is faster than List::SomeUtils.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n List-SomeUtils-XS-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
