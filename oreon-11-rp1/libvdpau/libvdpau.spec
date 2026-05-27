%global source0_hash a5d50a42b8c288febc07151ab643ac8de06a18446965c7241f89b4e810821913

Name:           libvdpau
Version:        1.5
Release:        11%{?dist}
Summary:        Wrapper library for the Video Decode and Presentation API
License:        MIT
URL:            https://freedesktop.org/wiki/Software/VDPAU/
Source0:        https://gitlab.freedesktop.org/vdpau/libvdpau/-/archive/%{version}/libvdpau-%{version}.tar.bz2
Patch0:         https://gitlab.freedesktop.org/vdpau/libvdpau/-/commit/2afa3f989af24a922692ac719fae23c321776cdb.diff#/%{name}-av1-trace.patch

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libX11-devel
BuildRequires:  meson >= 0.41
BuildRequires:  tex(latex)
BuildRequires:  pkgconfig(dri2proto) >= 2.2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
VDPAU is the Video Decode and Presentation API for UNIX. It provides an
interface to video decode acceleration and presentation hardware present in
modern GPUs.

%package        trace
Summary:        Trace library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    %{name}-debuginfo%{?_isa}

%description    trace
The %{name}-trace package contains trace library for %{name}.

%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch
Provides:       libvdpau-docs = %{version}-%{release}
Obsoletes:      libvdpau-docs < 0.6-2

%description    docs
The %{name}-docs package contains documentation for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Multilibs trace
Requires:       %{name}-trace%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(x11)
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete
# Let %%doc macro create the correct location in the rpm file.
rm -fr %{buildroot}%{_docdir}
mv %{_vpath_builddir}/doc/html html


%files
%doc AUTHORS
%license COPYING
%config(noreplace) %{_sysconfdir}/vdpau_wrapper.cfg
%{_libdir}/*.so.*
%dir %{_libdir}/vdpau/

%files trace
%{_libdir}/vdpau/%{name}_trace.so*

%files docs
%doc html

%files devel
%{_includedir}/vdpau/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/vdpau.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5-11
- Prepare for Oreon 11 (RP1)
