%global source0_hash 8e66374ade8b447ba94d276616973ef8a249e5b6258b81662142daa712329d53

Name:           perl-String-Dirify
Version:        1.03
Release:        30%{?dist}
Summary:        Convert a string into a directory name
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/String-Dirify
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/String-Dirify-%{version}.tgz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module allows you to convert a string (possibly containing high ASCII
characters, and even HTML) into another, lower-cased, string which can be
used as a directory name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Dirify-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/String*
%{_mandir}/man3/String*

%changelog
%autochangelog
