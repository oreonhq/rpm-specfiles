# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 78c9400d55eeeb5ab75161360543f9376438c4da4934cb34cdda5b46021ae379
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_without legacy_python
%endif

#global gitdate 20150818
#global gitversion eba96a4

Name:           evemu
Version:        2.7.0
Release:        37%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
Summary:        Event Device Query and Emulation Program

License:        GPL-3.0-only AND LGPL-3.0-only AND GPL-3.0-or-later
URL:            http://www.freedesktop.org/wiki/Evemu

%if 0%{?gitdate}
Source0:        http://www.freedesktop.org/software/evemu/evemu-2.7.0.tar.xz
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
%endif

BuildRequires:  automake libtool gcc gcc-c++ make
%if %{with legacy_python}
BuildRequires:  python2-devel
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  xmlto asciidoc
BuildRequires:  libevdev-devel >= 1.3
Requires:       libevdev >= 0.5
Requires:       %{name}-libs = %{version}-%{release}

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
%oreon_verify_sources
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

# We intentionally don't ship *.la files
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/evemu-describe
%{_bindir}/evemu-device
%{_bindir}/evemu-play
%{_bindir}/evemu-event
%{_bindir}/evemu-record
%{_mandir}/man1/evemu-*

%files libs
%{_libdir}/libevemu.so.*

%files devel
%{_includedir}/evemu.h
%{_libdir}/libevemu.so
%{_libdir}/pkgconfig/evemu.pc
%if %{with legacy_python}
%{python2_sitelib}/evemu
%else
%{python3_sitelib}/evemu
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.0-37
- Prepare for Oreon 11 (RP1)
