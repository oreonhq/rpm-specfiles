%global source0_hash 4f9e4d2622481b79cc298e8e29de8a30943aff9f4be7992c0ebb7b22e5b4b297

Name:           perl-List-SomeUtils-XS
Version:        0.58
Release:        27%{?dist}
Summary:        XS implementation for List::SomeUtils
License:        Artistic-2.0 AND ( GPL-1.0-or-later OR Artistic-1.0-Perl )
URL:            https://metacpan.org/release/List-SomeUtils-XS
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-XS-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(List::SomeUtils::PP)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::SomeUtils) >= 0.56
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.006
Requires:       perl(List::SomeUtils::PP)
Requires:       perl(XSLoader)

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

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/List*
%{_mandir}/man3/*

%changelog
%autochangelog
