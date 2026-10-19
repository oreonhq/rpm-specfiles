%global source0_hash e800eafa4caf70d3b6b3db29c0ff9907ff416accfb7f324803f7014ef581a9c3
%define tagname 0.3
%define relvers 0
%define tsuffix g8ed9274
%define dsuffix 31b4926
%global debug_package %{nil}
Name:           gio-sharp
Version:        %{tagname}
Release:        37%{?dist}
Summary:        C# bindings for gio
License:        MIT
URL:            http://github.com/mono/%{name}
Source0:        mono-%{name}-%{version}-%{relvers}-%{tsuffix}.tar.gz
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  make
BuildRequires:  mono-devel
# /oreon:deps
%package devel
Summary:        Development files for gio-sharp
Requires:       gtk-sharp2-gapi
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}
%description
C# bindings for gio

%description devel
Development files for gio-sharp

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mono-%{name}-%{dsuffix}

sed -i "s#gmcs#mcs#g" configure.ac.in

%build

NOCONFIGURE=true ./autogen-2.22.sh
%configure
make # Parallel builds don't work
%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod 644 `find $RPM_BUILD_ROOT%{_prefix}/lib -name '*.dll.config'`
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gio-sharp-devel -f %{oreon_filedir}/gio-sharp-devel.list

%changelog

%autochangelog
