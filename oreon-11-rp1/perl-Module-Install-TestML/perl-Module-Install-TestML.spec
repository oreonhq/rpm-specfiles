%global source0_hash 82b2d562608be5a47384bd4e9d0d3b8eef881b365f560d7062e28e5df5b62d2c
Name:           perl-Module-Install-TestML
Version:        0.02
Release:        1%{?dist}
Summary:        Module::Install support for TestML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-TestML
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Install-TestML-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Module::Install::Base) >= 1.10
Requires:       perl(warnings)
Conflicts:      perl-TestML < 0.47
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Install::Base\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module adds the use_testml_tap directive to Module::Install.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-TestML-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
