%global source0_hash 83cbb720dc7f48f7b9037955dbdcd62ed09ced7db67cb3ee3f0557415560d9f4

# To ensure hardened build on EL7
%global _hardened_build 1

# Fix platform definitions so slibtool build scripts can find binaries
# Matches what's in the gcc packaging
%ifnarch %{arm}
%global _gnu %{nil}
%else
%global _gnu -gnueabi
%endif
%global _host %{_target_platform}
%global _build %{_target_platform}

Name:           slibtool
Version:        0.5.28
Release:        16%{?dist}
Summary:        A skinny libtool implementation, written in C

License:        MIT
URL:            http://git.midipix.org/cgit.cgi/slibtool
Source0:        http://midipix.org/dl/slibtool/%{name}-%{version}.tar.xz

BuildRequires:  gcc, make

# slibtool uses libslibtool internally
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

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

%autosetup -p1

%build
%configure --enable-shared --all-shared \
           --pkgpsrc="https://src.fedoraproject.org/rpms/slibtool/" \
           --pkgdurl="https://apps.fedoraproject.org/packages/slibtool"
%make_build

%install
%make_install

%ldconfig_scriptlets libs

%files
%license COPYING.SLIBTOOL
%doc README NEWS THANKS CONTRIB
%{_bindir}/clibtool*
%{_bindir}/dlibtool*
%{_bindir}/r*libtool
%{_bindir}/slibtool*

%files libs
%license COPYING.SLIBTOOL
%{_libdir}/lib%{name}.so.*

%files devel
%license COPYING.SLIBTOOL
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
