%global source0_hash a3a97c1bb6fa441083f901ec325be9f0625fd603dde19309f79c61584691b119

Name:           perl-Data-Dump-Color
Version:        0.251
Release:        3%{?dist}
Summary:        Like Data::Dump, but with color
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Data-Dump-Color
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Data-Dump-Color-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
# runtime requirements
BuildRequires:  perl(ColorThemeBase::Static::FromStructColors) >= 0.006
BuildRequires:  perl(ColorThemeUtil::ANSI)
BuildRequires:  perl(Data::Dump::FilterContext)
BuildRequires:  perl(Data::Dump::Filtered)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Load::Util) >= 0.004
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util::LooksLikeNumber)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(Data::Dump::Filtered)
Requires:       perl(Data::Dump::FilterContext)
Requires:       perl(MIME::Base64)

%description
This module aims to be a drop-in replacement for Data::Dump. It adds colors
to dumps. For more information, see Data::Dump. This documentation explains
what's different between this module and Data::Dump.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Dump-Color-%{version}
/usr/bin/chmod +x share/examples/*.pl
/usr/bin/perl -pi -e 's|^#!/usr/bin/env ?perl|#!/usr/bin/perl|' share/examples/example2.pl

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
