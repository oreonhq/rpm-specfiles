%global source0_hash 0598b82aa7117ed46117638bb675c02789ff2fe7e674e87e35e681a1d6924093
Name:           perl-Lingua-Stem-Snowball
Version:        0.952
Release:        1%{?dist}
Summary:        Perl interface to Snowball stemmers
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND BSD-3-Clause
URL:            https://metacpan.org/release/Lingua-Stem-Snowball
Source0:        https://cpan.metacpan.org/modules/by-module/Lingua/Lingua-Stem-Snowball-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description 
Stemming reduces related words to a common root form -- for instance,
"horse", "horses", and "horsing" all become "hors". Most commonly,
stemming is deployed as part of a search application, allowing
searches for a given term to match documents which contain other forms
of that term.

This module is very similar to Lingua::Stem -- however, Lingua::Stem
is pure Perl, while Lingua::Stem::Snowball is an XS module which
provides a Perl interface to the C version of the Snowball
stemmers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-Stem-Snowball-%{version}

%build

perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
