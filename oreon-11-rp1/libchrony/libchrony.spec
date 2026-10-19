%global source0_hash fce931c6120273b3fb6706221935554e370804e8e9948fc9ccb28d895e83fb7d
Name:           libchrony
Version:        0.2
Release:        1%{?dist}
Summary:        Library for monitoring chronyd
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/chrony/libchrony
Source0:        https://gitlab.com/chrony/libchrony/-/archive/%{version}/libchrony-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libchrony is a C library for monitoring chronyd. It communicates with
chronyd directly over Unix domain or UDP socket, not relying on chronyc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%install
%make_install libdir=%{_libdir} includedir=%{_includedir}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}
%{?ldconfig_scriptlets}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libchrony-devel -f %{oreon_filedir}/libchrony-devel.list

%changelog

%autochangelog
