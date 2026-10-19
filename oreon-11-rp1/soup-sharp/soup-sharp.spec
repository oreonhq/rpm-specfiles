%global source0_hash 8e07c1cb5cf40d69cb162d6abdcd3df3f825b3cbaae6c5d00bf3a80c80973fdb
%global commit          0f36d103e567da1d1a8b5c43e1457c3d0c30393b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20190810
Name:       soup-sharp
Version:    2.42.2
Release:        1%{?dist}
Summary:        .NET bindings for libsoup
License:    LGPL-3.0-or-later
URL:        https://github.com/stsundermann/soup-sharp
Source0:        https://github.com/stsundermann/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Requires:       pkgconfig(gapi-3.0)
ExclusiveArch:  %{mono_arches}
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gapi-3.0)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(monodoc)
# /oreon:deps
%description
WebKit-sharp is .NET bindings for the WebKit rendering engine.

%package devel
Summary:    Development files for soup-sharp
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
%description devel
Development files for soup-sharp.

%package doc
Summary:        Documentation files for soup-sharp
Requires:       %{name} = %{version}-%{release}
Requires:       monodoc
BuildArch:      noarch
%description doc
Documentation files for soup-sharp

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}
sed -i "s|\r||g" AUTHORS

%build

NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
make
%install
%make_install
rm -f %{buildroot}%{_libdir}/libsoupsharpglue-%{version}.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n soup-sharp-devel -f %{oreon_filedir}/soup-sharp-devel.list
%files -n soup-sharp-doc -f %{oreon_filedir}/soup-sharp-doc.list

%changelog

%autochangelog
