%global source0_hash c6b801db8081ef822761b1a56e5a82bdf0535d0d6e62f2dd2424d1c66fe83013

# Run optional test
%bcond_without perl_DBD_Multi_enables_optional_test

Name:       perl-DBD-Multi
Version:    1.02
Release:    24%{?dist}
# See Build.PL
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    DB Proxy with fail-over and load balancing
Source:     https://cpan.metacpan.org/authors/id/D/DW/DWRIGHT/DBD-Multi-%{version}.tar.gz
Url:        https://metacpan.org/release/DBD-Multi
BuildArch:  noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Fast) >= 0.19
BuildRequires:  perl(DBD::File)
BuildRequires:  perl(DBI)
BuildRequires:  perl(List::Util) >= 1.18
BuildRequires:  perl(Sys::SigAction) >= 0.10
BuildRequires:  perl(vars)
# Test-only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite) >= 1.09
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Exception) >= 0.21
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP) >= 2.19
%if %{with perl_DBD_Multi_enables_optional_test}
# Optional tests
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(Test::Pod) >= 1.14
%endif
# not picked up automatically
Requires:       perl(Class::Accessor::Fast)

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

%check
./Build test

%files
%doc Changes README.md TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
