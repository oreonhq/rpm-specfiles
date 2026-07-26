%global source0_hash e6bebbc58408231fd1317db9102449b3e7da4fa437e79f637382d36313efd011

Name:           perl-Unicode-Stringprep
Summary:        Preparation of Internationalized Strings (RFC 3454)
Version:        1.105
Release:        34%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Unicode-Stringprep
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Unicode-Stringprep-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
This module implements the stringprep framework for preparing Unicode
text strings in order to increase the likelihood that string input and
string comparison work in ways that make sense for typical users
throughout the world. The stringprep protocol is useful for protocol
identifier values, company and personal names, internationalized domain
names, and other text strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Unicode-Stringprep-%{version}

# Convert the README file to UTF-8
iconv -f ISO_8859-1 -t UTF8 README > README.utf8
mv README.utf8 README

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes eg README
%license LICENSE
%{perl_vendorlib}/Unicode
%{_mandir}/man3/Unicode::Stringprep*3pm*

%changelog
%autochangelog
