Name:           perl-Module-Install-AutoLicense
Version:        0.10
Release:        26%{?dist}
Summary:        Module::Install extension to automatically generate LICENSE files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-AutoLicense
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-Install-AutoLicense-%{version}.tar.gz
Patch0:         Use-Module-Install-AutoLicense-for-tarball.patch
# oreon url source checksums begin
%global source0_sha256 5bd263365f0375ceb988cab6d3e4418695afa3ece770db12768974cee77aefe0
%global source0_file Module-Install-AutoLicense-0.10.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter >= 1:5.6.0
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Capture::Tiny) >= 0.05
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(inc::Module::Install) >= 0.85
BuildRequires:  perl(Module::Install) >= 0.85
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::Can)
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Software::License) >= 0.01
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(Module::Install) >= 0.85
Requires:       perl(Software::License) >= 0.01

%description
Module::Install::AutoLicense is a Module::Install extension that generates
a LICENSE file automatically whenever the author runs Makefile.PL. On the
user side it does nothing.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Module-Install-AutoLicense-0.10.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5bd263365f0375ceb988cab6d3e4418695afa3ece770db12768974cee77aefe0" || { echo "oreon: Source0 SHA256 mismatch for Module-Install-AutoLicense-0.10.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Module-Install-AutoLicense-%{version}
%patch -P0 -p1
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

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10-26
- Prepare for Oreon 11 (RP1)
