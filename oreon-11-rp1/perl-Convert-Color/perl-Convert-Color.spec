%global source0_hash 10c01c000b5aa6e9aaf259c7959b1b199b5c9235f40ccdac93e1d4ab885faab9
Name:           perl-Convert-Color
Version:        0.18
Release:        1%{?dist}
Summary:        Color space conversions and named lookups
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Color
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Convert-Color-%{version}.tar.gz
Patch0:         Convert-Color-0.09.patch
BuildArch:      noarch
Requires:       /usr/share/X11/rgb.txt
Provides:       perl(Convert::Color)
Provides:       perl(Convert::Color::RGB)
Provides:       perl(Convert::Color::RGB8)
# oreon:deps
BuildRequires:  /usr/share/X11/rgb.txt
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(meta)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
