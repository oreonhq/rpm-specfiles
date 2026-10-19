%global source0_hash 81c3d07cf15ce50441f43a82cefd0ac32767c535b5291bcc41bd2311d1337644
Name:		srecord
Version:	1.65.0
Release:        7%{?dist}
Summary:        Manipulate EPROM load files
License:	GPL-3.0-or-later AND LGPL-3.0-or-later
URL:		http://srecord.sourceforge.net/
Source0:        http://downloads.sourceforge.net/srecord/srecord-%{version}-Source.tar.gz
Patch0:		srecord-1.65-fedora.patch
Patch1:		srecord-1.65-fix-header.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  git-core
BuildRequires:  groff
BuildRequires:  libgcrypt-devel
BuildRequires:  netpbm-progs
BuildRequires:  psutils
# /oreon:deps
%description
The SRecord package is a collection of powerful tools for manipulating
EPROM load files.

- The SRecord package understands a number of file formats: Motorola
  S-Record, Intel, Tektronix, Binary.  These file formats may be read
  and written.  Also C array definitions, for output only.

- The SRecord package has a number of tools: srec_cat for copying and
  and converting files, srec_cmp for comparing files and srec_info for
  printing summaries.

- The SRecord package has a number for filters: checksum to add checksums
  to the data, crop to keep address ranges, exclude to remove address
  ranges, fill to plug holes in the data, length to insert the data
  length, maximum to insert the data address maximum, minimum to insert
  the data address minimum, offset to adjust addresses, and split for
  wide data buses and memory striping.

More than one filter may be applied to each input file.  Different filters
may be applied to each input file.  All filters may be applied to all
file formats.

%package devel
Summary:	Development headers and libraries for srecord
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers and libraries for developing applications against
srecord.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}-Source
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/htdocs
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n srecord-devel -f %{oreon_filedir}/srecord-devel.list

%changelog

%autochangelog
