%global source0_hash ae137229bcbd6cdf0f7b80a31df61766145077ddf49416a728b02cb3921ff3fc
%bcond check 1
%global debug_package %{nil}
%global crate windows-sys
Name:           rust-windows-sys
Version:        0.61.2
Release:        1%{?dist}
Summary:        Rust for Windows
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/windows-sys
Source0:        https://static.crates.io/crates/windows-sys/windows-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk-devel

This package contains library source intended for building other packages which
use the "Wdk" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Devices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Devices-devel

This package contains library source intended for building other packages which
use the "Wdk_Devices" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Devices_Bluetooth-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Devices_Bluetooth-devel

This package contains library source intended for building other packages which
use the "Wdk_Devices_Bluetooth" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Devices_HumanInterfaceDevice-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Devices_HumanInterfaceDevice-devel

This package contains library source intended for building other packages which
use the "Wdk_Devices_HumanInterfaceDevice" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Foundation-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Foundation-devel

This package contains library source intended for building other packages which
use the "Wdk_Foundation" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Graphics-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Graphics-devel

This package contains library source intended for building other packages which
use the "Wdk_Graphics" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Graphics_Direct3D-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Graphics_Direct3D-devel

This package contains library source intended for building other packages which
use the "Wdk_Graphics_Direct3D" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_NetworkManagement-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_NetworkManagement-devel

This package contains library source intended for building other packages which
use the "Wdk_NetworkManagement" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_NetworkManagement_Ndis-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_NetworkManagement_Ndis-devel

This package contains library source intended for building other packages which
use the "Wdk_NetworkManagement_Ndis" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_NetworkManagement_WindowsFilteringPlatform-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_NetworkManagement_WindowsFilteringPlatform-devel

This package contains library source intended for building other packages which
use the "Wdk_NetworkManagement_WindowsFilteringPlatform" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Storage-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Storage-devel

This package contains library source intended for building other packages which
use the "Wdk_Storage" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Storage_FileSystem-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Storage_FileSystem-devel

This package contains library source intended for building other packages which
use the "Wdk_Storage_FileSystem" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_Storage_FileSystem_Minifilters-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_Storage_FileSystem_Minifilters-devel

This package contains library source intended for building other packages which
use the "Wdk_Storage_FileSystem_Minifilters" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_System-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_System-devel

This package contains library source intended for building other packages which
use the "Wdk_System" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_System_IO-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_System_IO-devel

This package contains library source intended for building other packages which
use the "Wdk_System_IO" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_System_Memory-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_System_Memory-devel

This package contains library source intended for building other packages which
use the "Wdk_System_Memory" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_System_OfflineRegistry-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_System_OfflineRegistry-devel

This package contains library source intended for building other packages which
use the "Wdk_System_OfflineRegistry" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_System_Registry-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_System_Registry-devel

This package contains library source intended for building other packages which
use the "Wdk_System_Registry" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_System_SystemInformation-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_System_SystemInformation-devel

This package contains library source intended for building other packages which
use the "Wdk_System_SystemInformation" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_System_SystemServices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_System_SystemServices-devel

This package contains library source intended for building other packages which
use the "Wdk_System_SystemServices" feature of the "%{crate}" crate.

%package     -n %{name}+Wdk_System_Threading-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Wdk_System_Threading-devel

This package contains library source intended for building other packages which
use the "Wdk_System_Threading" feature of the "%{crate}" crate.

%package     -n %{name}+Win32-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32-devel

This package contains library source intended for building other packages which
use the "Win32" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Data-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Data-devel

This package contains library source intended for building other packages which
use the "Win32_Data" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Data_HtmlHelp-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Data_HtmlHelp-devel

This package contains library source intended for building other packages which
use the "Win32_Data_HtmlHelp" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Data_RightsManagement-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Data_RightsManagement-devel

This package contains library source intended for building other packages which
use the "Win32_Data_RightsManagement" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices-devel

This package contains library source intended for building other packages which
use the "Win32_Devices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_AllJoyn-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_AllJoyn-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_AllJoyn" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Beep-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Beep-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Beep" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_BiometricFramework-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_BiometricFramework-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_BiometricFramework" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Bluetooth-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Bluetooth-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Bluetooth" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Cdrom-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Cdrom-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Cdrom" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Communication-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Communication-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Communication" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_DeviceAndDriverInstallation-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_DeviceAndDriverInstallation-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_DeviceAndDriverInstallation" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_DeviceQuery-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_DeviceQuery-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_DeviceQuery" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Display-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Display-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Display" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Dvd-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Dvd-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Dvd" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Enumeration-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Enumeration-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Enumeration" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Enumeration_Pnp-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Enumeration_Pnp-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Enumeration_Pnp" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Fax-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Fax-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Fax" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_HumanInterfaceDevice-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_HumanInterfaceDevice-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_HumanInterfaceDevice" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Nfc-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Nfc-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Nfc" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Nfp-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Nfp-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Nfp" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_PortableDevices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_PortableDevices-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_PortableDevices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Properties-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Properties-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Properties" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Pwm-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Pwm-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Pwm" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Sensors-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Sensors-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Sensors" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_SerialCommunication-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_SerialCommunication-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_SerialCommunication" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Tapi-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Tapi-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Tapi" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_Usb-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_Usb-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_Usb" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Devices_WebServicesOnDevices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Devices_WebServicesOnDevices-devel

This package contains library source intended for building other packages which
use the "Win32_Devices_WebServicesOnDevices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Foundation-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Foundation-devel

This package contains library source intended for building other packages which
use the "Win32_Foundation" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Gaming-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Gaming-devel

This package contains library source intended for building other packages which
use the "Win32_Gaming" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Globalization-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Globalization-devel

This package contains library source intended for building other packages which
use the "Win32_Globalization" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Graphics-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Graphics-devel

This package contains library source intended for building other packages which
use the "Win32_Graphics" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Graphics_Dwm-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Graphics_Dwm-devel

This package contains library source intended for building other packages which
use the "Win32_Graphics_Dwm" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Graphics_Gdi-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Graphics_Gdi-devel

This package contains library source intended for building other packages which
use the "Win32_Graphics_Gdi" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Graphics_GdiPlus-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Graphics_GdiPlus-devel

This package contains library source intended for building other packages which
use the "Win32_Graphics_GdiPlus" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Graphics_Hlsl-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Graphics_Hlsl-devel

This package contains library source intended for building other packages which
use the "Win32_Graphics_Hlsl" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Graphics_OpenGL-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Graphics_OpenGL-devel

This package contains library source intended for building other packages which
use the "Win32_Graphics_OpenGL" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Graphics_Printing-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Graphics_Printing-devel

This package contains library source intended for building other packages which
use the "Win32_Graphics_Printing" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Graphics_Printing_PrintTicket-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Graphics_Printing_PrintTicket-devel

This package contains library source intended for building other packages which
use the "Win32_Graphics_Printing_PrintTicket" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Management-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Management-devel

This package contains library source intended for building other packages which
use the "Win32_Management" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Management_MobileDeviceManagementRegistration-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Management_MobileDeviceManagementRegistration-devel

This package contains library source intended for building other packages which
use the "Win32_Management_MobileDeviceManagementRegistration" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Media-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Media-devel

This package contains library source intended for building other packages which
use the "Win32_Media" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Media_Audio-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Media_Audio-devel

This package contains library source intended for building other packages which
use the "Win32_Media_Audio" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Media_DxMediaObjects-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Media_DxMediaObjects-devel

This package contains library source intended for building other packages which
use the "Win32_Media_DxMediaObjects" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Media_KernelStreaming-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Media_KernelStreaming-devel

This package contains library source intended for building other packages which
use the "Win32_Media_KernelStreaming" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Media_Multimedia-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Media_Multimedia-devel

This package contains library source intended for building other packages which
use the "Win32_Media_Multimedia" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Media_Streaming-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Media_Streaming-devel

This package contains library source intended for building other packages which
use the "Win32_Media_Streaming" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Media_WindowsMediaFormat-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Media_WindowsMediaFormat-devel

This package contains library source intended for building other packages which
use the "Win32_Media_WindowsMediaFormat" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_Dhcp-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_Dhcp-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_Dhcp" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_Dns-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_Dns-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_Dns" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_InternetConnectionWizard-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_InternetConnectionWizard-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_InternetConnectionWizard" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_IpHelper-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_IpHelper-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_IpHelper" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_Multicast-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_Multicast-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_Multicast" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_Ndis-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_Ndis-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_Ndis" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_NetBios-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_NetBios-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_NetBios" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_NetManagement-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_NetManagement-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_NetManagement" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_NetShell-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_NetShell-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_NetShell" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_NetworkDiagnosticsFramework-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_NetworkDiagnosticsFramework-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_NetworkDiagnosticsFramework" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_P2P-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_P2P-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_P2P" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_QoS-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_QoS-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_QoS" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_Rras-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_Rras-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_Rras" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_Snmp-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_Snmp-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_Snmp" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_WNet-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_WNet-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_WNet" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_WebDav-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_WebDav-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_WebDav" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_WiFi-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_WiFi-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_WiFi" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_WindowsConnectionManager-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_WindowsConnectionManager-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_WindowsConnectionManager" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_WindowsFilteringPlatform-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_WindowsFilteringPlatform-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_WindowsFilteringPlatform" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_WindowsFirewall-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_WindowsFirewall-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_WindowsFirewall" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_NetworkManagement_WindowsNetworkVirtualization-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_NetworkManagement_WindowsNetworkVirtualization-devel

This package contains library source intended for building other packages which
use the "Win32_NetworkManagement_WindowsNetworkVirtualization" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking-devel

This package contains library source intended for building other packages which
use the "Win32_Networking" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_ActiveDirectory-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_ActiveDirectory-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_ActiveDirectory" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_Clustering-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_Clustering-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_Clustering" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_HttpServer-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_HttpServer-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_HttpServer" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_Ldap-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_Ldap-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_Ldap" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_WebSocket-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_WebSocket-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_WebSocket" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_WinHttp-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_WinHttp-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_WinHttp" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_WinInet-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_WinInet-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_WinInet" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_WinSock-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_WinSock-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_WinSock" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Networking_WindowsWebServices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Networking_WindowsWebServices-devel

This package contains library source intended for building other packages which
use the "Win32_Networking_WindowsWebServices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security-devel

This package contains library source intended for building other packages which
use the "Win32_Security" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_AppLocker-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_AppLocker-devel

This package contains library source intended for building other packages which
use the "Win32_Security_AppLocker" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Authentication-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Authentication-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Authentication" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Authentication_Identity-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Authentication_Identity-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Authentication_Identity" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Authorization-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Authorization-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Authorization" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Credentials-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Credentials-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Credentials" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Cryptography-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Cryptography-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Cryptography" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Cryptography_Catalog-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Cryptography_Catalog-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Cryptography_Catalog" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Cryptography_Certificates-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Cryptography_Certificates-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Cryptography_Certificates" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Cryptography_Sip-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Cryptography_Sip-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Cryptography_Sip" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Cryptography_UI-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Cryptography_UI-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Cryptography_UI" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_DiagnosticDataQuery-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_DiagnosticDataQuery-devel

This package contains library source intended for building other packages which
use the "Win32_Security_DiagnosticDataQuery" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_DirectoryServices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_DirectoryServices-devel

This package contains library source intended for building other packages which
use the "Win32_Security_DirectoryServices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_EnterpriseData-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_EnterpriseData-devel

This package contains library source intended for building other packages which
use the "Win32_Security_EnterpriseData" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_ExtensibleAuthenticationProtocol-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_ExtensibleAuthenticationProtocol-devel

This package contains library source intended for building other packages which
use the "Win32_Security_ExtensibleAuthenticationProtocol" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_Isolation-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_Isolation-devel

This package contains library source intended for building other packages which
use the "Win32_Security_Isolation" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_LicenseProtection-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_LicenseProtection-devel

This package contains library source intended for building other packages which
use the "Win32_Security_LicenseProtection" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_NetworkAccessProtection-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_NetworkAccessProtection-devel

This package contains library source intended for building other packages which
use the "Win32_Security_NetworkAccessProtection" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_WinTrust-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_WinTrust-devel

This package contains library source intended for building other packages which
use the "Win32_Security_WinTrust" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Security_WinWlx-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Security_WinWlx-devel

This package contains library source intended for building other packages which
use the "Win32_Security_WinWlx" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage-devel

This package contains library source intended for building other packages which
use the "Win32_Storage" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Cabinets-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Cabinets-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Cabinets" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_CloudFilters-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_CloudFilters-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_CloudFilters" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Compression-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Compression-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Compression" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_DistributedFileSystem-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_DistributedFileSystem-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_DistributedFileSystem" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_FileHistory-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_FileHistory-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_FileHistory" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_FileSystem-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_FileSystem-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_FileSystem" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Imapi-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Imapi-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Imapi" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_IndexServer-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_IndexServer-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_IndexServer" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_InstallableFileSystems-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_InstallableFileSystems-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_InstallableFileSystems" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_IscsiDisc-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_IscsiDisc-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_IscsiDisc" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Jet-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Jet-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Jet" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Nvme-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Nvme-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Nvme" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_OfflineFiles-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_OfflineFiles-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_OfflineFiles" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_OperationRecorder-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_OperationRecorder-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_OperationRecorder" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Packaging-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Packaging-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Packaging" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Packaging_Appx-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Packaging_Appx-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Packaging_Appx" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_ProjectedFileSystem-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_ProjectedFileSystem-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_ProjectedFileSystem" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_StructuredStorage-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_StructuredStorage-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_StructuredStorage" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Vhd-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Vhd-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Vhd" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Storage_Xps-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Storage_Xps-devel

This package contains library source intended for building other packages which
use the "Win32_Storage_Xps" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System-devel

This package contains library source intended for building other packages which
use the "Win32_System" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_AddressBook-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_AddressBook-devel

This package contains library source intended for building other packages which
use the "Win32_System_AddressBook" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Antimalware-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Antimalware-devel

This package contains library source intended for building other packages which
use the "Win32_System_Antimalware" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_ApplicationInstallationAndServicing-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_ApplicationInstallationAndServicing-devel

This package contains library source intended for building other packages which
use the "Win32_System_ApplicationInstallationAndServicing" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_ApplicationVerifier-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_ApplicationVerifier-devel

This package contains library source intended for building other packages which
use the "Win32_System_ApplicationVerifier" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_ClrHosting-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_ClrHosting-devel

This package contains library source intended for building other packages which
use the "Win32_System_ClrHosting" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Com-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Com-devel

This package contains library source intended for building other packages which
use the "Win32_System_Com" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Com_Marshal-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Com_Marshal-devel

This package contains library source intended for building other packages which
use the "Win32_System_Com_Marshal" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Com_StructuredStorage-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Com_StructuredStorage-devel

This package contains library source intended for building other packages which
use the "Win32_System_Com_StructuredStorage" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Com_Urlmon-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Com_Urlmon-devel

This package contains library source intended for building other packages which
use the "Win32_System_Com_Urlmon" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_ComponentServices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_ComponentServices-devel

This package contains library source intended for building other packages which
use the "Win32_System_ComponentServices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Console-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Console-devel

This package contains library source intended for building other packages which
use the "Win32_System_Console" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_CorrelationVector-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_CorrelationVector-devel

This package contains library source intended for building other packages which
use the "Win32_System_CorrelationVector" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_DataExchange-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_DataExchange-devel

This package contains library source intended for building other packages which
use the "Win32_System_DataExchange" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_DeploymentServices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_DeploymentServices-devel

This package contains library source intended for building other packages which
use the "Win32_System_DeploymentServices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_DeveloperLicensing-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_DeveloperLicensing-devel

This package contains library source intended for building other packages which
use the "Win32_System_DeveloperLicensing" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Diagnostics-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Diagnostics-devel

This package contains library source intended for building other packages which
use the "Win32_System_Diagnostics" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Diagnostics_Ceip-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Diagnostics_Ceip-devel

This package contains library source intended for building other packages which
use the "Win32_System_Diagnostics_Ceip" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Diagnostics_Debug-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Diagnostics_Debug-devel

This package contains library source intended for building other packages which
use the "Win32_System_Diagnostics_Debug" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Diagnostics_Debug_Extensions-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Diagnostics_Debug_Extensions-devel

This package contains library source intended for building other packages which
use the "Win32_System_Diagnostics_Debug_Extensions" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Diagnostics_Etw-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Diagnostics_Etw-devel

This package contains library source intended for building other packages which
use the "Win32_System_Diagnostics_Etw" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Diagnostics_ProcessSnapshotting-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Diagnostics_ProcessSnapshotting-devel

This package contains library source intended for building other packages which
use the "Win32_System_Diagnostics_ProcessSnapshotting" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Diagnostics_ToolHelp-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Diagnostics_ToolHelp-devel

This package contains library source intended for building other packages which
use the "Win32_System_Diagnostics_ToolHelp" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Diagnostics_TraceLogging-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Diagnostics_TraceLogging-devel

This package contains library source intended for building other packages which
use the "Win32_System_Diagnostics_TraceLogging" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_DistributedTransactionCoordinator-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_DistributedTransactionCoordinator-devel

This package contains library source intended for building other packages which
use the "Win32_System_DistributedTransactionCoordinator" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Environment-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Environment-devel

This package contains library source intended for building other packages which
use the "Win32_System_Environment" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_ErrorReporting-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_ErrorReporting-devel

This package contains library source intended for building other packages which
use the "Win32_System_ErrorReporting" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_EventCollector-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_EventCollector-devel

This package contains library source intended for building other packages which
use the "Win32_System_EventCollector" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_EventLog-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_EventLog-devel

This package contains library source intended for building other packages which
use the "Win32_System_EventLog" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_EventNotificationService-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_EventNotificationService-devel

This package contains library source intended for building other packages which
use the "Win32_System_EventNotificationService" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_GroupPolicy-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_GroupPolicy-devel

This package contains library source intended for building other packages which
use the "Win32_System_GroupPolicy" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_HostCompute-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_HostCompute-devel

This package contains library source intended for building other packages which
use the "Win32_System_HostCompute" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_HostComputeNetwork-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_HostComputeNetwork-devel

This package contains library source intended for building other packages which
use the "Win32_System_HostComputeNetwork" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_HostComputeSystem-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_HostComputeSystem-devel

This package contains library source intended for building other packages which
use the "Win32_System_HostComputeSystem" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Hypervisor-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Hypervisor-devel

This package contains library source intended for building other packages which
use the "Win32_System_Hypervisor" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_IO-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_IO-devel

This package contains library source intended for building other packages which
use the "Win32_System_IO" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Iis-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Iis-devel

This package contains library source intended for building other packages which
use the "Win32_System_Iis" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Ioctl-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Ioctl-devel

This package contains library source intended for building other packages which
use the "Win32_System_Ioctl" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_JobObjects-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_JobObjects-devel

This package contains library source intended for building other packages which
use the "Win32_System_JobObjects" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Js-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Js-devel

This package contains library source intended for building other packages which
use the "Win32_System_Js" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Kernel-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Kernel-devel

This package contains library source intended for building other packages which
use the "Win32_System_Kernel" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_LibraryLoader-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_LibraryLoader-devel

This package contains library source intended for building other packages which
use the "Win32_System_LibraryLoader" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Mailslots-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Mailslots-devel

This package contains library source intended for building other packages which
use the "Win32_System_Mailslots" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Mapi-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Mapi-devel

This package contains library source intended for building other packages which
use the "Win32_System_Mapi" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Memory-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Memory-devel

This package contains library source intended for building other packages which
use the "Win32_System_Memory" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Memory_NonVolatile-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Memory_NonVolatile-devel

This package contains library source intended for building other packages which
use the "Win32_System_Memory_NonVolatile" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_MessageQueuing-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_MessageQueuing-devel

This package contains library source intended for building other packages which
use the "Win32_System_MessageQueuing" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_MixedReality-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_MixedReality-devel

This package contains library source intended for building other packages which
use the "Win32_System_MixedReality" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Ole-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Ole-devel

This package contains library source intended for building other packages which
use the "Win32_System_Ole" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_PasswordManagement-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_PasswordManagement-devel

This package contains library source intended for building other packages which
use the "Win32_System_PasswordManagement" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Performance-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Performance-devel

This package contains library source intended for building other packages which
use the "Win32_System_Performance" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Performance_HardwareCounterProfiling-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Performance_HardwareCounterProfiling-devel

This package contains library source intended for building other packages which
use the "Win32_System_Performance_HardwareCounterProfiling" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Pipes-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Pipes-devel

This package contains library source intended for building other packages which
use the "Win32_System_Pipes" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Power-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Power-devel

This package contains library source intended for building other packages which
use the "Win32_System_Power" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_ProcessStatus-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_ProcessStatus-devel

This package contains library source intended for building other packages which
use the "Win32_System_ProcessStatus" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Recovery-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Recovery-devel

This package contains library source intended for building other packages which
use the "Win32_System_Recovery" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Registry-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Registry-devel

This package contains library source intended for building other packages which
use the "Win32_System_Registry" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_RemoteDesktop-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_RemoteDesktop-devel

This package contains library source intended for building other packages which
use the "Win32_System_RemoteDesktop" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_RemoteManagement-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_RemoteManagement-devel

This package contains library source intended for building other packages which
use the "Win32_System_RemoteManagement" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_RestartManager-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_RestartManager-devel

This package contains library source intended for building other packages which
use the "Win32_System_RestartManager" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Restore-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Restore-devel

This package contains library source intended for building other packages which
use the "Win32_System_Restore" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Rpc-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Rpc-devel

This package contains library source intended for building other packages which
use the "Win32_System_Rpc" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Search-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Search-devel

This package contains library source intended for building other packages which
use the "Win32_System_Search" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Search_Common-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Search_Common-devel

This package contains library source intended for building other packages which
use the "Win32_System_Search_Common" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_SecurityCenter-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_SecurityCenter-devel

This package contains library source intended for building other packages which
use the "Win32_System_SecurityCenter" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Services-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Services-devel

This package contains library source intended for building other packages which
use the "Win32_System_Services" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_SetupAndMigration-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_SetupAndMigration-devel

This package contains library source intended for building other packages which
use the "Win32_System_SetupAndMigration" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Shutdown-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Shutdown-devel

This package contains library source intended for building other packages which
use the "Win32_System_Shutdown" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_StationsAndDesktops-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_StationsAndDesktops-devel

This package contains library source intended for building other packages which
use the "Win32_System_StationsAndDesktops" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_SubsystemForLinux-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_SubsystemForLinux-devel

This package contains library source intended for building other packages which
use the "Win32_System_SubsystemForLinux" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_SystemInformation-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_SystemInformation-devel

This package contains library source intended for building other packages which
use the "Win32_System_SystemInformation" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_SystemServices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_SystemServices-devel

This package contains library source intended for building other packages which
use the "Win32_System_SystemServices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Threading-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Threading-devel

This package contains library source intended for building other packages which
use the "Win32_System_Threading" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Time-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Time-devel

This package contains library source intended for building other packages which
use the "Win32_System_Time" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_TpmBaseServices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_TpmBaseServices-devel

This package contains library source intended for building other packages which
use the "Win32_System_TpmBaseServices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_UserAccessLogging-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_UserAccessLogging-devel

This package contains library source intended for building other packages which
use the "Win32_System_UserAccessLogging" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Variant-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Variant-devel

This package contains library source intended for building other packages which
use the "Win32_System_Variant" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_VirtualDosMachines-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_VirtualDosMachines-devel

This package contains library source intended for building other packages which
use the "Win32_System_VirtualDosMachines" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_WindowsProgramming-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_WindowsProgramming-devel

This package contains library source intended for building other packages which
use the "Win32_System_WindowsProgramming" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_System_Wmi-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_System_Wmi-devel

This package contains library source intended for building other packages which
use the "Win32_System_Wmi" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI-devel

This package contains library source intended for building other packages which
use the "Win32_UI" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Accessibility-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Accessibility-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Accessibility" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_ColorSystem-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_ColorSystem-devel

This package contains library source intended for building other packages which
use the "Win32_UI_ColorSystem" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Controls-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Controls-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Controls" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Controls_Dialogs-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Controls_Dialogs-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Controls_Dialogs" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_HiDpi-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_HiDpi-devel

This package contains library source intended for building other packages which
use the "Win32_UI_HiDpi" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Input-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Input-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Input" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Input_Ime-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Input_Ime-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Input_Ime" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Input_KeyboardAndMouse-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Input_KeyboardAndMouse-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Input_KeyboardAndMouse" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Input_Pointer-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Input_Pointer-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Input_Pointer" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Input_Touch-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Input_Touch-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Input_Touch" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Input_XboxController-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Input_XboxController-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Input_XboxController" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_InteractionContext-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_InteractionContext-devel

This package contains library source intended for building other packages which
use the "Win32_UI_InteractionContext" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Magnification-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Magnification-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Magnification" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Shell-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Shell-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Shell" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Shell_Common-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Shell_Common-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Shell_Common" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_Shell_PropertiesSystem-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_Shell_PropertiesSystem-devel

This package contains library source intended for building other packages which
use the "Win32_UI_Shell_PropertiesSystem" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_TabletPC-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_TabletPC-devel

This package contains library source intended for building other packages which
use the "Win32_UI_TabletPC" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_TextServices-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_TextServices-devel

This package contains library source intended for building other packages which
use the "Win32_UI_TextServices" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_UI_WindowsAndMessaging-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_UI_WindowsAndMessaging-devel

This package contains library source intended for building other packages which
use the "Win32_UI_WindowsAndMessaging" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Web-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Web-devel

This package contains library source intended for building other packages which
use the "Win32_Web" feature of the "%{crate}" crate.

%package     -n %{name}+Win32_Web_InternetExplorer-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+Win32_Web_InternetExplorer-devel

This package contains library source intended for building other packages which
use the "Win32_Web_InternetExplorer" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Rust for Windows
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-windows-sys-devel -f %{oreon_filedir}/rust-windows-sys-devel.list

%changelog

%autochangelog
