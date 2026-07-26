%global source0_hash fe71e53320bee13197749a0b17609aa263f71ff46e5e2c130e94742ea6abdf56

Name:           perl-Module-Install-XSUtil
Version:        0.45
Release:        34%{?dist}
Summary:        Utility functions for XS modules
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-XSUtil
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/Module-Install-XSUtil-%{version}.tar.gz
# Fix test, CPAN RT#77780
Patch0:         Module-Install-XSUtil-0.43-Fix-test-to-use-renamed-requires_xs.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Repository)
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::CheckLib) >= 0.4
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.18
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Install) >= 0.91
BuildRequires:  perl(Module::Install::Base)
# Optional:
BuildRequires:  perl(Devel::PPPort) >= 3.19
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
# Run authors tests because these are the only real tests
BuildRequires:  perl(B::Hooks::OP::Annotation) >= 0.43
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Test::Spellunker)
Requires:       perl(Devel::CheckLib) >= 0.4
Requires:       perl(ExtUtils::ParseXS) >= 3.18
Requires:       perl(File::Basename)
Requires:       perl(File::Temp)
Requires:       perl(Module::Install) >= 0.91
Requires:       perl(XSLoader) >= 0.1

%description
Module::Install::XSUtil provides a set of utilities to setup distributions
which include or depend on an XS module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-XSUtil-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf inc/*
sed -i -e '/^inc\//d' MANIFEST
# Run author tests, setting TEST_FILES clashes with nested test (CPAN RT#77780)
mkdir inc/.author

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
