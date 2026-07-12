%global source0_hash 0555bb7ac67d839747056054669065e1305ff4b4e7283d9ac43b7a62cd007cbd

Name:           perl-Test-HasVersion
Version:        0.014
Release:        30%{?dist}
Summary:        Check Perl modules have version numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-HasVersion
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-HasVersion-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Module Runtime
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::Builder::Tester) >= 1.04
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.18
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Dependencies
# (none)

Provides:       perl(Test::HasVersion)
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
# test_version described in Test::HasVersion manpage
mkdir -p %{buildroot}%{_mandir}/man1
echo ".so man3/Test::HasVersion.$(perl -MConfig -e 'print $Config{man3ext}')" > %{buildroot}%{_mandir}/man1/test_version.1
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/test_version
%{perl_vendorlib}/Test/
%{_mandir}/man1/test_version.1*
%{_mandir}/man3/Test::HasVersion.3*

%changelog
%autochangelog
