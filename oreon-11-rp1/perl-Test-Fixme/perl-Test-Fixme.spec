%global source0_hash 9ef8580420b0551f11e81541a22006837c9bdf26524d0b8bf35aa286acca878e

Name:           perl-Test-Fixme
Version:        0.17
Release:        3%{?dist}
Summary:        Check code for FIXMEs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Fixme
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Fixme-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

%description
When coding it is common to come up against problems that need to be
addressed but that are not a big deal at the moment. What generally happens
is that the coder adds comments and marks them FIXME.

Test::Fixme allows you to add a test file that ensures that none of these 
get forgotten in the module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Fixme-%{version}

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
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Fixme.3*

%changelog
%autochangelog
