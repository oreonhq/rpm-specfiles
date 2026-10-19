%global source0_hash d7f3cdaf44ba0226f3d5163f13e7bf6be5bc47534db774f5156eee3ffa9f84e4
%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName HarfBuzz-Shaper
Name: perl-%{FullName}
Summary:        Access to a small subset of the native HarfBuzz library
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 0.033
Release:        1%{?dist}
Source0:        %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  harfbuzz-devel
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(charnames)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HarfBuzz::Shaper is a perl module that provides access to a small
subset of the native HarfBuzz library.

The subset is suitable for typesetting programs that need to deal with
complex languages like Devanagari.

This module is intended to be used with module L<Text::Layout>.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{FullName}-%{version}

%build

env INCHS=%{with hbinc} \
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test VERBOSE=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
