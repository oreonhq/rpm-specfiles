%global source0_hash e8010cf1ebec23243a1a1cebca5f2724e0b519fe57d531a8a49b2ea2c173275d

Name:           perl-String-License
Version:        0.0.11
Release:        4%{?dist}
Summary:        Detect source code license statements in a text string
License:        AGPL-3.0-or-later

BuildArch:      noarch
URL:            https://metacpan.org/pod/String::License
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/String-License-v%{version}.tar.gz
# Fix failing test
# Patch0:         test.patch
# Fix build with perl-5.38
# See https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1042847
# Patch1:         perl538.patch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Array::IntSpan)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Feature::Compat::Class)
BuildRequires:  perl(File::BaseDir)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(re::engine::RE2)
BuildRequires:  perl(Regexp::Pattern)
BuildRequires:  perl(Regexp::Pattern::License)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Compare)
BuildRequires:  perl(Test2::Require)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Todo)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
String::License identifies license statements in a string and serializes them
in a normalized format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n String-License-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/String::License*.*

%changelog
%autochangelog
