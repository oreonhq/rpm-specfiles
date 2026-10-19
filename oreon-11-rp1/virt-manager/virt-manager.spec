%global source0_hash faa8e4cb594d4a205a12b221eba4e9c9c324eb4df152f8393f6f744279a90638
%global default_hvs         "qemu,xen,lxc"
%global have_spice          %{defined fedora}
Name: virt-manager
Version: 5.1.0
Release:        4%{?dist}
%global verrel %{version}-%{release}
Summary:        Desktop tool for managing virtual machines via libvirt
License: GPL-2.0-or-later
BuildArch: noarch
URL: https://virt-manager.org/
Source0:        https://codeload.github.com/virt-manager/virt-manager/tar.gz/refs/tags/v%{version}#/virt-manager-%{version}.tar.xz
Patch1: 0001-virtinst-cloudinit-include-empty-meta-data-file.patch
Requires: virt-manager-common = %{verrel}
Requires: python3-gobject >= 3.31.3
Requires: gtk3 >= 3.22.0
Requires: libvirt-glib >= 0.0.9
Requires: gtk-vnc2
%if %{have_spice}
Requires: spice-gtk3
%endif
%if ! 0%{?flatpak}
Requires: dconf
%endif
Requires: vte291
Recommends: gtksourceview4
Recommends: (libvirt-daemon-kvm or libvirt-daemon-qemu)
Recommends: libvirt-daemon-config-network
Suggests: python3-libguestfs
# oreon:deps
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
# /oreon:deps
%description
Virtual Machine Manager provides a graphical tool for administering virtual
machines for KVM, Xen, and LXC. Start, stop, add or remove virtual devices,
connect to a graphical or serial console, and see resource usage statistics
for existing VMs on local or remote machines. Uses libvirt as the backend
management API.

%package common
Summary: Common files used by the different Virtual Machine Manager interfaces
Requires: python3-argcomplete
Requires: python3-libvirt
Requires: python3-libxml2
Requires: python3-requests
Requires: libosinfo >= 0.2.10
Requires: python3-gobject-base
Requires: xorriso
%description common
Common files used by the different virt-manager interfaces, as well as
virt-install related tools.

%package -n virt-install
Summary: Utilities for installing virtual machines
Requires: virt-manager-common = %{verrel}
Requires: libvirt-client
Provides: virt-install
Provides: virt-clone
Provides: virt-xml
%description -n virt-install
Package includes several command line utilities, including virt-install
(build and install new VMs) and virt-clone (clone an existing virtual
machine).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if ! %{have_spice}
%global _default_graphics -Ddefault-graphics=vnc
%endif
%meson \
    -Ddefault-hvs=%{default_hvs} \
    %{?_default_graphics} \
    -Dupdate-icon-cache=false \
    -Dcompile-schemas=false \
    -Dtests=disabled
%meson_build
%install
%meson_install
%find_lang %{name}
%if 0%{?py_byte_compile:1}
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/virt-manager/
%oreon_autofiles virt-install usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n virt-manager-common -f %{oreon_filedir}/virt-manager-common.list
%files -n virt-install -f %{oreon_filedir}/virt-install.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.0-4
- Prepare for Oreon 11 (RP1)
