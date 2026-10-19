%global source0_hash e5813e97bbc8f498f034f5e05178489c1be86de015e8da838de59f90f68491e7
Name:           dcfldd
Version:        1.9.3
Release:        1%{?dist}
Summary:        Improved dd, useful for forensics and security
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Copyright-only
URL:            https://github.com/resurrecting-open-source-projects/dcfldd
Source0:        https://github.com/resurrecting-open-source-projects/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
dcfldd is an enhanced version of GNU dd with features useful for forensics
and security. dcfldd has the following additional features:

   * Hashing on-the-fly - dcfldd can hash the input data as it is being
     transferred, helping to ensure data integrity.
   * Status output - dcfldd can update the user of its progress in terms of
     the amount of data transferred and how much longer operation will take.
   * Flexible disk wipes - dcfldd can be used to wipe disks quickly
     and with a known pattern if desired.
   * Image/wipe Verify - dcfldd can verify that a target drive is a
     bit-for-bit match of the specified input file or pattern.
   * Multiple outputs - dcfldd can output to multiple files or disks at
     the same time.
   * Split output - dcfldd can split output to multiple files with more
     configuration possibilities than the split command.
   * Piped output and logs - dcfldd can send all its log data and output
     to commands as well as files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -i
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
