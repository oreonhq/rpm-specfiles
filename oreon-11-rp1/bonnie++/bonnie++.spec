%global source0_hash df79dbef41bc9afdb81f8c637431f227955abfde45e78329feca13b872570217
Name:           bonnie++
Version:        2.00a
Release:        1%{?dist}
Summary:        Filesystem and disk benchmark & burn-in suite
License:        GPL-2.0-only
URL:            http://www.coker.com.au/bonnie++/
Source0:        http://www.coker.com.au/bonnie++/experimental/bonnie++-%{version}.tgz
Patch0:         %{name}-makefile.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
bonnie++ filesystem and disk benchmark suite aggressively reads & writes
in various ways on your filesystem then outputs useful benchmark performance
data.  bonnie++ is also useful as a hardware, disk, and filesystem stability
test, exposing some types of hardware or kernel failures that would otherwise
be difficult to detect.

Do not leave bonnie++ installed on a production system.  Use only while you
test servers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-stripping
%make_build CFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
