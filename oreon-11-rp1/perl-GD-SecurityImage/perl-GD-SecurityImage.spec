%global source0_hash 3dde24d9acba951cdde5b569d1e42cad946cfdb51280e4469f336fd5fe0c8ea6

Name:           perl-GD-SecurityImage
Version:        1.75
Release:        22%{?dist}
Summary:        Security image (captcha) generator
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/GD-SecurityImage
Source0:        https://cpan.metacpan.org/authors/id/B/BU/BURAK/GD-SecurityImage-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(GD) >= 2.45
BuildRequires:  perl(Image::Magick) >= 6.66
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)

%{?perl_default_filter}

%description
This module gives you a basic interface to create "security images". Most
internet software use these in their registration screens to block robot
programs (which may register tons of fake member accounts). This module
gives you a basic interface to create such an image.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GD-SecurityImage-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
AUTHOR_TESTING=1 RELEASE_TESTING=1 make test

%files
%doc Changes eg StayPuft.ttf
%license LICENSE
%{perl_vendorlib}/GD*
%{_mandir}/man3/GD*

%changelog
%autochangelog
