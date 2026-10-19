%global source0_hash 933de2e4d1b2211a638be463eb6e8616891bfba73aef5d38060bd8319baeefc6
%undefine _hardened_build
Name:           btop
Version:        1.4.7
Release:        1%{?dist}
Summary:        Modern and colorful command line resource monitor that shows usage and stats
License:        Apache-2.0 AND ISC AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/aristocratos/btop
Source0:        https://github.com/aristocratos/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?el8}
%endif
%if 0%{?el9}
%endif
Requires:       hicolor-icon-theme
Provides:       bundled(igt-gpu-tools) = 1.28^20240731git0f02dc17-1
Provides:       bundled(widecharwidth)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lowdown
BuildRequires:  make
BuildRequires:  rocm-smi-devel
# /oreon:deps
%description
Resource monitor that shows usage and stats for processor,
memory, disks, network and processes.

C++ version and continuation of bashtop and bpytop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{?el8:. /opt/rh/gcc-toolset-12/enable}
%{?el9:. /opt/rh/gcc-toolset-14/enable}
export CXXFLAGS="${CXXFLAGS} -g"
%if 0%{?el9}
sed -i '1i #define _GNU_SOURCE' src/linux/intel_gpu_top/intel_gpu_top.c
%endif
%make_build
%install
%make_install PREFIX=%{_prefix}
rm -fv %{buildroot}%{_datadir}/btop/README.md
desktop-file-validate %{buildroot}%{_datadir}/applications/btop.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
