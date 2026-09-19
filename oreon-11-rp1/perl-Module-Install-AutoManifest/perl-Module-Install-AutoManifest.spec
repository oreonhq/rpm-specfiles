%global source0_hash 31d58092162783d657d4ade9e1f3de6a16f423081df15fc3e9434286530080fc

Name:           perl-Module-Install-AutoManifest
Version:        0.003
Release:        39%{?dist}
Summary:        The module generates MANIFEST automatically
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-AutoManifest
Source0:        https://cpan.metacpan.org/authors/id/H/HD/HDP/Module-Install-AutoManifest-%{version}.tar.gz
Patch0:         Module-Install-AutoManifest-0.003-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
This module is extension to Module::Install. It adds behavior for
automatically generating MANIFEST.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-AutoManifest-%{version}
%patch -P0 -p1
find -type f -exec chmod -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
%autochangelog
