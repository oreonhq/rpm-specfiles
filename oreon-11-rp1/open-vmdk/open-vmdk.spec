%global source0_hash 32ec77a8aa1cb65d7683bd2e3f2921d8537ba9cbcda425bc8a25e111fb939cdd
Name:           open-vmdk
Version:        3.0.1
Release:        1%{?dist}
Summary:        Tools to create OVA files from raw disk images
License:        Apache-2.0
URL:            https://github.com/vmware/open-vmdk
Source0:        https://github.com/vmware/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       coreutils
Requires:       grep
Requires:       python3-PyYAML
Requires:       python3-lxml
Requires:       sed
Requires:       tar
Requires:       util-linux
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Open VMDK is an assistant tool for creating Open Virtual Appliance (OVA).
An OVA is a tar archive file with Open Virtualization Format (OVF) files
inside, which is composed of an OVF descriptor with extension .ovf,
one or more virtual machine disk image files with extension .vmdk,
and a manifest file with extension .mf.

%package -n ovfenv
Summary:       Tools to get or set OVF environment variables
Requires:      open-vm-tools
Requires:      python3-libxml2
BuildArch:     noarch
%description -n ovfenv
Show the value of an OVF property, whether the properties
were presented to this VM in guestinfo or on a cdrom.
Optionally, allows a property value to be modified.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{!?_auto_set_build_flags:%{set_build_flags}}
%make_build
%install
%make_install
%py3_shebang_fix %{buildroot}%{_bindir}/ovfenv
install -m0644 templates/*.ovf %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_sharedstatedir}/ovfenv
%oreon_autofiles ovfenv usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ovfenv -f %{oreon_filedir}/ovfenv.list

%changelog

%autochangelog
