%global source0_hash 463e284ec47137e7c425c9691b02a8dec5ce272b58ea1f6359ae8041a239dd0f

Name:           perl-Tk-ToolBar
Version:        0.12
Release:        31%{?dist}
Summary:        Toolbar widget for Perl/Tk
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-ToolBar
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/Tk-ToolBar-%{version}.tar.gz
Patch0:         Tk-ToolBar-0.12-noarch.patch
BuildArch:      noarch
# Build
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tk::Balloon)
BuildRequires:  perl(Tk::BrowseEntry)
# Unused BuildRequires:  perl(Tk::CursorControl)
BuildRequires:  perl(Tk::Frame)
# Unused BuildRequires:  perl(Tk::LabEntry)
BuildRequires:  perl(Tk::widgets)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14
# Optional Requires:       perl(Tk::CursorControl)
Requires:       perl(Tk::LabEntry)

%description
This module implements a dockable toolbar. It is in the same spirit as the
"short-cut" toolbars found in most major applications, such as most web
browsers and text editors (where you find the "back" or "save" and other
shortcut buttons).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-ToolBar-%{version}
find -type f -print0 | xargs -0 sed -i 's/\r$//'
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Package the demo script in doc instead
rm -f %{buildroot}/%{perl_vendorlib}/Tk/toolbar.pl
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README toolbar.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
