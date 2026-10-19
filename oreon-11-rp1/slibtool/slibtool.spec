%global source0_hash 2e7a4ae528c49c82743ae91260d3fa24bee3d91d9a87066e3491a24ba745a948
%global _hardened_build 1
%ifnarch %{arm}
%global _gnu %{nil}
%else
%global _gnu -gnueabi
%endif
%global _host %{_target_platform}
%global _build %{_target_platform}
Name:           slibtool
Version:        0.7.4
Release:        1%{?dist}
Summary:        A skinny libtool implementation, written in C
License:        MIT
URL:            http://git.midipix.org/cgit.cgi/slibtool
Source0:        http://midipix.org/dl/slibtool/%{name}-%{version}.tar.xz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
'slibtool' is an independent reimplementation of the widely used libtool,
written in C. 'slibtool' is designed to be a clean, fast, easy-to-use
libtool drop-in replacement, and is accordingly aimed at package authors,
distro developers, and system integrators. 'slibtool' maintains compatibility
with libtool in nearly every aspect of the tool's functionality as well as
semantics, leaving out (or turning into a no-op) only a small number of
features that are no longer needed on modern systems.

Being a compiled binary, and although not primarily written for the sake of
performance, building a package with 'slibtool' is often faster than with its
script-based counterpart. The resulting performance gain would normally vary
between packages, and is most noticeable in builds that invoke libtool a large
number of times, and which are characterized by the short compilation duration
of individual translation units.

%package libs
Summary:        Backend library for %{name}
%description libs
This package provides libraries for applications to use the functionality
of %{name}.

%package devel
Summary:        Development files for lib%{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package provides files necessary for developing applications
to use functionality provided by %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-shared --all-shared \
           --pkgpsrc="https://src.fedoraproject.org/rpms/slibtool/" \
           --pkgdurl="https://apps.fedoraproject.org/packages/slibtool"
%make_build
%install
%make_install
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n slibtool-libs -f %{oreon_filedir}/slibtool-libs.list
%files -n slibtool-devel -f %{oreon_filedir}/slibtool-devel.list

%changelog

%autochangelog
