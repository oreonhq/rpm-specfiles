%global source0_hash 50ecd07fb6cab7b2b2a73b5526ee43b90e77734c9bcec95ce8822b9c0a912b68

Name:		perl-Test-Distribution
Version:	2.00
Release:	50%{?dist}
Summary:	Perform tests on all modules of a distribution
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Distribution
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Distribution-%{version}.tar.gz
Patch0:		Test-Distribution-2.00-utf8.patch
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build)
# Module
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(File::Find::Rule) >= 0.03
BuildRequires:	perl(Module::CoreList) >= 1.93
BuildRequires:	perl(Module::Signature)
BuildRequires:	perl(Pod::Coverage) >= 0.17
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 0.95
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
# (no additional dependencies)
# Dependencies
# these are considered "optional"; autoreq doesn't pick them up
Requires:	perl(File::Find::Rule) >= 0.03
Requires:	perl(Module::CoreList) >= 1.93
Requires:	perl(Module::Signature)
Requires:	perl(Pod::Coverage) >= 0.17
Requires:	perl(Test::Pod) >= 0.95
Requires:	perl(Test::Pod::Coverage)

Provides:       perl(Test::Distribution)
%description
When using this module in a test script, it goes through all the modules in
your distribution, checks their POD, checks that they compile OK and checks
that they all define a $VERSION.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Distribution-%{version}

# Fix character encoding of documentation
%patch -P 0

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes.pod README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Distribution.3*

%changelog
%autochangelog
