%global source0_hash 092df9d93150c115fb071fad7ce521152c50bb5c5f9d1315f7298349201517db
Name:           perl-Test-CheckManifest
Version:        1.43
Release:        1%{?dist}
Summary:        Check if your Manifest matches your distro
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-CheckManifest
Source0:        https://cpan.metacpan.org/authors/id/R/RE/RENEEB/Test-CheckManifest-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Test::CheckManifest)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This package checks whether the Manifest file matches the distro or not. To
match a distro the Manifest has to name all files that come along with the
distribution.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# Unpackage tarball in a subdirectory, otherwise the testsuite will fail.
%setup -q -c -n %{name}-%{version}
%setup -q -T -D -n %{name}-%{version} -a0

%if ("%{version}" == "1.42") || ("%{version}" == "1.43")
cd Test-CheckManifest-%{version}
# Bogus deps
sed -i -e '/Data::Dumper/d' META.json META.yml Makefile.PL
cd ..
%endif

%build

cd Test-CheckManifest-%{version}
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
cd ..
%install
cd Test-CheckManifest-%{version}
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
cd ..
%oreon_autofiles main

%check

cd Test-CheckManifest-%{version}
%{__make} test
cd ..
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
