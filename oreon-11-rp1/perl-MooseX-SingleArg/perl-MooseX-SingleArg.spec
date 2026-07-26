%global source0_hash 299685454a8f60e040bc1c8b2cb8b531d73ab36cf3f9f1d56309a47754c90fdc

Name:           perl-MooseX-SingleArg
Version:        0.09
Release:        21%{?dist}
Summary:        No-fuss instantiation of Moose objects using a single argument
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/MooseX-SingleArg/
Source0:        http://www.cpan.org/modules/by-module/MooseX/MooseX-SingleArg-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose) >= 1.23
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test2::V0) >= 0.000094
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(warnings)

%description
This module allows Moose instances to be constructed with a single
argument. Your class or role must use this module and then use the
single_arg sugar to declare which attribute will be assigned the single
argument value.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-SingleArg-%{version}

%build
%{__perl} Build.PL --prefix=%{_prefix} --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes cpanfile META.json README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
