%global source0_hash c3131924029caad1e1251c02ed4d5c0636b62f025d4ee730f43d2a0684b64bd1
%global git_version 26_g604758e_open
%global MAKEARG PSM_HAVE_SCIF=0 MIC=0 arch=$(uname -m)
Name:           infinipath-psm
Summary:        Intel Performance Scaled Messaging (PSM) Libraries
Version:        3.3
Release:        1%{?dist}
License:        GPL-2.0-only OR LicenseRef-Callaway-BSD
ExclusiveArch:  x86_64
URL:            https://github.com/01org/psm
Source0:        %{name}-%{version}-%{git_version}.tar.gz
Source1:        ipath.rules
Patch1:         0001-fix-a-compilation-issue.patch
Patch3:         remove-executable-permissions-for-header-files.patch
Patch4:         0001-Include-sysmacros.h.patch
Patch5:         0001-Extend-buffer-for-uvalue-and-pvalue.patch
Patch6:         extend-fdesc-array.patch
Patch7:         psm-multiple-definition.patch
Patch8:         infinipath-psm-gcc11.patch
Patch9:         fix-clang-build.patch
Requires:       udev
%if "%{toolchain}" == "clang"
%else
%endif
Obsoletes:      infinipath-libs <= %{version}-%{release}
# oreon:deps
BuildRequires:  clang
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The PSM Messaging API, or PSM API, is Intel's low-level
user-level communications interface for the True Scale
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%package devel
Summary:        Development files for Intel PSM
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      infinipath-devel <= %{version}-%{release}
%description devel
Development files for the %{name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-%{git_version}
%patch -P1 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p0
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
find libuuid -type f -not -name 'psm_uuid.[c|h]' -not -name Makefile -delete

%build

%define _lto_cflags %{nil}
%{set_build_flags}
%make_build PSM_USE_SYS_UUID=1 %{MAKEARG}
%install
%make_install %{MAKEARG}
install -d %{buildroot}%{_udevrulesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/60-ipath.rules
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n infinipath-psm-devel -f %{oreon_filedir}/infinipath-psm-devel.list

%changelog

%autochangelog
