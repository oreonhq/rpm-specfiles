%global source0_hash 0e22278717aceb40d16028899a12225e8c10bd3341de143a7685d4e86d2ace23

Name:           perl-JSON-Pointer
Version:        0.07
Release:        30%{?dist}
Summary:        Perl implementation of JSON Pointer
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-Pointer
Source0:        https://cpan.metacpan.org/authors/id/Z/ZI/ZIGOROU/JSON-Pointer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(Carp) >= 1.20
BuildRequires:  perl(Class::Accessor::Lite) >= 0.05
BuildRequires:  perl(Clone) >= 0.36
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON) >= 2.53
BuildRequires:  perl(overload)
BuildRequires:  perl(URI::Escape) >= 3.31
# Tests:
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Carp) >= 1.20
Requires:       perl(Class::Accessor::Lite) >= 0.05
Requires:       perl(Clone) >= 0.36
Requires:       perl(JSON) >= 2.53
Requires:       perl(URI::Escape) >= 3.31

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Carp|Class::Accessor::Lite|Clone|JSON|URI::Escape)\\)$

%description
This library is implemented JSON Pointer draft version 9
<http://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-09> and some
useful operators from JSON Patch draft version 10
<http://tools.ietf.org/html/draft-ietf-appsawg-json-patch-10>. JSON Pointer is
available to identify a specified value, and it is similar to XPath. Please
see the both of specifications for details.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-Pointer-%{version}
# Remove bundled modules
rm -rf inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
