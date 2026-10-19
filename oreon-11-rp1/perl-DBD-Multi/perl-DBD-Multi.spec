%global source0_hash c6b801db8081ef822761b1a56e5a82bdf0535d0d6e62f2dd2424d1c66fe83013
%bcond_without perl_DBD_Multi_enables_optional_test
Name:       perl-DBD-Multi
Version:    1.02
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        DB Proxy with fail-over and load balancing
Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWRIGHT/DBD-Multi-%{version}.tar.gz
Url:        https://metacpan.org/release/DBD-Multi
BuildArch:  noarch
%if %{with perl_DBD_Multi_enables_optional_test}
%endif
Requires:       perl(Class::Accessor::Fast)
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(DBD::File)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sys::SigAction)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This software manages multiple database connections for fail-overs and also
simple load balancing. It acts as a proxy between your code and your
database connections, transparently choosing a connection for each query,
based on your preferences and present availability of the DB server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBD-Multi-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
