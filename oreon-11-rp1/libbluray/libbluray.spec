%ifarch %{java_arches}
%global build_bdj 1
%else
%global build_bdj 0
%endif

Name:           libbluray
Version:        1.4.0
Release:        3%{?dist}
Summary:        Library to access Blu-Ray disks for video playback 
License:        LGPL-2.0-or-later
URL:            https://www.videolan.org/developers/libbluray.html

Source0:        https://download.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch0:         libbluray-0.8.0-no_doxygen_timestamp.patch
# https://code.videolan.org/videolan/libbluray/-/commit/48d76414455ab6a7d270cec96d6e83673df8a00d
Patch1:         libbluray-1.4.0-java_23_support.patch

BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libudfread-devel >= 1.2.0
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  texlive-latex
%if %{build_bdj}
BuildRequires:  ant
BuildRequires:  java-devel >= 1:1.8.0
BuildRequires:  jpackage-utils
%endif

%description
This package is aiming to provide a full portable free open source Blu-Ray
library, which can be plugged into popular media players to allow full Blu-Ray
navigation and playback on Linux. It will eventually be compatible with all
current titles, and will be easily portable and embeddable in standard players
such as MPlayer and VLC.

%if %{build_bdj}
%package        bdj
Summary:        BDJ support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       java-headless >= 1:1.8.0
Requires:       jpackage-utils

%description    bdj
The %{name}-bdj package contains the jar file needed to add BD-J support to
%{name}. BD-J support is still considered alpha.
%endif

%package        utils
Summary:        Test utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains test utilities for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch -P0 -p1 -b .no_timestamp
%patch -P1 -p1 -b .java_23

rm -rf contrib/libudfread

%build
%meson \
  --default-library=shared \
%if %{build_bdj}
  -Dbdj_jar=enabled \
  -Djava9=true \
  -Dbdj_type=j2se \
  -Djdk_home=%{_jvmdir}/java \
%else
  -Dbdj_jar=disabled \
%endif
  -Denable_docs=true \
  -Denable_devtools=true \
  -Denable_examples=true

%meson_build


%install
%meson_install
mv %{buildroot}%{_docdir}/%{name}/html .


%files
%license COPYING
%doc ChangeLog README.md
%{_libdir}/*.so.3*

%if %{build_bdj}
%files bdj
%{_javadir}/libbluray-j2se-%{version}.jar
%{_javadir}/libbluray-awt-j2se-%{version}.jar
%endif

%files utils
%{_bindir}/*

%files devel
%doc html/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-3
- Prepare for Oreon 11 (RP1)
