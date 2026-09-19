%global source0_hash aa65390e0120dfe98e8a2c510a81adc5d3e42efa3e13d54e85467303d911bf31

Name:           perl-Object-MultiType
Version:        0.05
Release:        52%{?dist}
Summary:        Perl Objects as Hash, Array, Scalar, Code and Glob at the same time
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-MultiType
Source0:        https://cpan.metacpan.org/authors/id/G/GM/GMPASSOS/Object-MultiType-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  dos2unix
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
Requires:       perl(warnings)

%{?perl_default_filter}

%description
This module return an object that works like a Hash, Array, Scalar, Code
and Glob object at the same time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-MultiType-%{version}

%build
dos2unix -q -k README Changes
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
