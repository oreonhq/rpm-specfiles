# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2ead44c973c748d72d9f199e41c44dc1801fe9ae06b0fadc59447693a3c98281
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:       perl-Module-Install-GithubMeta 
Version:    0.30
Release:    32%{?dist}
# lib/Module/Install/GithubMeta.pm -> GPL+ or Artistic
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    A Module::Install extension to include GitHub meta information in META.yml 
Source:     https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-Install-GithubMeta-%{version}.tar.gz 
Url:        https://metacpan.org/release/Module-Install-GithubMeta
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(base)
BuildRequires: perl(Capture::Tiny) >= 0.05
BuildRequires: perl(Config)
BuildRequires: perl(Cwd)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Install) >= 0.85
BuildRequires: perl(strict)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::Pod)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)

Requires:      perl(Module::Install) >= 0.85

%{?perl_default_filter}

%description
Module::Install::GithubMeta is a Module::Install extension
to include GitHub (http://github.com) meta information in
'META.yml'.  It automatically detects if the distribution 
directory is under 'git' version control and whether the 
'origin' is a GitHub repository; if so, it will set the
'repository' and 'homepage' meta in 'META.yml' to the 
appropriate URLs for GitHub.


%prep
%oreon_verify_sources
%setup -q -n Module-Install-GithubMeta-%{version}

cat README | iconv -f `file --mime-encoding --brief README` -t UTF-8 > x
mv x README

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30-32
- Prepare for Oreon 11 (RP1)
