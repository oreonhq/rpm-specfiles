%global source0_hash 34e75071934918d16f02beefd031b925e36091bd9557d9eb8b64411a04951ce3

Name:           perl-Text-xSV
Version:        0.21
Release:        22%{?dist}
Summary:        Read character separated files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Text-xSV
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TILLY/Text-xSV-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
# run requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)

%{?perl_default_filter}

%description
This module is for reading and writing a common variation of character
separated data. The most common example is comma-separated. However that is
far from the only possibility, the same basic format is exported by
Microsoft products using tabs, colons, or other characters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-xSV-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__perl} -Ilib test.pl
# ./Build test

%files
%doc Build Changes README test.csv
%{perl_vendorlib}/Text*
%{_mandir}/man3/Text*

%changelog
%autochangelog
