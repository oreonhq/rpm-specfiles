%global source0_hash 46822f029168f474c4e8e920f3a7b18d649097c0a06f17fb07b6e39e85150c1f

Name:           perl-Test-Prereq
Version:        2.005
Release:        4%{?dist}
Summary:        Check if Makefile.PL has the right pre-requisites
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Prereq
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Prereq-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 4:5.22.0
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Extract::Use)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 1.00
# Optional Tests
BuildRequires:  perl(Test::Manifest) >= 1.21
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# Dependencies
# (none)

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

%check
make test

%files
%license LICENSE
%doc Changes README.pod SECURITY.md
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Prereq.3*
%{_mandir}/man3/Test::Prereq::Build.3*

%changelog
%autochangelog
