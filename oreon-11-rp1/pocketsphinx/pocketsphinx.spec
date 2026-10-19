%global source0_hash 9acd63cfdc76bbc85b7b6c6610b7a9cf30c79d5b36a31de7dc2f969e962653d7
Name:           pocketsphinx
Epoch:          2
Version:        5.0.4
Release:        1%{?dist}
Summary:        Real-time speech recognition
License:        BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://cmusphinx.github.io/
Source0:        https://github.com/cmusphinx/pocketsphinx/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-models
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pocketsphinx = %{version}-%{release}
# /oreon:deps
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
%oreon_prep
%build

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
mv redhat-linux-build redhat-linux-build-python
mv redhat-linux-build-c redhat-linux-build
%cmake_install
rm -rf redhat-linux-build
mv redhat-linux-build-python redhat-linux-build
%pyproject_install
%ldconfig_scriptlets libs
%oreon_autofiles python3-pocketsphinx usr/lib/python3*/site-packages/pocketsphinx* usr/lib64/python3*/site-packages/pocketsphinx* usr/bin/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/pocketsphinx* usr/lib64/python3*/site-packages/pocketsphinx* usr/bin/*

%files
%files -n pocketsphinx-devel -f %{oreon_filedir}/pocketsphinx-devel.list
%files -n pocketsphinx-libs -f %{oreon_filedir}/pocketsphinx-libs.list
%files -n pocketsphinx-models -f %{oreon_filedir}/pocketsphinx-models.list
%files -n pocketsphinx-plugin -f %{oreon_filedir}/pocketsphinx-plugin.list
%files -n python3-pocketsphinx -f %{oreon_filedir}/python3-pocketsphinx.list

%changelog

%autochangelog
