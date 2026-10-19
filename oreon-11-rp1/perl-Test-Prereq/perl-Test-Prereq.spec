%global source0_hash 46822f029168f474c4e8e920f3a7b18d649097c0a06f17fb07b6e39e85150c1f
Name:           perl-Test-Prereq
Version:        2.005
Release:        1%{?dist}
Summary:        Check if Makefile.PL has the right pre-requisites
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Prereq
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Prereq-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Extract::Use)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Manifest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The prereq_ok() function examines the modules it finds in blib/lib/,
blib/script, and the test files it finds in t/ (and test.pl). It figures out
which modules they use and compares that list of modules to those in the
PREREQ_PM section of Makefile.PL.

If you use Module::Build, see Test::Prereq::Build instead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Prereq-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
