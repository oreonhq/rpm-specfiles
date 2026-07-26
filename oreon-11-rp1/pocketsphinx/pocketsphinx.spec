%global source0_hash none

Name:           pocketsphinx
Epoch:          2
Version:        5.0.4
Release:        5%{?dist}
Summary:        Real-time speech recognition

License:        BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://cmusphinx.github.io/
Source0:        https://github.com/cmusphinx/pocketsphinx/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-scikit-build-core

Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-models

%description
PocketSphinx is a version of the open-source Sphinx-II speech recognition
system which is able to recognize speech in real-time.  While it may be
somewhat less accurate than the offline speech recognizers, it is lightweight
enough to run on handheld and embedded devices.

%package devel
Summary:        Header files for developing with pocketsphinx
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(jquery)

%description devel
Header files for developing with pocketsphinx.

%package libs
Summary:        Shared libraries for pocketsphinx executables

%description libs
Shared libraries for pocketsphinx executables.

%package models
Summary:        Voice and language models for pocketsphinx
BuildArch:      noarch

%description models
Voice and language models for pocketsphinx.

%package plugin
Summary:        Pocketsphinx gstreamer plugin
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gstreamer1-plugins-base%{?_isa}

%description plugin
A gstreamer plugin for pocketsphinx.

%package -n python3-pocketsphinx
%{?python_provide:%python_provide python3-pocketsphinx}
Summary:        Python interface to pocketsphinx
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-pocketsphinx
Python interface to pocketsphinx.

%prep
%autosetup -p1

%build
# Build twice for C and Python (also below in install section).
# See https://github.com/cmusphinx/pocketsphinx/issues/342.
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DBUILD_GSTREAMER="on"
%cmake_build
mv redhat-linux-build redhat-linux-build-c
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DSKBUILD="on"
%cmake_build
%pyproject_wheel

%install
# Install twice for C and Python.
# See https://github.com/cmusphinx/pocketsphinx/issues/342.
mv redhat-linux-build redhat-linux-build-python
mv redhat-linux-build-c redhat-linux-build
%cmake_install
rm -rf redhat-linux-build

mv redhat-linux-build-python redhat-linux-build
%pyproject_install
%pyproject_save_files pocketsphinx

%ldconfig_scriptlets libs

%files
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%doc AUTHORS NEWS README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files models
%{_datadir}/%{name}/

%files plugin
%{_libdir}/gstreamer-1.0/*

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
