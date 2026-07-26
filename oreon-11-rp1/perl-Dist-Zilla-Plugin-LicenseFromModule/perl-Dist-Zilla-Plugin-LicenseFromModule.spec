%global source0_hash ecc4b81905fd1ab87c88ae4b4c4ef1e25302924872dbbbbc190e0672a148ee2a

Name:           perl-Dist-Zilla-Plugin-LicenseFromModule
Version:        0.07
Release:        22%{?dist}
Summary:        Extract license and copyright from its main module file
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-LicenseFromModule
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-LicenseFromModule-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# This is a Dist::Zilla plugin
BuildRequires:  perl(Dist::Zilla) >= 4.30003
BuildRequires:  perl(Dist::Zilla::Role::LicenseProvider)
BuildRequires:  perl(Module::Load) >= 0.32
BuildRequires:  perl(Moose)
BuildRequires:  perl(Software::LicenseUtils)
# Optional run-time:
# Prefer Pod::Escapes over Pod::Text
BuildRequires:  perl(Pod::Escapes)
# Tests:
BuildRequires:  perl(JSON)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
# This is a Dist::Zilla plugin
Requires:       perl(Dist::Zilla) >= 4.30003
Requires:       perl(Dist::Zilla::Role::LicenseProvider)
Requires:       perl(Module::Load) >= 0.32
# Optional run-time:
# Prefer Pod::Escapes over Pod::Text
Recommends:     perl(Pod::Escapes)
Suggests:       perl(Pod::Text)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Module::Load\\)$

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

%check
unset AUTHOR_TESTING
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
