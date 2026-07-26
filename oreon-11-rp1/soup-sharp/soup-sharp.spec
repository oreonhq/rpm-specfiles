%global source0_hash 8e07c1cb5cf40d69cb162d6abdcd3df3f825b3cbaae6c5d00bf3a80c80973fdb

%global commit          0f36d103e567da1d1a8b5c43e1457c3d0c30393b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20190810

Name:       soup-sharp
Version:    2.42.2
Release:    15.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:    .NET bindings for libsoup

License:    LGPL-3.0-or-later
URL:        https://github.com/stsundermann/soup-sharp
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: make
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  pkgconfig(gapi-3.0)
BuildRequires:  pkgconfig(monodoc)
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
Requires:       pkgconfig(gapi-3.0)

ExclusiveArch:  %{mono_arches}

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
# No parallel make, race condition with monodoc
make

%install
%make_install
# remove .la files
rm -f %{buildroot}%{_libdir}/libsoupsharpglue-%{version}.la

%files
%doc AUTHORS README.md
%license COPYING
%{_monodir}/
%{_datadir}/gapi-3.0/soup-sharp-api.xml
%{_libdir}/libsoupsharpglue-%{version}.so

%files devel
%{_libdir}/pkgconfig/soup-sharp-*.pc

%files doc
%{_prefix}/lib/monodoc/sources/soup-sharp*

%changelog
%autochangelog
