%global source0_hash 6df04205747ae35cd62edc9649ab0187f902a56fb16f355cbdbdc7ca3e14b6bd

Summary: Macromolecular coordinate library
Name: mmdb2
Version: 2.0.1
Release: 28%{?dist}
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
URL: ftp://ftp.ccp4.ac.uk/opensource/
Source0: ftp://ftp.ccp4.ac.uk/opensource/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
MMDB is a macromolecular coordinate library, written by Eugene
Krissinel primarily for use by the collaborative computational project
4 (CCP4) group in the United Kingdom.  The Coordinate Library is
designed to assist CCP4 developers in working with coordinate files.

The Library features work with the primary file formats of the Protein
Data Bank (PDB), the PDB file format and the mmCIF file format.

The Library provides various high-level tools for working with
coordinate files, which include not only reading and writing, but also
orthogonal-fractional coordinate transforms, generation of symmetry
mates, editing the molecular structure and some others. The Library is
supposed as a general low-level tool for unifying the
coordinate-related operations.

This package contains the shared library components needed for programs
that have been compiled with the mmdb library. 

%package devel
Summary: Header files and library for developing programs with mmdb
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains libraries and header files needed for program
development using the macromolecular coordinate library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
chmod 644 README COPYING AUTHORS

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README
%{_libdir}/libmmdb2.so.0.0.0
%{_libdir}/libmmdb2.so.0

%files devel
%{_libdir}/libmmdb2.so
%{_includedir}/mmdb2/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
