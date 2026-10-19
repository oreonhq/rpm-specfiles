%global source0_hash 3d6000cbe1356beebe2a573dabd496e92348c30c843ffa13050469ec3da115dc
Name:		gst-editing-services
Version:        1.28.7
Release:        1%{?dist}
Summary:        Gstreamer editing services
License:	GPL-2.0-or-later and LGPL-2.0-or-later
URL:		http://cgit.freedesktop.org/gstreamer/gst-editing-services/		
%if 0%{?gitrel}
Source0:        gst-editing-services-%{version}.tar.xz
%else
%endif
# oreon:deps
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
# /oreon:deps
%description 
This is a high-level library for facilitating the creation of audio/video
non-linear editors.

%package devel
Summary: Development files for gst-editing-services
License:	GPL-2.0-or-later and LGPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for
developing applications that use %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p3 -n gst-editing-services-%{version}

%build

%meson \
	-D validate=disabled \
	-D doc=disabled \
        -D tests=disabled
%meson_build
find . -name '.gitignore' | xargs rm -f
%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
cp data/completions/ges-launch-1.0 \
        %{buildroot}%{_datadir}/bash-completion/completions/ges-launch-1.0
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gst-editing-services-devel -f %{oreon_filedir}/gst-editing-services-devel.list

%changelog

%autochangelog
