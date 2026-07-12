%global source0_hash 10c01c000b5aa6e9aaf259c7959b1b199b5c9235f40ccdac93e1d4ab885faab9

Name:           perl-Convert-Color
Version:        0.18
Release:        4%{?dist}
Summary:        Color space conversions and named lookups
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Color
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Convert-Color-%{version}.tar.gz
# Workaround to a source-code trick, which break rpm's perl-module deptracking
Patch0:         Convert-Color-0.09.patch
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(meta) >= 0.008

# For improved testing
BuildRequires:  perl(Test::Pod) >= 1.00

%if 0%{fedora} >= 40
# REGRESSION: dnf5 is unable to BuildRequires: files
# REGRESSION: dnf5 is unable to Requires: files
BuildRequires:  rgb
Requires: rgb
%else
BuildRequires:  /usr/share/X11/rgb.txt
Requires:       /usr/share/X11/rgb.txt
%endif

Provides:       perl(Convert::Color)
Provides:       perl(Convert::Color::RGB)
Provides:       perl(Convert::Color::RGB8)
%description
This module provides conversions between commonly used ways to express
colors. It provides conversions between color spaces such as RGB and HSV,
and it provides ways to look up colors by a name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Convert-Color-%{version}
%patch -P0 -p1

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes examples README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
