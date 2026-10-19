%global source0_hash a71f2fe8b96ab8bfc2760aa1d3135ea049a5b20dcb105457b769a1195c7a2509
Name:           perl-Test-UseAllModules
Version:        0.17
Release:        32%{?dist}
Summary:        Do use_ok() for all the MANIFESTed modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-UseAllModules
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-UseAllModules-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Test::Builder) >= 0.30
Requires:       perl(Test::More) >= 0.60
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Test::More\\)
Provides:       perl(Test::UseAllModules)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
I'm sick of writing 00_load.t (or something like that) that will do use_ok()
for every module I write. I'm sicker of updating 00_load.t when I add
another file to the distribution. This module reads MANIFEST to find modules
to be tested and does use_ok() for each of them. Now all you have to do is
update MANIFEST. You don't have to modify the test any more (hopefully).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-UseAllModules-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

TEST_POD=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
