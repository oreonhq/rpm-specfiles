%global source0_hash 849205d0d2c065d916c5cc7438a101ae50ec561e0adc844c0e90a823448595f9

Name:           perl-Module-Install-Repository
Version:        0.08
Release:        5%{?dist}
Summary:        Automatically sets repository URL from Svn/Svk/Git checkout
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-Repository
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Install-Repository-%{version}.tar.gz



Patch0:         Module-Install-Repository-0.06-Fix-building-on-Perl-without-dot-in-INC.patch
Patch1:         Module-Install-Repository-0.08-Update-test_requires.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 0:5.005
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test::More)

%description
Module::Install::Repository is a Module::Install plugin to automatically
figure out repository URL and set it via repository(), which then will be
added to resources under META.yml.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Install-Repository-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} -c $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Install::Repository.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.08-5
- Prepare for Oreon 11 (RP1)
