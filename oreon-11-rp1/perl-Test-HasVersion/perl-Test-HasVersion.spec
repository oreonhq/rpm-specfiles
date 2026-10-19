%global source0_hash 0555bb7ac67d839747056054669065e1305ff4b4e7283d9ac43b7a62cd007cbd
Name:           perl-Test-HasVersion
Version:        0.014
Release:        1%{?dist}
Summary:        Check Perl modules have version numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-HasVersion
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-HasVersion-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Test::HasVersion)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Do you want to check that every one of your Perl modules in a distribution has
a version number? You want to make sure you don't forget the brand new modules
you just added? Well, this is the module you have been looking for.

Do you want to check someone else's distribution to make sure the author has
not committed the sin of leaving Perl modules without a version that can be
used to tell if you have this or that feature? Test::HasVersion is also for
you.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-HasVersion-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
mkdir -p %{buildroot}%{_mandir}/man1
echo ".so man3/Test::HasVersion.$(perl -MConfig -e 'print $Config{man3ext}')" > %{buildroot}%{_mandir}/man1/test_version.1
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
