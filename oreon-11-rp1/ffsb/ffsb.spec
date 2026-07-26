%global source0_hash e5867692aae8c9bfbcdc774599022289c4d89c1d90f4dd7101fb9865ac773c71

Name:		ffsb
Version:	6.0
Release:	0.33.rc2%{?dist}
Summary:	The Flexible Filesystem Benchmark

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/ffsb
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}-rc2.tar.bz2
BuildRequires:	gcc
BuildRequires: make

Patch0:		getu32random.patch
Patch1:		ffsb-c99.patch

%description
The Flexible Filesystem Benchmark (FFSB) is a cross-platform filesystem
performance measurement tool. It uses customizable profiles to measure
of different workloads, and it supports multiple groups of threads
across multiple filesystems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ffsb-6.0-rc2
%patch -P0 -p1
%patch -P1 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# Odd leftover in the tarball...
rm -f examples/profile_smallfile_reads~

%files
%doc AUTHORS COPYING README examples
%{_bindir}/ffsb

%changelog
%autochangelog
