%global source0_hash d7e9d5353849d23a4994f532662ba9656c5a60aad9ec5d7d0c378c69d1d84017
Name:           perl-Data-ObjectDriver
Version:        0.26
Release:        1%{?dist}
Summary:        Simple, transparent data interface, with caching
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Data-ObjectDriver
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIXAPART/Data-ObjectDriver-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}%{perl_vendorlib}/Data/ObjectDriver/Driver/DBD/Oracle.pm
# oreon:deps
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
# /oreon:deps
%description
Data::ObjectDriver is an object relational mapper, meaning that it maps object-
oriented design concepts onto a relational database.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-ObjectDriver-%{version}

%build

/usr/bin/perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
