%global source0_hash d8939fa4f12bd6b8c043537fd0bf96b055ac3686b9cdd9fa773dca6ae679cb4c
Name:           perl-HTTP-Server-Simple
Version:        0.52
Release:        1%{?dist}
Summary:        Very simple standalone HTTP daemon
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Server-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-Server-Simple-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CGI)
Requires:       perl(POSIX)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
HTTP::Server::Simple is a very simple standalone HTTP daemon with no non-core
module dependencies.  It's ideal for building a standalone http-based UI to
your existing tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Server-Simple-%{version}

# Unbundle inc::Module::Install
rm -rvf inc/
sed -i -e '/^inc\// d' MANIFEST

# Drop bogus exec permissions
chmod -c a-x lib/HTTP/Server/*.pm

# Fix shellbang
perl -pi -e 's|^#!perl\b|#!%{__perl}|' ex/sample_server

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
