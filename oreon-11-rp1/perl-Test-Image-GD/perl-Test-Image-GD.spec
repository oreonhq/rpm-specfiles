%global source0_hash fe938a4e0430628a2b13a03716b9706e691c647669a269ec1b4e4400fafa7c1a

Name:           perl-Test-Image-GD
Version:        0.03
Release:        36%{?dist}
Summary:        Module for testing images using GD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Image-GD
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Image-GD-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Exporter)
BuildRequires:  perl(GD)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.47
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Dependencies
# (none)

%description
This module is meant to be used for testing custom graphics. It attempts
to "visually" compare the images, which means that it ignores invisible
differences like color palettes and metadata. It also provides some extra
functions to check the size of the image.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Image-GD-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Image::GD.3*

%changelog
%autochangelog
