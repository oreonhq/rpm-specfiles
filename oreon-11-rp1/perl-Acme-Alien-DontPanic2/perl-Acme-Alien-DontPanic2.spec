%global source0_hash ed441ff26d4bd48dd85b582be3db8e1d5daeda24b7592eb4d077bb1b043d2c97
Name:           perl-Acme-Alien-DontPanic2
%global cpan_version 2.7200
Version:        2.720.0
Release:        9%{?dist}
Summary:        Test module for Alien::Base + Alien::Build
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Acme-Alien-DontPanic2
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Acme-Alien-DontPanic2-%{cpan_version}.tar.gz
%global debug_package %{nil}
Requires:       perl(Alien::Base) >= 2.72
Requires:       pkgconfig(dontpanic)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Build)
BuildRequires:  perl(Alien::Build::MB)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Inline::CPP)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(dontpanic)
# /oreon:deps
%description
This module is a toy module to test the efficacy of the Alien::Base system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Acme-Alien-DontPanic2-%{cpan_version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
