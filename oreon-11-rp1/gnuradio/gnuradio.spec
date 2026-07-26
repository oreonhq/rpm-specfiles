%global source0_hash 2353c8f669f8a4cfbde13bbfeb75c4329b5994bc4e9411f5eb0e9117bd87681a

# NEON support is by default enabled on aarch64 and disabled on other ARMs (it can be overridden)
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

# fmt API change workaround
%global optflags %(echo %{optflags} -DFMT_DEPRECATED_OSTREAM)

# For versions not yet on ftp, pull from git
#%%global git_commit 441a3767e05d15e62c519ea66b848b5adb0f4b3a

#%%global alphatag rc1

Name:		gnuradio
Version:	3.10.12.0
Release:	12%{?alphatag:.%{alphatag}}%{?dist}
Summary:	Software defined radio framework

License:	GPL-3.0-or-later
URL:		https://www.gnuradio.org/
#Source0:	http://gnuradio.org/releases/gnuradio/gnuradio-%%{version}%%{?alphatag}.tar.xz
#Source0:	http://gnuradio.org/releases/gnuradio/gnuradio-%%{version}.tar.gz
Source0:	https://github.com/gnuradio/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# git clone git://gnuradio.org/gnuradio
# cd gnuradio
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{git_commit} | \
# gzip > ../%%{name}-%%{version}.tar.gz

Requires(pre):	shadow-utils
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	alsa-lib-devel
BuildRequires:	boost-devel
BuildRequires:	codec2-devel
BuildRequires:	cppzmq-devel
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	fftw-devel
BuildRequires:	findutils
BuildRequires:	gmp-devel
BuildRequires:	graphviz
BuildRequires:	gsl-devel
BuildRequires:	gsm-devel
BuildRequires:	gtk3-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	portaudio-devel
BuildRequires:	gobject-introspection
BuildRequires:	python3-devel
BuildRequires:	python3-cairo
BuildRequires:	python3-click
BuildRequires:	python3-gobject
BuildRequires:	python3-numpy
BuildRequires:	python3-pyyaml
BuildRequires:	python3-lxml
BuildRequires:	python3-mako
BuildRequires:	python3-qt5-devel
BuildRequires:	python3-scipy
BuildRequires:	python3-thrift
BuildRequires:	python3-zmq
BuildRequires:	python3-jsonschema
BuildRequires:	qwt-qt5-devel
BuildRequires:	tex(latex)
BuildRequires:	SDL-devel
BuildRequires:	thrift
BuildRequires:	uhd-devel
BuildRequires:	xdg-utils
BuildRequires:	xmlto
BuildRequires:	zeromq-devel
BuildRequires:	python3-gobject
BuildRequires:	pybind11-devel
BuildRequires:	volk-devel
BuildRequires:	libsndfile-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	spdlog-devel
BuildRequires:	libiio-devel
BuildRequires:	libad9361-iio-devel
# for pygccxml
#BuildRequires:	castxml

Requires:	python3-%{name} = %{version}-%{release}
Requires:	python3-numpy
Requires:	python3-thrift
%if ! 0%{?rhel}
Requires:	python3-pyopengl
%endif
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
# this could be dropped when f32 get retired (not counting EPEL)
%undefine __cmake_in_source_build

# -DLIB_SUFFIX workaround due to:
# https://github.com/gnuradio/gnuradio/issues/7766
# https://bugzilla.redhat.com/show_bug.cgi?id=2351130
%cmake \
-DSYSCONFDIR=%{_sysconfdir} \
-DGR_PKG_DOC_DIR=%{_docdir}/%{name} \
-DGR_PYTHON_DIR=%{python3_sitearch} \
-DPYTHON_EXECUTABLE=%{__python3} \
%{?mfpu_neon} \
%if "%{?_lib}"=="lib64"
-DLIB_SUFFIX=64
%endif
#-DENABLE_DOXYGEN=FALSE \

%cmake_build

%install
%cmake_install

# desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
  grc/scripts/freedesktop/gnuradio-grc.desktop
# mime
install -Dpm 0644 grc/scripts/freedesktop/gnuradio-grc.xml \
  %{buildroot}%{_datadir}/mime/packages/gnuradio-grc.xml
# metainfo
install -Dpm 0644 grc/scripts/freedesktop/org.gnuradio.grc.metainfo.xml \
  %{buildroot}%{_datadir}/metainfo/org.gnuradio.grc.metainfo.xml
# icons
for i in 16 24 32 48 64 128 256
do
  install -Dpm 0644 grc/scripts/freedesktop/grc-icon-${i}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/gnuradio-grc.png
done

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/gnuradio
%{_datadir}/applications/gnuradio-grc.desktop
%{_datadir}/mime/packages/gnuradio-grc.xml
%{_datadir}/icons/hicolor/*/apps/gnuradio-grc.png
%{_datadir}/metainfo/org.gnuradio.grc.metainfo.xml
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/gnuradio
%exclude %{_datadir}/gnuradio/examples
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%doc %{_docdir}/%{name}

%files -n python3-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/pmt/
%{_datadir}/bash-completion/completions/gr_modtool
%{_datadir}/fish/vendor_completions.d/gr_modtool.fish
%{_datadir}/zsh/site-functions/_gr_modtool

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/gnuradio

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%files examples
%{_datadir}/gnuradio/examples

%changelog
%autochangelog
