%global source0_hash 45c77896b2a5a0a45f6202a6f813f437ff8b283f84a1c60d0c4f3730802af3a2

Name:           perl-LockFile-Simple
Version:        0.208
Release:        35%{?dist}
Summary:        Simple file locking scheme
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LockFile-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/LockFile/LockFile-Simple-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(vars)
# Test Suite
# (no additioanl dependencies)
# Dependencies
BuildRequires:  perl(Carp)

%description
This simple locking scheme is not based on any file locking system calls
such as flock() or lockf() but rather relies on basic file system
primitives and properties, such as the atomicity of the write() system
call. It is not meant to be exempt from all race conditions, especially
over NFS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LockFile-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/LockFile/
%{_mandir}/man3/LockFile::Simple.3*

%changelog
%autochangelog
