%global source0_hash 87572d18ebcf91ca5d28548c77652b0202876a5874cd848a8b90250923b81162

Name:           perl-UNIVERSAL-exports
Version:        0.05
Release:        50%{?dist}
Summary:        Lightweight, universal exporting of variables
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-exports
Source0:        http://backpan.perl.org/authors/id/M/MS/MSCHWERN/UNIVERSAL-exports-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(Exporter::Lite) >= 0.01
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(Exporter::Lite) >= 0.01

# Filter bogus provide for perl(UNIVERSAL) (rpm 4.9 onwards)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(UNIVERSAL\\)
# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter::Lite\\)$

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n UNIVERSAL-exports-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/UNIVERSAL::exports.3pm*

%changelog
%autochangelog
