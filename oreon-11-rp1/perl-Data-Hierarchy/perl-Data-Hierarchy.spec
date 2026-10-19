%global source0_hash b3a8e62b53e29f71dd5989aeef99fbfaf1f4b6e272a06800381360d59e9fd9ed
Name:           perl-Data-Hierarchy
Version:        0.34
Release:        1%{?dist}
Summary:        Handle data in a hierarchical structure
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Hierarchy
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Hierarchy-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Data::Hierarchy provides a simple interface for manipulating inheritable
data attached to a hierarchical environment (like filesystem).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Hierarchy-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
