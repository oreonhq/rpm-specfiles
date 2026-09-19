%global source0_hash d8c5de841b304048451367e7c4a8a6e0e94fb60cf18ec382b87d7a788be19bf4

Name:           perl-Module-Pluggable-Ordered
Version:        1.5
Release:        47%{?dist}
Summary:        Call module plugins in a specified order
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Pluggable-Ordered
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APEIRON/Module-Pluggable-Ordered-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Module::Pluggable) >= 1.9
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(UNIVERSAL::require)
Requires:       perl(Module::Pluggable) >= 1.9
Requires:       perl(warnings)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Pluggable\\)$

%description
This module behaves exactly the same as Module::Pluggable, supporting
all of its options, but also mixes in the call_plugins and
plugins_ordered methods to your class. call_plugins acts a little like
Class::Trigger; it takes the name of a method, and some parameters.
Let's say we call it like so:

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Pluggable-Ordered-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
