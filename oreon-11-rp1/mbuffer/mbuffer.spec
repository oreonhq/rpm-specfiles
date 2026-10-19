%global source0_hash 13bab36f39408f7a08fb368913290ad0f117c934bab602094e18fcc123ec5783
Name:           mbuffer
Version:        20260511
Release:        1%{?dist}
Summary:        Measuring Buffer is an enhanced version of buffer
License:        GPL-3.0-or-later
URL:            http://www.maier-komor.de/mbuffer.html
Source0:        http://www.maier-komor.de/software/mbuffer/mbuffer-%{version}.tgz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mhash-devel
BuildRequires:  mt-st
# /oreon:deps
%description
Measuring Buffer is an enhanced version of buffer. It features displayof
throughput, memory-mapped file I/O for huge buffers, and multithreading.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

export ac_cv_search_MD5_Init=no
%configure
%make_build
%install
%make_install
rm -rf %{buildroot}/usr/etc/mbuffer.rc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
