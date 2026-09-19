%global source0_hash 7d5c3c2d4f9b657a8b1dce7f5e2cbbe02ada2e97c72f3a0304bf3c99d084b045

Name:           perl-Term-Animation
Version:        2.6
Release:        51%{?dist}
Summary:        ASCII sprite animation framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Animation
Source0:        https://cpan.metacpan.org/authors/id/K/KB/KBAUCOM/Term-Animation-2.6.tar.gz
# Fix a POD syntax, CPAN RT#115456
Patch0:         Term-Animation-2.6-pod.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Curses)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)

%description
This module provides a framework to produce sprite animations using ASCII art.
Each ASCII 'sprite' is given one or more frames, and placed into the animation
as an 'animation object'. An animation object can have a callback routine that
controls the position and frame of the object.

If the constructor is passed no arguments, it assumes that it is running full
screen, and behaves accordingly. Alternatively, it can accept a curses window
(created with the Curses new win call) as an argument, and will draw into that
window.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Animation-%{version}
%patch -P0 -p0

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes examples README MIGRATION
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
