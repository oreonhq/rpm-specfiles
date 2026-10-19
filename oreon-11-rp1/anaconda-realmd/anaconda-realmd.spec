%global source0_hash d8525bb25b7849c5f8c57b288014b3cebb11e542700c73d74629f839c9af8c9b
Name:		anaconda-realmd
Version:	0.2
Release:        1%{?dist}
Summary:        Anaconda addon which interacts with realmd to join domains
License:	GPL-2.0-or-later
URL:		http://git.fedorahosted.org/cgit/anaconda-realmd.git/
Source0:        https://fedorahosted.org/releases/a/n/anaconda-realmd/anaconda-realmd-%{version}.tgz
BuildArch:	noarch
Requires:	anaconda >= 19
Requires:	realmd >= 0.12
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
This is a addon for Anaconda which allows use of 'realm' commands in the
kickstart file to join domains.

%define _hardened_build 1

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
