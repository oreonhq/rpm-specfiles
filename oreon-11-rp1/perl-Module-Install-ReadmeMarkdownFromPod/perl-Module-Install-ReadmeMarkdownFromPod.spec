%global source0_hash 300b2e244f83b9a54a95f8404c1cd3af0635b4fae974ca65390ee428ec668591

Name:           perl-Module-Install-ReadmeMarkdownFromPod
Version:        0.04
Release:        26%{?dist}
Summary:        Create README.mkdn from POD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-ReadmeMarkdownFromPod
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTN/Module-Install-ReadmeMarkdownFromPod-0.04.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter >= 1:5.6.0
BuildRequires:  perl-generators
# XXX: We cannot remove ./inc because it build-requires this module
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN) >= 1.89
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Module::Install)
Requires:       perl(Module::Install::ReadmeFromPod)
Requires:       perl(Pod::Markdown)

%description
Module::Install::ReadmeMarkdownFromPod is a Module::Install extension that
generates a README.mkdn file automatically from an indicated file
containing POD whenever the author runs Makefile.PL. This file is used by
GitHub to display nicely formatted information about a repository.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Module-Install-ReadmeMarkdownFromPod-%{version}

# README is ISO-8859-1 encoded
iconv -f iso-8859-1 -t utf8 < README > README.utf8
mv README.utf8 README

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.04-26
- Prepare for Oreon 11 (RP1)
