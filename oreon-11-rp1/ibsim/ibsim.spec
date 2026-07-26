%global source0_hash 18a59039adfb31ee6d65bb761ad6ed8c8a818af5995e6ec68ddf816898c00354

Summary: InfiniBand fabric simulator for management
Name: ibsim
Version: 0.12
Release: 2%{?dist}
# Automatically converted from old format: GPLv2 or BSD - review is highly recommended.
License: GPL-2.0-only OR LicenseRef-Callaway-BSD
Source: https://github.com/linux-rdma/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0027: 0027-run_opensm.sh-remove-opensm-c-option.patch

Url: https://github.com/linux-rdma/ibsim
BuildRequires: libibmad-devel, libibumad-devel, gcc
BuildRequires: make

# RDMA is not currently built on 32-bit ARM: #1484155
ExcludeArch: s390 %{arm}

%description
ibsim provides simulation of infiniband fabric for using with
OFA OpenSM, diagnostic and management tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -v -p1

%build
%set_build_flags
%make_build

%install
%make_install prefix=%{_prefix} libpath=%{_libdir} binpath=%{_bindir}

%files
%{_libdir}/umad2sim/
%{_bindir}/ibsim
%{_bindir}/ibsim-run
%doc README TODO net-examples scripts
%license COPYING

%changelog
%autochangelog
