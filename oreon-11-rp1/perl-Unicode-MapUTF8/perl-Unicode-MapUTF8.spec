%global source0_hash 85ddb1de88dc96e4f211ca57d9685e41ce4da0764671117dceeb0e05cad8a5b0
Name:           perl-Unicode-MapUTF8
Version:        1.14
Release:        1%{?dist}
Summary:        Conversions to and from arbitrary character sets and UTF8
License:        MIT
URL:            https://metacpan.org/release/Unicode-MapUTF8
Source0:        https://cpan.metacpan.org/modules/by-module/Unicode/Unicode-MapUTF8-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Jcode)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Unicode::Map)
BuildRequires:  perl(Unicode::Map8)
BuildRequires:  perl(Unicode::String)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Unicode::MapUTF8 Provides an adapter layer between core routines for
converting to and from UTF8 and other encodings. In essence, a way to
give multiple existing Unicode modules a single common interface so
you don't have to know the underlying implementations to do simple
UTF8 to-from other character set string conversions. As such, it wraps
the Unicode::String, Unicode::Map8, Unicode::Map and Jcode modules in
a standardized and simple API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Unicode-MapUTF8-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
