%global source0_hash 07d89418a0fea13c528a4887d004db3b56e02345686fda50c17dc33f6b491768
Name:		perl-Apache-Session-Browseable
Version:	1.3.18
Release:        1%{?dist}
Summary:        Add index and search methods to Apache::Session
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Apache-Session-Browseable
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIMARD/Apache-Session-Browseable-%{version}.tar.gz
Patch0:		Apache-Session-Browseable-1.3.6-synopsis-cafile.patch
BuildArch:	noarch
Requires:	perl(MIME::Base64)
Requires:	perl(Redis)
Requires:	perl(Storable)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Apache::Session)
BuildRequires:  perl(Apache::Session::Generate::MD5)
BuildRequires:  perl(Apache::Session::Lock::File)
BuildRequires:  perl(Apache::Session::Lock::Null)
BuildRequires:  perl(Apache::Session::Serialize::Base64)
BuildRequires:  perl(Apache::Session::Serialize::Storable)
BuildRequires:  perl(Apache::Session::Serialize::Sybase)
BuildRequires:  perl(Apache::Session::Store::DBI)
BuildRequires:  perl(Apache::Session::Store::File)
BuildRequires:  perl(Apache::Session::Store::Informix)
BuildRequires:  perl(Apache::Session::Store::MySQL)
BuildRequires:  perl(Apache::Session::Store::Oracle)
BuildRequires:  perl(Apache::Session::Store::Postgres)
BuildRequires:  perl(Apache::Session::Store::Sybase)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Redis)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  valkey
# /oreon:deps
%description
A virtual Apache::Session back-end providing some class methods to manipulate
all sessions and add the capability to index some fields to make re-search
faster.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-Session-Browseable-%{version}

# Fix certificate bundle location in SYNOPSIS
%patch -P 0

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

valkey-server --port 6379 --pidfile /tmp/valkey.pid &
./Build test
kill $(cat /tmp/valkey.pid)
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
