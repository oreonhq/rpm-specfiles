%global source0_hash 425ddc9358151c52775a00b14e9dbd4044fc1f3aa931beef2aa3633707ba1eb8
%ifarch i686 x86_64
%global optflags %{optflags} -mno-sse4.1
%endif
Name:           frei0r-plugins
Version:        3.6.0
Release:        1%{?dist}
Summary:        Frei0r - a minimalist plugin API for video effects
License:        GPL-2.0-or-later
URL:            https://frei0r.dyne.org/
Source0:        https://github.com/dyne/frei0r/archive/refs/tags/v%{version}.tar.gz#/frei0r-plugins-%{version}.tar.gz
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  gavl-devel
BuildRequires:  gcc-c++
BuildRequires:  opencv-devel
# /oreon:deps
%description
It is a minimalist plugin API for video sources and filters. The behavior of
the effects can be controlled from the host by simple parameters. The intent is
to solve the recurring re-implementation or adaptation issue of standard effect

%package	opencv
Summary:  Frei0r plugins using OpenCV
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description opencv
Frei0r plugins that use the OpenCV computer vision framework.

%package -n     frei0r-devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n frei0r-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir frei0r-%{version}
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles frei0r-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n frei0r-plugins-opencv -f %{oreon_filedir}/frei0r-plugins-opencv.list
%files -n frei0r-devel -f %{oreon_filedir}/frei0r-devel.list

%changelog

%autochangelog
