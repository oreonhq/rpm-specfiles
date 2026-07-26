%global source0_hash 1c8129a65d8ee81f47699958eeed1b774155343b5911638ffe89ec54b51d6575

Name: nfsometer		
Version: 1.9
Release: 29%{?dist}
Summary: NFS Performance Framework Tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later 
URL: http://wiki.linux-nfs.org/wiki/index.php/NFSometer
Source0: http://www.linux-nfs.org/~dros/nfsometer/releases/%{name}-%{version}.tar.gz 
Patch001: nfsometer_py3.patch

BuildArch: noarch
BuildRequires: python3-setuptools
BuildRequires: python3-numpy
BuildRequires: python3-matplotlib
BuildRequires: python3-mako
BuildRequires: python3-devel
Requires: nfs-utils 
Requires: python3-matplotlib
Requires: python3-numpy
Requires: python3-mako
Requires: filebench
Requires: time
Requires: git

%description
NFSometer is a performance measurement framework for running workloads and 
reporting results across NFS protocol versions, NFS options and Linux 
NFS client implementations. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P001 -p1

%build
python3 setup.py build

%install
python3 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/*/*
#For noarch packages: sitelib
%{python3_sitelib}/*

%changelog
%autochangelog
