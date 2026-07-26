%global source0_hash 30db7a237dd26022216fffb970b985285347130b36923c711aa0956adcb47e9f

Name:           perl-MooseX-RelatedClassRoles
Version:        0.004
Release:        40%{?dist}
Summary:        Apply roles to a class related to yours
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-RelatedClassRoles
Source0:        https://cpan.metacpan.org/authors/id/H/HD/HDP/MooseX-RelatedClassRoles-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Class::MOP) >= 0.80
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose) >= 0.73
BuildRequires:  perl(MooseX::Role::Parameterized) >= 0.04
BuildRequires:  perl(Test::More)
Requires:       perl(Class::MOP) >= 0.80
Requires:       perl(Moose) >= 0.73

%{?perl_default_filter}

%description
Frequently, you have to use a class that provides some foo_class accessor
or attribute as a method of dependency injection. Use this role when you'd
rather apply roles to make your custom foo_class instead of manually
setting up a subclass.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-RelatedClassRoles-%{version}

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
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
