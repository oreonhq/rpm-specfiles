%global source0_hash c32aa4f309573d7648ab2e416f62b6b20652f2ad9cfd3eec82fd51101fe7310d
%global perlname XML-Entities
Name:      perl-XML-Entities
Version:   1.0002
Release:        1%{?dist}
Summary:        Decode strings with XML entities
License:   GPL-1.0-or-later OR Artistic-1.0-Perl
URL:       https://metacpan.org/release/XML-Entities
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIXTEASE/%{perlname}-%{version}.tar.gz
BuildArch: noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(open)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a mapping from the standard XML entities to their Unicode
characters. A function for decoding is provided. The mapping can be generated
from a DTD file with entity definitions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{perlname}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';' -print
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';' -print
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
