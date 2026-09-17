%global source0_hash 4beb90172c6acaac08c1b4a5112fb616772e214a7ef992bcbd461453295a58be

%undefine _hardened_build

Name:           btop
Version:        1.4.6
Release:        4%{?dist}
Summary:        Modern and colorful command line resource monitor that shows usage and stats

# The entire source code is ASL 2.0 except:
# ISC:
#  - src/openbsd/internal.h
#  - src/openbsd/sysctlbyname.cpp
#  - src/openbsd/sysctlbyname.h
# MIT:
#  - include/fmt/
#  - src/linux/intel_gpu_top/
# Public Domain
#  - include/widechar_width.hpp
License:        Apache-2.0 AND ISC AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/aristocratos/btop
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  lowdown
%if 0%{?el8}
BuildRequires:  gcc-toolset-12-gcc-c++
BuildRequires:  gcc-toolset-12-annobin-plugin-gcc
BuildRequires:  gcc-toolset-12-binutils
%endif
%if 0%{?el9}
BuildRequires:  gcc-toolset-14-gcc-c++
BuildRequires:  gcc-toolset-14-gcc-plugin-annobin
BuildRequires:  gcc-toolset-14-binutils
%endif

# AMD GPU support
%if 0%{?fedora}
%ifnarch i686 s390x
BuildRequires:  rocm-smi-devel
Recommends: rocm-smi
%endif
%endif

Requires:       hicolor-icon-theme

# Include file from https://gitlab.freedesktop.org/drm/igt-gpu-tools
# Snapshot from 0f02dc176959e6296866b1bafd3982e277a5e44b
Provides:       bundled(igt-gpu-tools) = 1.28^20240731git0f02dc17-1
# Bundling was chosen for widecharwidth as it is not versioned upstream
# and doesn't appear to be a widely-used lib.
Provides:       bundled(widecharwidth)

%description
Resource monitor that shows usage and stats for processor,
memory, disks, network and processes.

C++ version and continuation of bashtop and bpytop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{?el8:. /opt/rh/gcc-toolset-12/enable}
%{?el9:. /opt/rh/gcc-toolset-14/enable}

# to build debuginfo
export CXXFLAGS="${CXXFLAGS} -g"
# fix build error on epel9 using non-standard functions in older glibc
%if 0%{?el9}
sed -i '1i #define _GNU_SOURCE' src/linux/intel_gpu_top/intel_gpu_top.c
%endif
%make_build

%install
%make_install PREFIX=%{_prefix}
rm -fv %{buildroot}%{_datadir}/btop/README.md
desktop-file-validate %{buildroot}%{_datadir}/applications/btop.desktop

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/btop.desktop
%{_datadir}/btop
%{_datadir}/icons/hicolor/*/apps/btop.*
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
