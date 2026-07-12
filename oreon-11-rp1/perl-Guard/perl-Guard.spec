%global source0_hash 34c4ddf91fc93d1090d86da14df706d175b1610c67372c01e12ce9555d4dd1dc

Name:           perl-Guard
Version:        1.023
Release:        36%{?dist}
Summary:        Safe cleanup blocks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Guard
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Guard-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Test Suite
# (no additional dependencies)
# Dependencies
Requires:       perl(Exporter)
Requires:       perl(warnings)
Requires:       perl(XSLoader)

# Avoid provides from private shared objects
%{?perl_default_filter}

Provides:       perl(Guard)
%description
This module implements so-called "guards". A guard is something (usually an
object) that "guards" a resource, ensuring that it is cleaned up when expected.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Guard-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorarch}/auto/Guard/
%{perl_vendorarch}/Guard.pm
%{_mandir}/man3/Guard.3*

%changelog
%autochangelog
