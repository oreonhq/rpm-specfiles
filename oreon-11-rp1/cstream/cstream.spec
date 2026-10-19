%global source0_hash 6bc06d7c4386fb98d3a91713434c315d9e6d425c91c886281beaa254c0e096e3
Summary:        General-purpose stream-handling tool
Name:      cstream
Version:   4.0.0
Release:        1%{?dist}
License:   MIT
URL:       http://www.cons.org/cracauer/cstream.html
Source0:        http://www.cons.org/cracauer/download/%{name}-%{version}.tar.gz
Patch2:    %{name}-%{version}-Wextra.patch
Patch3:    %{name}-%{version}-double-assignment.patch
Patch5:    %{name}-%{version}-meh.patch
Patch6:    %{name}-%{version}-Werror=tautological-compare.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
cstream filters data streams, much like the UNIX tool dd(1).

It has a more traditional commandline syntax, support for precise
bandwidth limiting and reporting and support for FIFOs.

Data limits and throughput rate calculation will work for files > 4 GB.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P2 -p1 -b .Wextra
%patch -P3 -p1 -b .double-assignment
%patch -P5 -p1 -b .meh
%patch -P6 -p1 -b .Werror=autological-compare

%build

%{configure} INSTALL="%{__install} -p"
%make_build CFLAGS="%{optflags} -Wall -Wextra -Wno-unused-parameter -Werror"
%install
%make_install
%oreon_autofiles main

%check

%{__make} %{?_smp_mflags} check installcheck DESTDIR="%{buildroot}"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
