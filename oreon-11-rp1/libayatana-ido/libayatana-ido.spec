%global source0_hash bd59abd5f1314e411d0d55ce3643e91cef633271f58126be529de5fb71c5ab38
%bcond check 0
%global         src_name ayatana-ido
%global         nsversion 0.4
Name:           lib%{src_name}
Version:        0.10.4
Release:        1%{?dist}
Summary:        Ayatana Indicator Display Objects library
License:        LGPL-2.0-or-later AND GPL-3.0-only AND (LGPL-3.0-only OR LGPL-2.1-only)
URL:            https://github.com/AyatanaIndicators/%{src_name}
Source0:        https://github.com/AyatanaIndicators/%{src_name}/archive/%{version}/%{src_name}-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vala
BuildRequires:  xwayland-run
# /oreon:deps
%description

%package        gtk3
Summary:        %{summary} for GTK3
%description    gtk3

This version is built against GTK3.

%package        gtk3-devel
Summary:        Development files for %{name}-gtk3
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}
%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{src_name}-%{version}

%build

%cmake \
%if %{with check}
    -DENABLE_TESTS=ON
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

cd %_vpath_builddir
xwfb-run -- %__ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}
%endif
%files -f %{oreon_filedir}/main.list
%files -n libayatana-ido-gtk3 -f %{oreon_filedir}/libayatana-ido-gtk3.list
%files -n libayatana-ido-gtk3-devel -f %{oreon_filedir}/libayatana-ido-gtk3-devel.list

%changelog

%autochangelog
