%global source0_hash 60559acecebf707afce0f6250f32a8e17c24b2d13c01ffd26f9dc28860fccd9d

Name:           perl-Tk-CursorControl
Version:        0.4
Release:        40%{?dist}
Summary:        Manipulate the mouse cursor programmatically
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-CursorControl
Source0:        https://cpan.metacpan.org/authors/id/D/DU/DUNNIGANJ/Tk-CursorControl-%{version}.tar.gz
# don't install cursor.pl demo - add to docs instead
Patch0:         perl-Tk-CursorControl-no-demos.patch
# disable interactive tests (reenable --with interactive-tests)
Patch1:         perl-Tk-CursorControl-no-interactive-test.patch
%bcond_with     interactive_tests
BuildArch:      noarch
# Build
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tk) >= 800.015

%{?perl_default_filter}

%description
This module offers a Tk programmer the functionality of warping, moving,
confining or hiding a mouse cursor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-CursorControl-%{version}
%patch -P0 -p1
%if %{without interactive_tests}
%patch -P1 -p1
%endif

# strip CRLF
find -type f -print0 | xargs -0 sed -i 's/\r$//'

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README demos/cursor.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
