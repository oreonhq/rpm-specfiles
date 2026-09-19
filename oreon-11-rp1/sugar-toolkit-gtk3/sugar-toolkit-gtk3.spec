%global source0_hash 2b508b28d75fe30967de0650dcc67aaacfa579e707b043a2e43785c315039c57

%undefine _hardened_build

Name:    sugar-toolkit-gtk3
Version: 0.121
Release: 13%{?dist}
Summary: Sugar toolkit GTK+ 3
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     http://wiki.laptop.org/go/Sugar

Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Source1: macros.sugar
Patch0: Fix-logging-usage.patch

BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: gettext-devel
BuildRequires: gtk3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: librsvg2-devel
BuildRequires: libSM-devel
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-gobject
# py-compile needs updating
BuildRequires: automake
Requires: python3-dateutil
Requires: python3-dbus
Requires: python3-gobject
Requires: python3-decorator
Requires: gettext-runtime
Requires: sugar-datastore
Requires: unzip
Requires: webkit2gtk4.1
Requires: git-core

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.
This is the toolkit depending on GTK3.

%package devel
Summary: Invokation information for accessing SugarExt-1.0
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the invocation information for accessing
the SugarExt-1.0 library through gobject-introspection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf
ls -1 %{_datadir}/automake-*/py-compile | sort | \
	tail -n 1 | while read f
do
	cp -p $f .
done

%configure
# There are missing dependencies in this project's Makefiles, in
# particular dependencies on libsugarext.   LTO is tripping these
# issues regularly.
make -O V=1 VERBOSE=1

%install
%make_install

mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -pm 644 %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d/macros.sugar

%find_lang %name

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%exclude %{_bindir}/sugar-activity
%{_bindir}/sugar-activity3
%{python3_sitelib}/*
%{_bindir}/sugar-activity-web
%{_rpmconfigdir}/macros.d/macros.sugar
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

%changelog
%autochangelog
