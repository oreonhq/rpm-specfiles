%global source0_hash af050313ee63bc18b35b2e064e5dce05b276aaf6d1aa2b8a82ced1fe2f8028e9
%bcond_without check
%global so_version 3
Name:           rubberband
Version:        4.0.0
Release:        1%{?dist}
Summary:        Audio time-stretching and pitch-shifting utility
License:        GPL-2.0-or-later
URL:            http://www.breakfastquay.com/rubberband/
Source0:        https://breakfastquay.com/files/releases/%{name}-%{version}.tar.bz2
Patch:          %{name}-disable-failed-ppc64le-tests.diff
Recommends:     (ladspa-%{name}-plugins if ladspa)
Recommends:     (lv2-%{name}-plugins if lv2)
Recommends:     (vamp-%{name}-plugins if vamp-plugin-sdk)
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  vamp-plugin-sdk-devel
# /oreon:deps
%description

This package provides standalone command-line utilities.

%package        libs
Summary:        Audio time-stretching and pitch-shifting library
Conflicts:      %{name} < %{version}-%{release}
%description    libs

This package provides a shared library for use by applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n ladspa-%{name}-plugins
Summary:        LADSPA plugin for audio time-stretching and pitch-shifting
Requires:       ladspa
Conflicts:      %{name} < %{version}-%{release}
%description -n ladspa-%{name}-plugins

This package provides a LADSPA plugin.

%package     -n lv2-%{name}-plugins
Summary:        LV2 plugin for audio time-stretching and pitch-shifting
Requires:       lv2
Conflicts:      %{name} < %{version}-%{release}
%description -n lv2-%{name}-plugins

This package provides a LV2 plugin.

%package     -n vamp-%{name}-plugins
Summary:        VAMP plugin for audio time-stretching and pitch-shifting
Conflicts:      %{name} < %{version}-%{release}
%description -n vamp-%{name}-plugins

This package provides a VAMP plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
  -Dfft=fftw \
  -Djni=disabled \
  -Dresampler=libsamplerate
%meson_build
%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_libdir}/*.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubberband-libs -f %{oreon_filedir}/rubberband-libs.list
%files -n rubberband-devel -f %{oreon_filedir}/rubberband-devel.list
%files -n ladspa-rubberband-plugins -f %{oreon_filedir}/ladspa-rubberband-plugins.list
%files -n lv2-rubberband-plugins -f %{oreon_filedir}/lv2-rubberband-plugins.list
%files -n vamp-rubberband-plugins -f %{oreon_filedir}/vamp-rubberband-plugins.list

%changelog

%autochangelog
