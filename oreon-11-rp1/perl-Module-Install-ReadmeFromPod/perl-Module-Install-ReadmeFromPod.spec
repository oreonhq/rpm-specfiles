%global source0_hash 79f6df5536619faffbda696bdd25ccad17c469bf32e51cd3e613366d49400169

%if ! (0%{?rhel})
# Perform optional tests
%{bcond_without perl_Module_Install_ReadmeFromPod_enables_optional_test}
# Support output to PDF
%{bcond_without perl_Module_Install_ReadmeFromPod_enables_pdf}
%else
%{bcond_with perl_Module_Install_ReadmeFromPod_enables_optional_test}
%{bcond_with perl_Module_Install_ReadmeFromPod_enables_pdf}
%endif

Name:           perl-Module-Install-ReadmeFromPod
Version:        0.30
Release:        30%{?dist}
Summary:        Module::Install extension to automatically convert POD to a README
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-ReadmeFromPod
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-Install-ReadmeFromPod-%{version}.tar.gz
# Regenerate README in UTF-8
Patch0:         Module-Install-ReadmeFromPod-0.26-Regenerate-README-in-UTF-8.patch
# Remove a bogus test that fails on PDF binary files randomly, CPAN RT#130221
Patch1:         Module-Install-ReadmeFromPod-0.30-Do-not-test-PDF-file-for-new-lines.patch
# Avoid an unnecessary development dependency
Patch2:         Module-Install-ReadmeFromPod-0.30-Test-InDistDir.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AutoLicense)
BuildRequires:  perl(Module::Install::AuthorRequires) >= 0.02
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(strict)
# Build script uses lib/Module/Install/ReadmeFromPod.pm
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny) >= 0.05
BuildRequires:  perl(IO::All)
# Module::Install::Base version from Module::Install in Makefile.PL
BuildRequires:  perl(Module::Install::Base) >= 1
BuildRequires:  perl(Pod::Html)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Markdown) >= 2
BuildRequires:  perl(Pod::Text) >= 3.13
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
%if %{with perl_Module_Install_ReadmeFromPod_enables_pdf}
BuildRequires:  perl(App::pod2pdf)
%endif
# Tests:
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.47
%if %{with perl_Module_Install_ReadmeFromPod_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
%if %{with perl_Module_Install_ReadmeFromPod_enables_pdf}
Suggests:       perl(App::pod2pdf)
%endif
Requires:       perl(Capture::Tiny) >= 0.05
Requires:       perl(IO::All)
# Module::Install::Base version from Module::Install in Makefile.PL
Requires:       perl(Module::Install::Base) >= 1
Requires:       perl(Pod::Html)
Requires:       perl(Pod::Man)
Requires:       perl(Pod::Markdown) >= 2
Requires:       perl(Pod::Text) >= 3.13

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Module::Install::Base\\)$

Provides:       perl(Module::Install::ReadmeFromPod)
%description
Module::Install::ReadmeFromPod is a Module::Install extension that
generates a README file automatically from an indicated file containing
POD, whenever the author runs Makefile.PL. Several output formats are
supported: plain-text, HTML, PDF or manual page.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Install-ReadmeFromPod-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Drop executable bit from documentation
chmod -x tools/git-log.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README tools
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30-30
- Prepare for Oreon 11 (RP1)
