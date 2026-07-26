%global source0_hash 86729cce634cd057f9d2774d9b55912fe96ff2f68b029691e6807c7a9b397d71

Name:           perl-CatalystX-InjectComponent
Version:        0.025
Release:        37%{?dist}
Summary:        Inject components into your Catalyst application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CatalystX-InjectComponent
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROKR/CatalystX-InjectComponent-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80000
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Devel::InnerPackage)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
Requires:       perl(Catalyst::Runtime) >= 5.80000
Requires:       perl(parent)

%{?perl_default_filter}

%description
CatalystX::InjectComponent will inject Controller, Model, and View components
into your Catalyst application at setup (run)time. It does this by creating a
new package on-the-fly, having that package extend the given component, and
then having Catalyst setup the new component (via ->setup_component).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CatalystX-InjectComponent-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
