%global source0_hash dcda0371cd11dd3ed71e59bd33a8e432cf51560ec75eb82ca04a2d8975af7b18
Name:           perl-Class-DBI-Plugin
Version:        0.03
Release:        1%{?dist}
Summary:        Abstract base class for Class::DBI plugins
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-Plugin
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-DBI-Plugin-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::DBI) >= 0.9
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Class::DBI::Plugin is an abstract base class for Class::DBI plugins. Its
purpose is to make writing plugins easier. Writers of plugins should be able
to concentrate on the functionality their module provides, instead of having
to deal with the symbol table hackery involved when writing a plugin module.
Only three things must be remembered:

* All methods to be exported are given the "Plugged" attribute. All other
  methods are not exported to the plugged-in class.

* Method calls that are to be sent to the plugged-in class are put in the
  init() method. Examples of these are set_sql(), add_trigger() and so on.

* The class parameter for the init() method and the "Plugged" methods is the
  plugged-in class, not the plugin class.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-Plugin-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
