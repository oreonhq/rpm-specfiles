%global source0_hash b70576ee89adb5f0be404b0d4e714623b10d6d9d1a041ebdf11f8a423f95be1d

Name:           open-vmdk
Version:        0.3.12
Release:        1%{?dist}
Summary:        Tools to create OVA files from raw disk images
License:        Apache-2.0
URL:            https://github.com/vmware/open-vmdk
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
Requires:       coreutils
Requires:       grep
Requires:       python3-PyYAML
Requires:       python3-lxml
Requires:       sed
Requires:       tar
Requires:       util-linux

%description
Open VMDK is an assistant tool for creating Open Virtual Appliance (OVA).
An OVA is a tar archive file with Open Virtualization Format (OVF) files
inside, which is composed of an OVF descriptor with extension .ovf,
one or more virtual machine disk image files with extension .vmdk,
and a manifest file with extension .mf.

%files
%{_bindir}/mkova.sh
%{_bindir}/ova-compose
%{_bindir}/vmdk-convert
%{_datadir}/%{name}/
%config(noreplace) %{_sysconfdir}/open-vmdk.conf

%dnl ---------------------------------------------------------------------

%package -n ovfenv
Summary:       Tools to get or set OVF environment variables
Requires:      open-vm-tools
Requires:      python3-libxml2
BuildArch:     noarch

%description -n ovfenv
Show the value of an OVF property, whether the properties
were presented to this VM in guestinfo or on a cdrom.
Optionally, allows a property value to be modified.

%files -n ovfenv
%{_bindir}/ovfenv
%dir %{_sharedstatedir}/ovfenv

%dnl ---------------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{!?_auto_set_build_flags:%{set_build_flags}}
%make_build

%install
%make_install

# Fix shebang for ovfenv
%py3_shebang_fix %{buildroot}%{_bindir}/ovfenv

install -m0644 templates/*.ovf %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_sharedstatedir}/ovfenv

%changelog
%autochangelog
