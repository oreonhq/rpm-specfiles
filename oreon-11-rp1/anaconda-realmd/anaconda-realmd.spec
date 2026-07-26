%global source0_hash 1bcaadf02fecb5c93d7d0c26e043a49dbbbd70eb8a20d9d636ca8a663f8c4597

Name:		anaconda-realmd
Version:	0.2
Release:	28%{?dist}
Summary:	Anaconda addon which interacts with realmd to join domains
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://git.fedorahosted.org/cgit/anaconda-realmd.git/
Source0:	https://fedorahosted.org/releases/a/n/anaconda-realmd/anaconda-realmd-%{version}.tgz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires: make
Requires:	anaconda >= 19
Requires:	realmd >= 0.12

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

%files
%dir %{_datadir}/anaconda/addons/org_fedora_realm/
%dir %{_datadir}/anaconda/addons/org_fedora_realm/ks
%{_datadir}/anaconda/addons/org_fedora_realm/ks/realm.py*
%doc COPYING ChangeLog NEWS README

%changelog
%autochangelog
