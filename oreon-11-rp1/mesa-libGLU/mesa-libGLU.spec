# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 bd43fe12f374b1192eb15fe20e45ff456b9bc26ab57f0eee919f96ca0f8a330f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           mesa-libGLU
Version:        9.0.3
Release:        8%{?dist}
Summary:        Mesa libGLU library

License:        X11
URL:            http://mesa3d.org/
# ftp.freedesktop.org TLS hostname does not match on some workers, use Mesa archive
Source0:        https://mesa.freedesktop.org/archive/glu/glu-%{version}.tar.xz
Source2:        make-git-snapshot.sh

BuildRequires:  gcc-c++
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
Provides: libGLU

%description
Mesa implementation of the standard GLU OpenGL utility API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:	libGLU-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_verify_sources
%autosetup -p1 -n glu-%{version}

%build
%meson -Dgl_provider=glvnd
%meson_build

%install
%meson_install
find $RPM_BUILD_ROOT -name '*.a' -delete

%ldconfig_scriptlets

%files
%{_libdir}/libGLU.so.1
%{_libdir}/libGLU.so.1.3.*

%files devel
%{_includedir}/GL/glu*.h
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.0.3-9
- Source0 from mesa.freedesktop.org archive (ftp.freedesktop.org TLS mismatch)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.0.3-8
- Prepare for Oreon 11 (RP1)
