%global source0_hash f3f971cd677c4a0c0668cb369002c581d305050b3b0411e18dd3cb9cc270d14a
%global debug_package %{nil}
Name:           ncrack
Version:        0.7
Release:        1%{?dist}
Summary:        A high-speed network auth cracking tool
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            http://nmap.org/ncrack/
Source0:        http://nmap.org/ncrack/dist/%{name}-%{version}.tar.gz
Patch0:         https://github.com/nmap/ncrack/commit/bdcd5d6a0c9ed0b21de33d7bfe34c0f43ced8edd.patch
Patch1:         https://github.com/nmap/ncrack/commit/9232958b35a6f5118049f252814a26bbe21783d6.patch
Patch2:         https://github.com/nmap/ncrack/pull/99.patch
Patch3:		ncrack-0.7-fedora-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Ncrack is a high-speed network authentication cracking tool. It was
built to help companies secure their networks by proactively testing
all their hosts and networking devices for poor passwords. Security
professionals also rely on Ncrack when auditing their clients. Ncrack
was designed using a modular approach, a command-line syntax similar to
Nmap and a dynamic engine that can adapt its behaviour based on network
feedback. It allows for rapid, yet reliable large-scale auditing of
multiple hosts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ivf
export CFLAGS="${RPM_OPT_FLAGS} -fcommon"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
