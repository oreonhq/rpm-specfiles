%global source0_hash a8e3d10f5c4dd307655a7b6ff4002aeb827c44ba5ec41e99c6c46edfcf07aecc
%global _hardened_build 1
Name:             libijs
Summary:        IJS Raster Image Transport Protocol Library
Version:          0.35
Release:        26%{?dist}
License:          AGPL-3.0-or-later
URL:              https://ghostscript.com/
Source0:        https://github.com/ArtifexSoftware/ijs/archive/%{version}.tar.gz#/ijs-%{version}.tar.gz
Patch: 0001-Squash-compiler-warning-in-ijs-code.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
The IJS (InkJet Server) Raster Image Transport Protocol is a library, which
is no longer actively developed, and often other alternatives are used instead.

This library, however, still seem to be useful for Ghostscript application
to be able to connect to the HP IJS server to print on an HP printer.

# === SUBPACKAGES =============================================================

%package devel
Summary:          Header & pkgconfig files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}
BuildRequires:    pkgconfig
BuildRequires: make
%description devel
This subpackage provides /usr/include/ijs/ijs.h header file, as well as ijs.pc
pkgconfig file. Both of these files are useful for development purposes only.

# ---------------

%package doc
Summary:          Documentation for %{name}
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch
%description doc
This subpackage contains PDF documentation with IJS protocol specification,
which is useful for development purposes only.

# === BUILD INSTRUCTIONS ======================================================

# We have to override the folder name, because upstream's archive cotains the
# name 'ijs' (not 'libijs')...
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ijs-%{version}
%oreon_prep
%build

autoreconf -ifv
%configure --disable-static --enable-shared
%make_build
%install
%make_install
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_libdir}/*.la
install -m 0755 -d %{buildroot}%{_docdir}/%{name}
install -m 0644 -p ijs_spec.pdf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libijs-devel -f %{oreon_filedir}/libijs-devel.list
%files -n libijs-doc -f %{oreon_filedir}/libijs-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.35-26
- Prepare for Oreon 11 (RP1)
