%global source0_hash fe78ad9f74c8ebf93d5c8ad6fa2c13236af330f3c67149d91a0647b3dc6f3958
%ifarch aarch64
%bcond_without neon
%else
%bcond_with neon
%endif
%ifarch %{arm}
%if %{with neon}
%global my_optflags %(echo -n "%{optflags}" | sed 's/-mfpu=[^ \\t]\\+//g'; echo " -mfpu=neon")
%{expand: %global optflags %{my_optflags}}
%global mfpu_neon -Dhave_mfpu_neon=1
%else
%global mfpu_neon -Dhave_mfpu_neon=0
%endif
%endif
%global optflags %(echo %{optflags} -DFMT_DEPRECATED_OSTREAM)
Name:		gnuradio
Version:	3.10.12.0
Release:        12%{?dist}
Summary:        Software defined radio framework
License:	GPL-3.0-or-later
URL:		https://www.gnuradio.org/
Source0:        https://github.com/gnuradio/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires(pre):	shadow-utils
Requires:	python3-%{name} = %{version}-%{release}
Requires:	python3-numpy
Requires:	python3-thrift
Requires:	python3-pyyaml
Requires:	python3-gobject
Requires:	python3-mako
Requires:	python3-click
Requires:	python3-qt5
Requires:	python3-scipy
Requires:	python3-pyqtgraph
Requires:	python3-zmq
Requires:	python3-jsonschema
Requires:	gtk3
Suggests:	soapy-rtlsdr
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SoapySDR-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  codec2-devel
BuildRequires:  cppzmq-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gobject-introspection
BuildRequires:  graphviz
BuildRequires:  gsl-devel
BuildRequires:  gsm-devel
BuildRequires:  gtk3-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libad9361-iio-devel
BuildRequires:  libiio-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  portaudio-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-cairo
BuildRequires:  python3-click
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-jsonschema
BuildRequires:  python3-lxml
BuildRequires:  python3-mako
BuildRequires:  python3-numpy
BuildRequires:  python3-pyyaml
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-scipy
BuildRequires:  python3-thrift
BuildRequires:  python3-zmq
BuildRequires:  qwt-qt5-devel
BuildRequires:  spdlog-devel
BuildRequires:  tex(latex)
BuildRequires:  thrift
BuildRequires:  uhd-devel
BuildRequires:  volk-devel
BuildRequires:  xdg-utils
BuildRequires:  xmlto
BuildRequires:  zeromq-devel
# /oreon:deps
%description
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

%package -n python3-%{name}
Summary:	GNU Radio Python 3 module
%description -n python3-%{name}
GNU Radio Python 3 module

%package devel
Summary:	GNU Radio
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	cmake
Requires:	boost-devel%{?_isa}
%description devel
GNU Radio Headers

%package doc
Summary:	GNU Radio
Requires:	%{name} = %{version}-%{release}
%description doc
GNU Radio Documentation

%package examples
Summary:	GNU Radio
Requires:	%{name} = %{version}-%{release}
%description examples
GNU Radio examples

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?alphatag}

%build

%undefine __cmake_in_source_build
%cmake \
-DSYSCONFDIR=%{_sysconfdir} \
-DGR_PKG_DOC_DIR=%{_docdir}/%{name} \
-DGR_PYTHON_DIR=%{python3_sitearch} \
-DPYTHON_EXECUTABLE=%{__python3} \
%{?mfpu_neon} \
%if "%{?_lib}"=="lib64"
-DLIB_SUFFIX=64
%endif
%cmake_build
%install
%cmake_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
  grc/scripts/freedesktop/gnuradio-grc.desktop
install -Dpm 0644 grc/scripts/freedesktop/gnuradio-grc.xml \
  %{buildroot}%{_datadir}/mime/packages/gnuradio-grc.xml
install -Dpm 0644 grc/scripts/freedesktop/org.gnuradio.grc.metainfo.xml \
  %{buildroot}%{_datadir}/metainfo/org.gnuradio.grc.metainfo.xml
for i in 16 24 32 48 64 128 256
do
  install -Dpm 0644 grc/scripts/freedesktop/grc-icon-${i}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/gnuradio-grc.png
done
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-gnuradio -f %{oreon_filedir}/python3-gnuradio.list
%files -n gnuradio-devel -f %{oreon_filedir}/gnuradio-devel.list
%files -n gnuradio-doc -f %{oreon_filedir}/gnuradio-doc.list
%files -n gnuradio-examples -f %{oreon_filedir}/gnuradio-examples.list

%changelog

%autochangelog
