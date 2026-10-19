%global source0_hash 570c8e6cfe70260284bcaad7d63b42a401384bc2d15987cc6411ea7ee1b45c8e
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%global make_flags \\\
        LDFLAGS="%{__global_ldflags} -Lsrc" \\\
        LIBDIR=%{_libdir} \\\
        HWINFO_VERSION=%{version}
Name:           hwinfo
Version:        25.5
Release:        1%{?dist}
Summary:        Hardware information tool
License:        GPL-1.0-or-later
URL:            https://github.com/openSUSE/hwinfo
Source0:        https://github.com/openSUSE/hwinfo/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name} < 22.2-1
# oreon:deps
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  libx86emu-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
hwinfo is to probe for the hardware present in the system. It can be used to
generate a system overview log which can be later used for support.

%package libs
Summary:        Libraries for hwinfo
Obsoletes:      %{name} < 22.2-1
%description libs
Libraries for using hwinfo, a hardware information tool, in other applications.

%package devel
Summary:        Development files for hwinfo
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Header files and libraries for developing with libhd library from hwinfo, a
hardware information tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make %{make_flags}
%install
%make_install %{make_flags}
%ldconfig_scriptlets libs
%if "%{_sbindir}" == "%{_bindir}"
mv %{buildroot}/usr/sbin  %{buildroot}%{_sbindir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n hwinfo-libs -f %{oreon_filedir}/hwinfo-libs.list
%files -n hwinfo-devel -f %{oreon_filedir}/hwinfo-devel.list

%changelog

%autochangelog
