%global source0_hash 351d25ee7131628aaf7e3995fe1fffb893ae7fe6ef58cf3370ed320953f5b2a8
%global baseversion 0.12
%global extraversion 02
Name:		perl-Test-Unit-Lite
Epoch:		1
Version:	0.12%{?extraversion:.}%{?extraversion}
Release:        10%{?dist}
Summary:        Unit testing without external dependencies
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Unit-Lite
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Unit-Lite-%{baseversion}%{extraversion}.tar.gz
BuildArch:	noarch
%global __provides_exclude ^perl\\(Test::Unit::(Debug|HarnessUnit|Result|TestCase|TestRunner|TestSuite)\\)$
%global __requires_exclude ^perl\\(Test::Unit::Test(Runner|Suite)\\)
Provides:       perl(Test::Unit::Lite)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Taint::Runtime)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This framework provides a lighter version of Test::Unit framework. It
implements some of the Test::Unit classes and methods needed to run test
units. Test::Unit::Lite tries to be compatible with public API of
Test::Unit. It doesn't implement all classes and methods at 100% and only
those necessary to run tests are available.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Unit-Lite-%{baseversion}%{?extraversion}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
