%global source0_hash ed441ff26d4bd48dd85b582be3db8e1d5daeda24b7592eb4d077bb1b043d2c97

Name:           perl-Acme-Alien-DontPanic2
%global cpan_version 2.7200
Version:        2.720.0
Release:        9%{?dist}
Summary:        Test module for Alien::Base + Alien::Build
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Acme-Alien-DontPanic2
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Acme-Alien-DontPanic2-%{cpan_version}.tar.gz
# Full-arch for files storing architecture-specific paths
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Alien::Build::MB) >= 0.07
BuildRequires:  perl(alienfile)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(dontpanic)
# Run-time
BuildRequires:  perl(Alien::Base) >= 2.72
# Alien::Build::Plugin::Digest::Negotiate not used
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
# Tests
BuildRequires:  perl(Alien::Build) >= 2.72
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Inline) >= 0.56
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Inline::CPP)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien) >= 0.05
Requires:       perl(Alien::Base) >= 2.72
Requires:       pkgconfig(dontpanic)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$

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

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Acme
%{_mandir}/man3/*

%changelog
%autochangelog
