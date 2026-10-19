%global source0_hash 87572d18ebcf91ca5d28548c77652b0202876a5874cd848a8b90250923b81162
Name:           perl-UNIVERSAL-exports
Version:        0.05
Release:        50%{?dist}
Summary:        Lightweight, universal exporting of variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-exports
Source0:        http://backpan.perl.org/authors/id/M/MS/MSCHWERN/UNIVERSAL-exports-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter::Lite) >= 0.01
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(UNIVERSAL\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter::Lite\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter::Lite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
