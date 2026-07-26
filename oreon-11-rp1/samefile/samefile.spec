%global source0_hash 45eabde7a8c20cdc3a59d56c72e29acd35f3c77c6d3bb1d1ca10ea202869e599

Name:		samefile
Version:	2.14
Release:	27%{?dist}
Summary:	Command-line utility to find identical files on the file system

License:	BSD-2-Clause
URL:		http://www.schweikhardt.net/samefile/
Source0:	http://www.schweikhardt.net/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc

%description
The samefile utility finds files with identical contents, independent of file 
name. This program is for you if you are notoriously low on disk space, keep 
exceeding your disk quota, pay for your storage by the megabyte, run any kind 
of file server, need to reduce the size of your backups, or just want to get 
a feeling for how much redundant files are there on your system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make test

%files
%doc README ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
