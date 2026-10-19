%global source0_hash 34c4ddf91fc93d1090d86da14df706d175b1610c67372c01e12ce9555d4dd1dc
Name:           perl-Guard
Version:        1.023
Release:        1%{?dist}
Summary:        Safe cleanup blocks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Guard
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Guard-%{version}.tar.gz
Requires:       perl(Exporter)
Requires:       perl(warnings)
Requires:       perl(XSLoader)
%{?perl_default_filter}
Provides:       perl(Guard)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
