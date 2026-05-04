# Upstream KDE automoc 0.9.88 ships Automoc4Config.cmake without cmake_policy(SET CMP0002 OLD).
# Fedora’s automoc4 added that policy for ancient CMake; CMake 3.28+ rejects OLD for CMP0002 and
# find_package(KDE4) fails. Epoch so this replaces same-version distro builds in mock.
Epoch:   1
Summary: KDE4 Meta Object Compiler (automoc4)
Name:    automoc4
Version: 0.9.88
Release: 1%{?dist}

License: BSD-3-Clause
URL:     https://invent.kde.org/developer-tools/automoc

# Unpacks to automoc-%{version}
Source0: https://github.com/KDE/automoc/archive/refs/tags/v%{version}/automoc-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: kde4-filesystem
BuildRequires: qt4-devel

%ifarch x86_64 aarch64 ppc64 ppc64le s390x
%global automoc_lib_suffix 64
%else
%global automoc_lib_suffix %{nil}
%endif

%description
automoc4 scans C++ sources for Q_OBJECT macros and runs moc where needed. This package ships the
automoc4 binary and the CMake module files used by KDE4 and kdelibs4.


%prep
%setup -q -n automoc-%{version}


%build
mkdir build
pushd build
%if 0%{?automoc_lib_suffix:1}
%__cmake .. \
  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DLIB_SUFFIX:STRING=%{automoc_lib_suffix} \
  -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_qt4_bindir}/qmake
%else
%__cmake .. \
  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_qt4_bindir}/qmake
%endif
%__cmake --build . -- %{?_smp_mflags}
popd


%install
DESTDIR=%{buildroot} %__cmake --install build


%files
%{_bindir}/automoc4
%{_libdir}/automoc4/
