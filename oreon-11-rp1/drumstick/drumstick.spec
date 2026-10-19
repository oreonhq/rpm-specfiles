%global source0_hash 7d537aeca77486fc8f57a84af3df1bd0ddddb401a61935e8b4821542d160b677
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
Summary:        C++/Qt6 wrapper around multiple MIDI interfaces
Name:    drumstick
Version: 2.11.1
Release:        1%{?dist}
License: GPL-3.0-or-later
URL:     https://drumstick.sourceforge.io/
Source0:        https://sourceforge.net/projects/drumstick/files/%{version}/drumstick-%{version}.tar.bz2
Obsoletes: aseqmm < %{version}-%{release}
Provides: aseqmm = %{version}-%{release}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  sonivox-devel
# /oreon:deps
%description
The drumstick library is a C++ wrapper around the ALSA library sequencer
interface, using Qt objects, idioms and style. OSS, network and Fluidsynth
interfaces are also supported by this library.

%package devel
Summary: Developer files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: alsa-lib-devel
Obsoletes: aseqmm-devel < %{version}-%{release}
Provides: aseqmm-devel = %{version}-%{release}
%description devel
%{summary}.

%package examples
Summary: Example programs for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: aseqmm-examples < %{version}-%{release}
Provides: aseqmm-examples = %{version}-%{release}
%description examples
This package contains the test/example programs for %{name}.

%package drumgrid
Summary: Drum Grid application from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description drumgrid
This package contains the drumgrid application.

%package guiplayer
Summary: MIDI player from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description guiplayer
This package contains the guiplayer application.

%package vpiano
Summary: Virtual piano application from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description vpiano
This package contains the vpiano application.

%package dumprmi
Summary: RIFF RMID file support for %{name}
Requires: %{name}-examples = %{version}-%{release}
%description dumprmi
Standard RIFF MIDI File dump program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake
%cmake_build
doxygen %{_vpath_builddir}/Doxyfile
%install
%cmake_install
for i in $RPM_BUILD_ROOT%{_datadir}/applications/* ; do
  desktop-file-validate $i
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n drumstick-devel -f %{oreon_filedir}/drumstick-devel.list
%files -n drumstick-examples -f %{oreon_filedir}/drumstick-examples.list
%files -n drumstick-drumgrid -f %{oreon_filedir}/drumstick-drumgrid.list
%files -n drumstick-guiplayer -f %{oreon_filedir}/drumstick-guiplayer.list
%files -n drumstick-vpiano -f %{oreon_filedir}/drumstick-vpiano.list
%files -n drumstick-dumprmi -f %{oreon_filedir}/drumstick-dumprmi.list

%changelog

%autochangelog
