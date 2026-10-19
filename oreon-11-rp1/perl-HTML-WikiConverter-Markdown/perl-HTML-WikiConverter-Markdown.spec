%global source0_hash 23a50793c8643a2ceab41091f0d4aa5bde337d9e9f88c9e2b857667d98027f60
Name:           perl-HTML-WikiConverter-Markdown
Version:        0.06
Release:        32%{?dist}
Summary:        Convert HTML to Markdown markup
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-WikiConverter-Markdown
Source0:        https://cpan.metacpan.org/authors/id/J/JF/JFEARN/HTML-WikiConverter-Markdown-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(HTML::WikiConverter) >= 0.67
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::WikiConverter)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module contains rules for converting HTML into Markdown markup. You
should not use this module directly; HTML::WikiConverter is the entry point
for html->wiki conversion (eg, see synopsis above). See HTML::WikiConverter
for additional usage details.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-WikiConverter-Markdown-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
