%global source0_hash ecc4b81905fd1ab87c88ae4b4c4ef1e25302924872dbbbbc190e0672a148ee2a
Name:           perl-Dist-Zilla-Plugin-LicenseFromModule
Version:        0.07
Release:        22%{?dist}
Summary:        Extract license and copyright from its main module file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-LicenseFromModule
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-LicenseFromModule-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::Zilla) >= 4.30003
Requires:       perl(Dist::Zilla::Role::LicenseProvider)
Requires:       perl(Module::Load) >= 0.32
Recommends:     perl(Pod::Escapes)
Suggests:       perl(Pod::Text)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Module::Load\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::Role::LicenseProvider)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is is a Dist::Zilla plugin to extract license, author and copyright year
from your main module's POD document.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-LicenseFromModule-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
