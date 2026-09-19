%global source0_hash 81c3d07cf15ce50441f43a82cefd0ac32767c535b5291bcc41bd2311d1337644

Name:		srecord
Version:	1.65.0
Release:	7%{?dist}
Summary:	Manipulate EPROM load files
License:	GPL-3.0-or-later AND LGPL-3.0-or-later
# see also https://github.com/sierrafoxtrot/srecord
URL:		http://srecord.sourceforge.net/
Source0:	http://downloads.sourceforge.net/srecord/srecord-%{version}-Source.tar.gz
# https://github.com/sharkcz/srecord/tree/fedora-1.65
# - switch to a shared library with a sane name
# - don't install runtime deps
Patch0:		srecord-1.65-fedora.patch
Patch1:		srecord-1.65-fix-header.patch
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	git-core
BuildRequires:	libgcrypt-devel
# for building docs
BuildRequires:	doxygen
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	netpbm-progs
BuildRequires:	psutils

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

%autosetup -p1 -n %{name}-%{version}-Source

%build
%cmake
%cmake_build

%install
%cmake_install

# the generated html docs are huge and unlikely to be used ...
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/htdocs

%check
%ctest

%files
%license LICENSE
%{_defaultdocdir}/%{name}/
%{_bindir}/srec_*
%{_libdir}/lib%{name}.so.%{version}
%{_mandir}/man1/srec_*.1*
%{_mandir}/man3/%{name}*.3*
%{_mandir}/man5/srec_*.5*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
