%global source0_hash 20587c4d86241f1db68a082b45d26a16cc7d99c668a37ac47735945f647b054f
Name:           perl-DBIx-POS
Version:        0.03
Release:        1%{?dist}
Summary:        Define a dictionary of SQL statements in a POD dialect (POS)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-POS
Source0:        https://cpan.metacpan.org/authors/id/M/MD/MDORMAN/DBIx-POS-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DBIx-POS subclasses Pod::Parser to define a POD dialect for writing a SQL
dictionary for an application, and uses code from Class::Singleton to make
the resulting structure easily accessible.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-POS-%{version}

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
