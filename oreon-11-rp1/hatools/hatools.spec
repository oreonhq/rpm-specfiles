%global source0_hash 2bfcb19b5f004f7c8286a86b67304837b61d5a9d68f5568e9e7110d5524299fb

Name:		hatools
Version:	2.14
Release:	30%{?dist}
Summary:	Improved shell scripting in High Availability environment

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://fatalmind.com/software/hatools/
Source0:	http://fatalmind.com/software/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires: make
%description
The HA-Tools provide some programs to improve shell scripting in a High
Availability environment.

The halockrun program provides a simple and reliable way to implement a locking
in shell scripts. A typical usage for halockrun is to prevent cronjobs to run
simultanously. halockrun uses a lock on a file via fcntl(2) which ensures the
release of the lock even if the process gets killed via SIGKILL.

The hatimerun program provides a time-out mechanism which can be used from
shell scripts. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
