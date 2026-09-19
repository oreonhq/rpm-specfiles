%global source0_hash c103a19cf99801489ce23e4da86a5f9df79f032f1f1c71b8130d0d3ff96e6304

Name:           perl-HTML-SimpleParse
Version:        0.12
Release:        48%{?dist}
Summary:        Bare-bones HTML parser
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/HTML-SimpleParse
Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/HTML-SimpleParse-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)

%description
This module is a simple HTML parser. It is similar in concept to
HTML::Parser, but it differs from HTML::TreeBuilder in a couple of
important ways.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-SimpleParse-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/HTML*
%{_mandir}/man3/HTML*

%changelog
%autochangelog
