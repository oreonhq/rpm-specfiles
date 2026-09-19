%global source0_hash 5041d08dc276c45df5e98173097bc84eadcca85354b605c1f439b60e0e9f093e

Name:           perl-Class-Forward
Version:        0.100006
Release:        35%{?dist}
Summary:        Namespace Dispatch and Resolution
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Class-Forward
Source0:        https://cpan.metacpan.org/authors/id/A/AW/AWNCORP/Class-Forward-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Class::Forward is designed to resolve Perl namespaces from shorthand (which
is simply a file-path-like specification). Class::Forward can also be used
to dispatch method calls using said shorthand. See the included exported
functions for examples on how this can be used.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Forward-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
