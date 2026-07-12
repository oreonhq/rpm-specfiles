%global source0_hash e3c0b56af99867ff9d7ca5d4c50390a982ec5d90f5b034e5b069960df4b1d39b

Name:           perl-ColorThemeBase-Static
Version:        0.009
Release:        4%{?dist}
Summary:        Base class for color theme modules with static list of items
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ColorThemeBase-Static/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/ColorThemeBase-Static-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Color::RGB::Util) >= 0.607
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Color::RGB::Util) >= 0.607

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Color::RGB::Util\\)\\s*$

Provides:       perl(ColorThemeBase::Static)
Provides:       perl(ColorThemeBase::Static::FromStructColors)
Provides:       perl(ColorTheme::Test::Static)
%description
This is base class for color theme modules with static list of items (from
object's colors key).
This class is now alias for ColorThemeBase::Static::FromStructColors. You
can use that class directly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ColorThemeBase-Static-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
