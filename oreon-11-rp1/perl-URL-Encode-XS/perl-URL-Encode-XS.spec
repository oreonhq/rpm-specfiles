%global source0_hash d44f416bd3e58e3b3366ab420705da02c7118fc848a97ce089366ea0461fa823

Name:           perl-URL-Encode-XS
Version:        0.03
Release:        37%{?dist}
Summary:        XS implementation of URL::Encode
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URL-Encode-XS
Source0:        https://cpan.metacpan.org/modules/by-module/URL/URL-Encode-XS-%{version}.tar.gz
Patch0:         URL-Encode-XS-0.03-Fix-building-on-Perl-without-.-in-INC.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
# Module
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Dependencies
Requires:       perl(Exporter)
Requires:       perl(XSLoader)

%description
This package implements the original URL::Encode via XS interface. The main
URL::Encode package will use this package automatically if it can find it. 
Do not use this package directly, use URL::Encode instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn URL-Encode-XS-%{version}

# Unbundle inc::Module::Install and friends
rm -rf inc/
sed -i -e '/^inc\// d' MANIFEST

# Fix build on Perl without "." in @INC, CPAN RT#121686
%patch -P0 -p1

# Avoid doc-file dependencies
chmod -c -x dev/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete -print
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes dev/ README
%{perl_vendorarch}/auto/URL/
%{perl_vendorarch}/URL/
%{_mandir}/man3/URL::Encode::XS.3*

%changelog
%autochangelog
