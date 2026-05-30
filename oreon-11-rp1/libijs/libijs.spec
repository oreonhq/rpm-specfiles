%global source0_hash a8e3d10f5c4dd307655a7b6ff4002aeb827c44ba5ec41e99c6c46edfcf07aecc

# === GLOBAL MACROS ===========================================================

# According to Fedora Package Guidelines, it is advised that packages that can
# process untrusted input are build with position-independent code (PIC).
#
# Koji should override the compilation flags and add the -fPIC or -fPIE flags
# by default. This is here just in case this wouldn't happen for some reason.
# For more info: https://fedoraproject.org/wiki/Packaging:Guidelines#PIE
%global _hardened_build 1

# =============================================================================

Name:             libijs
Summary:          IJS Raster Image Transport Protocol Library
Version:          0.35
Release:          26%{?dist}

License:          AGPL-3.0-or-later

URL:              https://ghostscript.com/
Source:        https://github.com/ArtifexSoftware/ijs/archive/%{version}.tar.gz#/ijs-%{version}.tar.gz

BuildRequires:    gcc
BuildRequires:    git
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool

# =============================================================================

# NOTE: 'autosetup' macro (below) uses 'git' for applying the patches:
#       ->> All the patches should be provided in 'git format-patch' format.
#       ->> Auxiliary repository will be created during 'fedpkg prep', you
#           can see all the applied patches there via 'git log'.

# Upstream patches -- official upstream patches released by upstream since the
# ----------------    last rebase that are necessary for any reason:
#Patch000: example000.patch
# https://git.ghostscript.com/?p=ghostpdl.git;a=commitdiff;h=eb770edd1c
Patch: 0001-Squash-compiler-warning-in-ijs-code.patch


# Downstream patches -- these should be always included when doing rebase:
# ------------------
#Patch100: example100.patch


# Downstream patches for RHEL -- patches that we keep only in RHEL for various
# ---------------------------    reasons, but are not enabled in Fedora:
%if %{defined rhel} || %{defined centos}
#Patch200: example200.patch
%endif


# Patches to be removed -- deprecated functionality which shall be removed at
# ---------------------    some point in the future:


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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n ijs-%{version} -S git

# ---------------

%build
autoreconf -ifv
%configure --disable-static --enable-shared
%make_build

# ---------------

%install
%make_install

# Remove files that we don't want to ship:
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_libdir}/*.la

# Install the ijs_spec.pdf to correct location:
install -m 0755 -d %{buildroot}%{_docdir}/%{name}
install -m 0644 -p ijs_spec.pdf %{buildroot}%{_docdir}/%{name}

# === PACKAGING INSTRUCTIONS ==================================================

%files
%license COPYING
%{_libdir}/libijs-%{version}.so

# ---------------

%files devel
%dir %{_includedir}/ijs
%{_includedir}/ijs/*.h
%{_libdir}/libijs.so
%{_libdir}/pkgconfig/*.pc

# ---------------
%files doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/ijs_spec.pdf

# =============================================================================

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.35-26
- Prepare for Oreon 11 (RP1)
