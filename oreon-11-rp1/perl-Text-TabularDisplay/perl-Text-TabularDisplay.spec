%global source0_hash eb0990fafa56b667f23db764bdda5a4dc5f4b1ddc4b1383aa5eed6f22ed186e8

Name:           perl-Text-TabularDisplay
Version:        1.38
Release:        33%{?dist}
Summary:        Display text in formatted table output
# see TabularDisplay.pm's header
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://metacpan.org/release/Text-TabularDisplay
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DARREN/Text-TabularDisplay-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)

%description
Text::TabularDisplay simplifies displaying textual data in a table. The
output is identical to the columnar display of query results in the MySQL
text monitor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-TabularDisplay-%{version}
chmod -c -x t/* examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=true
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc COPYING README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
