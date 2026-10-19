%global source0_hash cdebce7e9493f5cd8f77fbb74254f7687763ed839f285cf0546b240d3b2fdc54
Name:           perl-HTML-HTML5-Entities
Version:        0.004
Release:        1%{?dist}
Summary:        Drop-in replacement for HTML::Entities with HTML5 support
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-1.0-or-later OR Artistic-1.0-Perl OR LicenseRef-Callaway-CC-BY-SA)
URL:            https://metacpan.org/release/HTML-HTML5-Entities
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Entities-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a drop-in replacement for HTML::Entities Perl module. This replacement
provides the character entities defined in HTML5.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-HTML5-Entities-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
