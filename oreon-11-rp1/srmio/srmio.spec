%global source0_hash 8de4681af802316af621e838eec014bbea5dd11546065f5e1ac29ff3bea4de6e
%global realver 0.1.1git1
Name:           srmio
Version:        0.1.1.1
Release:        15%{?dist}
Summary:        Schoberer Radmesstechnik (SRM) PowerControl access
License:        MIT
URL:            http://www.zuto.de/project/srmio/
Source0:        https://github.com/rclasen/%{name}/archive/v%{realver}.tar.gz#/%{name}-%{realver}.tar.gz
Patch0:         srmio-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
App to access the most important functions of a Schoberer
Radmesstechnik (SRM) PowerControl V, VI and 7. You can download the data,
mark it deleted, sync the time and set the recording interval.

%package libs
Summary:        Library for %{name}
%description libs
This package contains library for %{name}.

%package devel
Summary:        Header files and development documentation for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and development documentation
for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{realver}

%build

autoreconf -vfi
%configure \
    --enable-static=no
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n srmio-libs -f %{oreon_filedir}/srmio-libs.list
%files -n srmio-devel -f %{oreon_filedir}/srmio-devel.list

%changelog

%autochangelog
