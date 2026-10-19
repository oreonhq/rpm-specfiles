%global source0_hash 91fe411ac6889bcf6b70074f3c0dc62de9076a43e804fd7cc2009f8b008dbd6b
%define tagname 2.14.0
%define relvers 0
%define tsuffix ga2ff3c5
%define dsuffix 19023b6
%global debug_package %{nil}
Name:           gtk-sharp-beans
Version:        %{tagname}
Release:        1%{?dist}
Summary:        C# bindings for GTK+ API not included in GTK#
License:        LicenseRef-Callaway-LGPLv2
URL:            http://github.com/mono/%{name}
Source0:        mono-%{name}-%{version}-%{relvers}-%{tsuffix}.tar.gz
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gio-sharp-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  make
BuildRequires:  mono-devel
# /oreon:deps
%package devel
Summary:        Development files for gtk-sharp-beans
Requires:	pkgconfig
Requires:       %{name} = %{version}-%{release}
%description
C# bindings for GTK+ API not included in GTK#

%description devel
Development files for gtk-sharp-beans

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mono-%{name}-%{dsuffix}
sed -i "s#gmcs#mcs#g" configure.ac

%build

NOCONFIGURE=true ./autogen.sh
%configure
make #%{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gtk-sharp-beans-devel -f %{oreon_filedir}/gtk-sharp-beans-devel.list

%changelog

%autochangelog
