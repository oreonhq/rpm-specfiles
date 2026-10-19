%global source0_hash 18a59039adfb31ee6d65bb761ad6ed8c8a818af5995e6ec68ddf816898c00354
Summary:        InfiniBand fabric simulator for management
Name: ibsim
Version: 0.12
Release:        1%{?dist}
License: GPL-2.0-only OR LicenseRef-Callaway-BSD
Source0:        https://github.com/linux-rdma/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0027: 0027-run_opensm.sh-remove-opensm-c-option.patch
Url: https://github.com/linux-rdma/ibsim
ExcludeArch: s390 %{arm}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libibmad-devel
BuildRequires:  libibumad-devel
BuildRequires:  make
# /oreon:deps
%description
ibsim provides simulation of infiniband fabric for using with
OFA OpenSM, diagnostic and management tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install prefix=%{_prefix} libpath=%{_libdir} binpath=%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
