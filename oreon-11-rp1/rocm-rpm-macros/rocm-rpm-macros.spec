%global source0_hash f3629cdf4ebb19129b567bdf4ec9bc2c79e935f7ce97fffd2108d3e309aaab25
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_suffix -%{rocm_release}
%else
%global pkg_suffix %{nil}
%endif
%global pkg_name rocm-rpm-macros%{pkg_suffix}
Name:           %{pkg_name}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm RPM macros
License:        GPL-2.0-or-later
URL:            https://github.com/trixirt/rocm-rpm-macros
Source0:        macros.rocm
Source1:        GPL
Source2:        default
Source3:        gfx8
Source4:        gfx9
Source5:        gfx10
Source6:        gfx11
Source7:        gfx906
Source8:        gfx908
Source9:        gfx90a
Source10:       gfx942
Source11:       gfx1031
Source12:       gfx1036
Source13:       gfx1100
Source14:       gfx1101
Source15:       gfx1102
Source16:       gfx1103
Source17:       default.rhel
Source18:       gfx12
Source19:       gfx950
Source30:       rocm-7.1
%global debug_package %{nil}
Requires:       rpm
%if 0%{?suse_version}
Requires:       Modules
%else
Requires:       environment-modules
%endif
BuildArch: noarch
ExclusiveArch:  x86_64
# oreon:deps

# /oreon:deps
%description
This package contains ROCm RPM macros for building ROCm packages.

# To use, run
# $> source /etc/profile.d/modules.sh
%package modules
Summary: ROCm enviroment modules
%if 0%{?suse_version}
Requires:       Modules
%else
Requires: environment(modules)
Requires: cmake-filesystem
Requires: rocm-llvm-filesystem
%endif
%description modules
This package contains ROCm environment modules for switching
between different GPU families.

%prep

%setup -cT
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
mkdir modules
install -pm 644 %{SOURCE2} modules
install -pm 644 %{SOURCE3} modules
install -pm 644 %{SOURCE4} modules
install -pm 644 %{SOURCE5} modules
install -pm 644 %{SOURCE6} modules
install -pm 644 %{SOURCE7} modules
install -pm 644 %{SOURCE8} modules
install -pm 644 %{SOURCE9} modules
install -pm 644 %{SOURCE10} modules
install -pm 644 %{SOURCE11} modules
install -pm 644 %{SOURCE12} modules
install -pm 644 %{SOURCE13} modules
install -pm 644 %{SOURCE14} modules
install -pm 644 %{SOURCE15} modules
install -pm 644 %{SOURCE16} modules
install -pm 644 %{SOURCE18} modules
install -pm 644 %{SOURCE19} modules
# compat modules
install -pm 644 %{SOURCE30} modules

%install
mkdir -p %{buildroot}%{_rpmmacrodir}/
install -Dpm 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/
%if 0%{?suse_version}
mkdir -p %{buildroot}%{_datadir}/modules/rocm/
cp -p modules/* %{buildroot}%{_datadir}/modules/rocm/
%else
mkdir -p %{buildroot}%{_datadir}/modulefiles/rocm/
cp -p modules/* %{buildroot}%{_datadir}/modulefiles/rocm/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n rocm-rpm-macros-7.1-modules -f %{oreon_filedir}/rocm-rpm-macros-7.1-modules.list

%changelog

%autochangelog
