%global source0_hash 73d71c908b803f12e4a5ecd8392511b58afbdd0c82ad7909611a17bb7847c5c8
%bcond check 1
%bcond_without gtk2
%global         nsversion 0.4
Name:           libayatana-indicator
Version:        0.9.5
Release:        1%{?dist}
Summary:        Ayatana Indicators Shared Library
License:        GPL-3.0-only
URL:            https://github.com/AyatanaIndicators/%{name}
Source0:        https://github.com/AyatanaIndicators/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with gtk2}
%endif
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-test-runner
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  mutter
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libayatana-ido3-0.4)
BuildRequires:  vala
BuildRequires:  xwayland-run
# /oreon:deps
%description

%if %{with gtk2}
%package        gtk2
Summary:        %{summary} for GTK2
Provides:       libayatana-indicator2 = %{version}-%{release}
Obsoletes:      libayatana-indicator2 < 0.9.5
%description    gtk2

This version is built against GTK2.
%endif

%package        gtk3
Summary:        %{summary} for GTK3
Provides:       libayatana-indicator3 = %{version}-%{release}
Obsoletes:      libayatana-indicator3 < 0.9.5
%description    gtk3

This version is built against GTK3.

%if %{with gtk2}
%package        gtk2-devel
Summary:        Development files for %{name}-gtk2
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}
Provides:       libayatana-indicator2-devel = %{version}-%{release}
Obsoletes:      libayatana-indicator2-devel < 0.9.5
%description    gtk2-devel
The %{name}-gtk2-devel package contains libraries and header files for
developing applications that use %{name}-gtk2.
%endif

%package        gtk3-devel
Summary:        Development files for %{name}-gtk3
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}
Provides:       libayatana-indicator3-devel = %{version}-%{release}
Obsoletes:      libayatana-indicator3-devel < 0.9.5
%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.

%package tools-gtk3
Summary:    Development tools for %{name}
Requires:   %{name}-gtk3%{?_isa} = %{version}-%{release}
%description tools-gtk3

This package contains GTK3 developer tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%define _vpath_builddir build-gtk3
%cmake \
%if %{with check}
    -DENABLE_TESTS=ON
%endif
%cmake_build
%if %{with gtk2}
%define _vpath_builddir build-gtk2
%cmake -DFLAVOUR_GTK2=ON \
%if %{with check}
    -DENABLE_TESTS=ON
%endif
%cmake_build
%endif
%install
%define _vpath_builddir build-gtk3
%cmake_install
%if %{with gtk2}
%define _vpath_builddir build-gtk2
%cmake_install
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*
%endif
%if %{with check}
%check

pushd build-gtk3 >/dev/null
xwfb-run -c mutter -- %__ctest --output-on-failure --force-new-ctest-process
popd >/dev/null
%if %{with gtk2}
pushd build-gtk2 >/dev/null
xwfb-run -c mutter -- %__ctest --output-on-failure --force-new-ctest-process
popd >/dev/null
%endif
%endif
%if %{with gtk2}
%files -f %{oreon_filedir}/main.list
%files -n libayatana-indicator-gtk2 -f %{oreon_filedir}/libayatana-indicator-gtk2.list
%files -n libayatana-indicator-gtk3 -f %{oreon_filedir}/libayatana-indicator-gtk3.list
%files -n libayatana-indicator-gtk2-devel -f %{oreon_filedir}/libayatana-indicator-gtk2-devel.list
%files -n libayatana-indicator-gtk3-devel -f %{oreon_filedir}/libayatana-indicator-gtk3-devel.list
%files -n libayatana-indicator-tools-gtk3 -f %{oreon_filedir}/libayatana-indicator-tools-gtk3.list

%changelog

%autochangelog
%endif
