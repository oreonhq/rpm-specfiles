%global source0_hash b2c7b581901054a32dfcea12536fda8626457ed0bfbc02600bd354bde7e2a9b4

Name:           perl-ExtUtils-CppGuess
Version:        0.27
Release:        %autorelease
Summary:        Guess C++ compiler and flags
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-CppGuess
Source:         https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-CppGuess-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.35
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.280231
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XSLoader)
# Dependencies
Requires:       perl(ExtUtils::ParseXS) >= 3.35

%description
ExtUtils::CppGuess attempts to guess the system's C++ compiler that is
compatible with the C compiler that your perl was built with.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ExtUtils-CppGuess-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
%make_build test

%files
%doc Changes README
%dir %{perl_vendorlib}/ExtUtils/
%{perl_vendorlib}/ExtUtils/CppGuess.pm
%{_mandir}/man3/ExtUtils::CppGuess.3*

%changelog
%autochangelog
