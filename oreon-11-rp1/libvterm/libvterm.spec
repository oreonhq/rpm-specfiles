%global source0_hash 09156f43dd2128bd347cbeebe50d9a571d32c64e0cf18d211197946aff7226e0
%global libname vterm
Name:           lib%{libname}
Version:        0.3.3
Release:        1%{?dist}
Summary:        An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator
License:        MIT
URL:            https://www.leonerd.org.uk/code/libvterm
Source0:        https://www.leonerd.org.uk/code/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
An abstract C99 library which implements a VT220 or xterm-like
terminal emulator. It does not use any particular graphics toolkit or
output system. Instead, it invokes callback function pointers that
its embedding program should provide it to draw on its behalf.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir}
%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%set_build_flags
%make_build test
%files -f %{oreon_filedir}/main.list
%files -n libvterm-devel -f %{oreon_filedir}/libvterm-devel.list
%files -n libvterm-tools -f %{oreon_filedir}/libvterm-tools.list

%changelog

%autochangelog
