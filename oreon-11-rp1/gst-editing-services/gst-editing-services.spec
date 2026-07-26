%global source0_hash 3d6000cbe1356beebe2a573dabd496e92348c30c843ffa13050469ec3da115dc

#global gitrel     140
#global gitcommit  bb40668ff9e47481d4741304f22129097a0d73d7
#global shortcommit %%(c=%%{gitcommit}; echo ${c:0:5})

Name:		gst-editing-services
Version:        1.28.1
Release:        1%{?dist}
Summary:	Gstreamer editing services

License:	GPL-2.0-or-later and LGPL-2.0-or-later
URL:		http://cgit.freedesktop.org/gstreamer/gst-editing-services/		
%if 0%{?gitrel}
# git clone git://anongit.freedesktop.org/gstreamer/gstreamer
# cd gstreamer; git reset --hard %{gitcommit}; ./autogen.sh; make; make distcheck
Source0:        gst-editing-services-%{version}.tar.xz
%else
# autogen.sh was run before tarballing, because it calls git
Source0:	http://gstreamer.freedesktop.org/src/gst-editing-services/gst-editing-services-%{version}.tar.xz
%endif

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:	gstreamer1-devel >= 1.6.0
BuildRequires:	gstreamer1-plugins-base-devel >= 1.6.0
BuildRequires:	gstreamer1-plugins-bad-free-devel >= 1.6.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	flex
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel

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

%files
%doc ChangeLog README
%license AUTHORS COPYING*
%{_bindir}/ges-launch-1.0
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/GES-1.0.typelib
%{_datadir}/bash-completion/completions/ges-launch-1.0
%doc %{_mandir}/man1/ges-launch-1.0.*
#%%{_libdir}/gst-validate-launcher/
%{python3_sitearch}/gi/overrides/*
#%%{_datadir}/gstreamer-1.0/validate/scenarios/ges-edit-clip-while-paused.scenario
#%%dir %%{_datadir}/gstreamer-1.0/validate/
#%%dir %%{_datadir}/gstreamer-1.0/validate/scenarios/

# plugins 
%{_libdir}/gstreamer-1.0/*.so

%files devel
%doc docs/
%{_libdir}/*.so
%{_includedir}/gstreamer-1.0/ges/
%{_libdir}/pkgconfig/gst-editing-services-1.0.pc
%{_datadir}/gir-1.0/GES-1.0.gir

%changelog
%autochangelog
