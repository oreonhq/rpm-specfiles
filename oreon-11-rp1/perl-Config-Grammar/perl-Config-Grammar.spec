%global source0_hash a8b3a3a2c9c8c43b92dc401bf2709d6514f15b467fd4f72c48d356335771d6e3
Name:           perl-Config-Grammar
Version:        1.13
Release:        1%{?dist}
Summary:        Grammar-based, user-friendly config parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-Grammar
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSCHWEI/Config-Grammar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Config::Grammar is a module to parse configuration files. The
configuration may consist of multiple-level sections with assignments
and tabular data.  The parsed data will be returned as a hash
containing the whole configuration. Config::Grammar uses a grammar
that is supplied upon creation of a Config::Grammar object to parse
the configuration file and return helpful error messages in case of
syntax errors. Using the makepod method you can generate documentation
of the configuration file format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Grammar-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
