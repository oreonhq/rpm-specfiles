%global source0_hash c72c51a1da70c306562f3f1cd5e5591266a0ba3e7590812b6a7dbfb8acfd5552
Name:		perl-Module-Package-Au
Version:	2
Release:        1%{?dist}
Summary:        Reusable Module::Install bits
License:	CC0-1.0
URL:		https://metacpan.org/release/Module-Package-Au
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Module-Package-Au-%{version}.tar.gz
BuildArch:	noarch
%{?perl_default_filter}
Provides:       perl(Module::Package::Au)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::ReadmeMarkdownFromPod)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Package)
BuildRequires:  perl(Module::Package::Plugin)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module defines a set of standard configurations for Makefile.PL
files based on Module::Package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Package-Au-%{version}
rm -rf inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

# Work around goofy perl versioning mistakes of the past
sed -i 's|1.110730|1.301|g' lib/Module/Package/Au.pm
sed -i 's|1.110730|1.301|g' META.yml

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2-33
- Import
