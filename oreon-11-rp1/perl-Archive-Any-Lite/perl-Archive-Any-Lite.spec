%global source0_hash 15c188253993a4b66e5599f0789b1326f0a66c092bdbfac9313706d41c285170

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_Archive_Any_Lite_enables_extra_test
%else
%bcond_with perl_Archive_Any_Lite_enables_extra_test
%endif

Name:		perl-Archive-Any-Lite
Version:	0.11
Release:	30%{?dist}
Summary:	Simple CPAN package extractor 
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Archive-Any-Lite
Source0:	https://cpan.metacpan.org/modules/by-module/Archive/Archive-Any-Lite-%{version}.tar.gz
Patch0:		Archive-Any-Lite-0.08-EU:MM.patch
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
# Module
BuildRequires:	perl(Archive::Tar) >= 1.76
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Uncompress::Bunzip2)
BuildRequires:	perl(IO::Zlib)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp) >= 0.19
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Test::More) >= 0.82
BuildRequires:	perl(Test::UseAllModules) >= 0.10
# Optional Tests
%if %{with perl_Archive_Any_Lite_enables_extra_test}
BuildRequires:	perl(Parallel::ForkManager) >= 0.7.6
%endif
BuildRequires:	perl(Test::Pod) >= 1.18
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
# Runtime
Requires:	perl(IO::Uncompress::Bunzip2)
Requires:	perl(IO::Zlib)

Provides:       perl(Archive::Any::Lite)
%description
This is a fork of Archive::Any by Michael Schwern and Clint Moore. The main
difference is that this works properly even when you fork(), and may require
less memory to extract a tarball. On the other hand, this isn't pluggable
(it only supports file formats used in the CPAN toolchains), and it doesn't
check MIME types.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Archive-Any-Lite-%{version}

# Build with ExtUtils::MakeMaker rather than ExtUtils::MakeMaker::CPANfile
%patch -P0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test TEST_POD=1

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Archive/
%{_mandir}/man3/Archive::Any::Lite.3*

%changelog
%autochangelog
