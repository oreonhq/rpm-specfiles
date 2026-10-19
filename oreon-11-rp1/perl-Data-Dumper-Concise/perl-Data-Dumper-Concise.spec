%global source0_hash a6c22f113caf31137590def1b7028a7e718eface3228272d0672c25e035d5853
Name:           perl-Data-Dumper-Concise
Summary:        A convenient way to reproduce a set of Dumper options
Version:        2.023
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Data-Dumper-Concise-%{version}.tar.gz
URL:            https://metacpan.org/release/Data-Dumper-Concise
BuildArch:      noarch
Requires:       perl(Devel::ArgNames)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::ArgNames)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module always exports a single function, Dumper, which can be
called with an array of values to dump those values or with no arguments
to return the Data::Dumper object it has created.  It exists,
fundamentally, as a convenient way to reproduce a set of Dumper options
that we've found ourselves using across large numbers of applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Dumper-Concise-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
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
