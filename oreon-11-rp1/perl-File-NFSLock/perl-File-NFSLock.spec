%global source0_hash 61d41599b481164edf9b8becabbef2d23f622a9727f6c18365e92b5782d4fa37
Name:           perl-File-NFSLock
Version:        1.29
Release:        21%{?dist}
Summary:        Perl module to do NFS (or not) locking
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-NFSLock
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBB/File-NFSLock-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Sys::Hostname)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Program based of concept of hard linking of files being atomic across NFS. 
This concept was mentioned in Mail::Box::Locker (which was originally 
presented in Mail::Folder::Maildir). Some routine flow is taken from 
there -- particularly the idea of creating a random local file, hard 
linking a common file to the local file, and then checking the nlink 
status. Some ideologies were not complete (uncache mechanism, shared 
locking) and some coding was even incorrect (wrong stat index). 
File::NFSLock was written to be light, generic, and fast.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-NFSLock-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
chmod a-x examples/lock_test
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
