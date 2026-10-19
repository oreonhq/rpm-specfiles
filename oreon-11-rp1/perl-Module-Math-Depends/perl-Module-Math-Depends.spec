%global source0_hash 733cd9b92e500e04f388e25413c611f93ad0f262588b2aa83d2f2880888a4f99
Name:           perl-Module-Math-Depends
Version:        0.02
Release:        48%{?dist}
Summary:        Convenience object for manipulating module dependencies
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Math-Depends
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Module-Math-Depends-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Params::Util) >= 0.10
Requires:       perl(version) >= 0.74
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(version\\)\s*$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This is a small convenience module created originally as part of
Module::Inspector but released separately, in the hope that people might
find it useful in other contexts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Math-Depends-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
