%global source0_hash 23be92ad8eb9625ce93b23b14f82f3cf88a4970c31d48581945ddfbac0441d06
%bcond check 1
%if 0%{?flatpak}
%bcond_with    docs
%else
%bcond_without docs
%endif
%bcond_without gtk2
%bcond_without mono
%ifnarch %{mono_arches}
%global with_mono 0
%endif
%global nsversion   0.1
%global gtknver2    ayatana-appindicator
%global gtknver3    ayatana-appindicator3
%global _summary    Ayatana Application Indicators
Name:           libayatana-appindicator
Version:        0.6.0
Release:        1%{?dist}
Summary:        Ayatana Application Indicators
License:        GPL-3.0-only AND LGPL-3.0-only AND (LGPL-3.0-only OR LGPL-2.1-only)
URL:            https://github.com/AyatanaIndicators/%{name}
Source0:        https://github.com/AyatanaIndicators/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-fix-mono-dir.patch
%if %{with docs}
%endif
%if %{with gtk2}
%endif
%if %{with mono}
%if %{with gtk2}
%endif
%endif
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-test-runner
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  mono-devel
BuildRequires:  mutter
BuildRequires:  pkgconfig(ayatana-indicator-0.4)
BuildRequires:  pkgconfig(ayatana-indicator3-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(gapi-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  vala
BuildRequires:  xwayland-run
# /oreon:deps
%description

%if %{with gtk2}
%package gtk2
Summary:        %{_summary} - GTK2
Provides:       libayatana-appindicator2 = %{version}-%{release}
Obsoletes:      libayatana-appindicator2 < 0.5.93
Provides:       libayatana-appindicator2-gir = %{version}-%{release}
Obsoletes:      libayatana-appindicator2-gir < 0.5.93
%description gtk2

This version is built against GTK2.

%package gtk2-devel
Summary:        Development files for %{name}-gtk2
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}
Provides:       libayatana-appindicator-doc = %{version}-%{release}
Obsoletes:      libayatana-appindicator-doc < 0.5.93
Provides:       libayatana-appindicator2-devel = %{version}-%{release}
Obsoletes:      libayatana-appindicator2-devel < 0.5.93
%description gtk2-devel
The %{name}-gtk2-devel package contains libraries
and header files for developing applications that use
%{name}-gtk2.
%endif

%package gtk3
Summary:        %_summary - GTK3
Provides:       libayatana-appindicator3 = %{version}-%{release}
Obsoletes:      libayatana-appindicator3 < 0.5.93
Provides:       libayatana-appindicator3-gir = %{version}-%{release}
Obsoletes:      libayatana-appindicator3-gir < 0.5.93
%description gtk3

This version is built against GTK3.

%package gtk3-devel
Summary:        Development files for %{name}-gtk3
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}
Provides:       libayatana-appindicator3-doc = %{version}-%{release}
Obsoletes:      libayatana-appindicator3-doc < 0.5.93
Provides:       libayatana-appindicator3-devel = %{version}-%{release}
Obsoletes:      libayatana-appindicator3-devel < 0.5.93
%description gtk3-devel
The %{name}-gtk3-devel package contains libraries
and header files for developing applications that use
%{name}-gtk3.

%if %{with mono}
%if %{with gtk2}
%package gtk2-sharp
Summary:        Mono C# bindings for %{name}-gtk2
Requires:       mono-core
Requires:       gtk-sharp2
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}
%description gtk2-sharp

This package contains the Mono C# bindings for %{name}-gtk2.

%package gtk2-sharp-devel
Summary:        Development files for %{name}-gtk2-sharp
Requires:       %{name}-gtk2-sharp%{?_isa} = %{version}-%{release}
%description gtk2-sharp-devel
The %{name}-gtk2-sharp-devel package contains libraries
and header files for developing applications that use
%{name}-gtk2-sharp.
%endif

%package gtk3-sharp
Summary:        Mono C# bindings for %{name}-gtk2
Requires:       mono-core
Requires:       gtk-sharp3
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}
%description gtk3-sharp

This package contains the Mono C# bindings for %{name}-gtk3.

%package gtk3-sharp-devel
Summary:        Development files for %{name}-sharp
Requires:       %{name}-gtk3-sharp%{?_isa} = %{version}-%{release}
%description gtk3-sharp-devel
The %{name}-gtk3-sharp-devel package contains libraries
and headerfiles for developing applications that use
%{name}-gtk3-sharp.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%define _vpath_builddir build-gtk3
%cmake \
%if %{with docs}
    -DENABLE_GTKDOC=ON \
%else
    -DENABLE_GTKDOC=OFF \
%endif
%if %{with check}
    -DENABLE_TESTS=ON \
%endif
    -DENABLE_BINDINGS_MONO=%{?with_mono:ON}%{!?with_mono:OFF} \
%cmake_build
%if %{with gtk2}
%define _vpath_builddir build-gtk2
%cmake -DFLAVOUR_GTK2=ON \
%if %{with docs}
    -DENABLE_GTKDOC=ON \
%else
    -DENABLE_GTKDOC=OFF \
%endif
%if %{with check}
    -DENABLE_TESTS=ON \
%endif
    -DENABLE_BINDINGS_MONO=%{?with_mono:ON}%{!?with_mono:OFF} \
%cmake_build
%endif
%install
%define _vpath_builddir build-gtk3
%cmake_install
%if %{with mono}
mkdir -p %{buildroot}/%{_monogacdir}
gacutil \
    -i %{buildroot}%{_libdir}/ayatana-appindicator3-sharp-%{nsversion}/ayatana-appindicator3-sharp.dll \
    -package ayatana-appindicator3-sharp \
    -root %{buildroot}%{_prefix}/lib
%endif
%if %{with gtk2}
%define _vpath_builddir build-gtk2
%cmake_install
%if %{with mono}
gacutil \
    -i %{buildroot}%{_libdir}/ayatana-appindicator-sharp-%{nsversion}/ayatana-appindicator-sharp.dll \
    -package ayatana-appindicator-sharp \
    -root %{buildroot}%{_prefix}/lib
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%endif
%if %{with check}
%check

pushd build-gtk3 >/dev/null
xwfb-run -c mutter -a %__ctest --output-on-failure --force-new-ctest-process
popd >/dev/null
%if %{with gtk2}
pushd build-gtk2 >/dev/null
xwfb-run -c mutter -a %__ctest --output-on-failure --force-new-ctest-process
popd >/dev/null
%endif
%endif
%if %{with gtk2}
%files -f %{oreon_filedir}/main.list
%files -n libayatana-appindicator-gtk2 -f %{oreon_filedir}/libayatana-appindicator-gtk2.list
%files -n libayatana-appindicator-gtk2-devel -f %{oreon_filedir}/libayatana-appindicator-gtk2-devel.list
%files -n libayatana-appindicator-gtk3 -f %{oreon_filedir}/libayatana-appindicator-gtk3.list
%files -n libayatana-appindicator-gtk3-devel -f %{oreon_filedir}/libayatana-appindicator-gtk3-devel.list
%files -n libayatana-appindicator-gtk2-sharp -f %{oreon_filedir}/libayatana-appindicator-gtk2-sharp.list
%files -n libayatana-appindicator-gtk2-sharp-devel -f %{oreon_filedir}/libayatana-appindicator-gtk2-sharp-devel.list
%files -n libayatana-appindicator-gtk3-sharp -f %{oreon_filedir}/libayatana-appindicator-gtk3-sharp.list
%files -n libayatana-appindicator-gtk3-sharp-devel -f %{oreon_filedir}/libayatana-appindicator-gtk3-sharp-devel.list

%changelog

%autochangelog
%endif
