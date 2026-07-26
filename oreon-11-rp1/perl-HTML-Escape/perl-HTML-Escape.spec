%global source0_hash 5a5eef896500d1ea6c24a9085ecfbe9a43abee68cfc66c03f889d2a2cb689a5d

Name:           perl-HTML-Escape
Version:        1.11
Release:        16%{?dist}
Summary:        Extremely fast HTML escape
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Escape
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTML-Escape-%{version}.tar.gz
BuildRequires:  findutils
# lib/HTML/ppport.h includes <limits.h>
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# Devel::PPPort not used
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.4005
# Module::Build::Pluggable::PPPort not used
BuildRequires:  perl(strict)
# Test::Requires not used
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More) >= 0.98
# XSLodaer is optional but highly recommended as we deliver the XS
# implementation in the same package.
Requires:       perl(XSLoader)

%description
This Perl module escapes HTML's special characters. It's the same as PHP's
htmlspecialchars.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Escape-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
/usr/bin/find $RPM_BUILD_ROOT -type f -name '*.bs' -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/HTML*
%{_mandir}/man3/*

%changelog
%autochangelog
