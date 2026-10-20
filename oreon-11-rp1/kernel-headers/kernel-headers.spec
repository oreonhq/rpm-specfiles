%global source0_hash fd0fc479f983a8c05313f13e9c36330fe6651cf725396748c40d5cd93fa1e6a4
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: kernel-headers
Version: 7.2.11
Release: 1%{?dist}
Summary: Linux kernel headers
License: GPL-2.0-only WITH Linux-syscall-note
URL: https://kernel.org/
Source0: https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: make
%endif

%description
The Linux kernel is the core of any Linux operating system. It manages hardware, system resources, and provides the fundamental services for all other software.

%prep
%oreon_sha256
%autosetup -n linux-%{version} -p1

%build
:

%install
%ifarch x86_64
make -s headers ARCH=x86
%endif
%ifarch aarch64
make -s headers ARCH=arm64
%endif
mkdir -p %{buildroot}/usr
cp -a usr/include %{buildroot}/usr/
find %{buildroot}%{_includedir} \( -name '.*' -o -name '*.orig' -o -type f ! -name '*.h' \) -delete

%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING

%changelog
* Mon Oct 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.2.11-1
- 7.2.11
