%global source0_hash 2b508b28d75fe30967de0650dcc67aaacfa579e707b043a2e43785c315039c57
%undefine _hardened_build
Name:    sugar-toolkit-gtk3
Version: 0.121
Release:        1%{?dist}
Summary:        Sugar toolkit GTK+ 3
License: LicenseRef-Callaway-LGPLv2+
URL:     http://wiki.laptop.org/go/Sugar
Source0:        http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Source1: macros.sugar
Patch0: Fix-logging-usage.patch
Requires: python3-dateutil
Requires: python3-dbus
Requires: python3-gobject
Requires: python3-decorator
Requires: gettext-runtime
Requires: sugar-datastore
Requires: unzip
Requires: webkit2gtk4.1
Requires: git-core
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libSM-devel
BuildRequires:  librsvg2-devel
BuildRequires:  make
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
# /oreon:deps
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
%oreon_prep
%build

autoreconf
ls -1 %{_datadir}/automake-*/py-compile | sort | \
	tail -n 1 | while read f
do
	cp -p $f .
done
%configure
make -O V=1 VERBOSE=1
%install
%make_install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -pm 644 %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d/macros.sugar
%find_lang %name
find %{buildroot} -type f -name "*.la" -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sugar-toolkit-gtk3-devel -f %{oreon_filedir}/sugar-toolkit-gtk3-devel.list

%changelog

%autochangelog
