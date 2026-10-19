%global source0_hash 78c9400d55eeeb5ab75161360543f9376438c4da4934cb34cdda5b46021ae379
Name:           evemu
Version:        2.7.0
Release:        1%{?dist}
Summary:        Event Device Query and Emulation Program
License:        GPL-3.0-only AND LGPL-3.0-only AND GPL-3.0-or-later
URL:            http://www.freedesktop.org/wiki/Evemu
%if 0%{?gitdate}
Source0:        http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
%endif
%if %{with legacy_python}
%else
%endif
Requires:       libevdev >= 0.5
Requires:       %{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libevdev-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  xmlto
# /oreon:deps
%description
%{name} is a simple utility to capture the event stream from input devices
and replay that stream on a virtual input device.

%package libs
Summary:        Event Device Query and Emulation Program Library
License:        LGPL-3.0-or-later
Conflicts:      evemu < 2.7.0-8
%description libs
%{name} base library, used by the evemu tools.

%package devel
Summary:        Event Device Query and Emulation Program Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
%{name} development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build

autoreconf -v --install --force || exit 1
%if %{with legacy_python}
export PYTHON=python2
%else
export PYTHON=python3
%endif
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n evemu-libs -f %{oreon_filedir}/evemu-libs.list
%files -n evemu-devel -f %{oreon_filedir}/evemu-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.0-37
- Prepare for Oreon 11 (RP1)
