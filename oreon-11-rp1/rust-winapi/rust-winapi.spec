%global source0_hash 5c839a674fcd7a98952e593242ea400abe93992746761e38641405d28b00f419
%bcond check 0
%global debug_package %{nil}
%global crate winapi
Name:           rust-winapi
Version:        0.3.9
Release:        1%{?dist}
Summary:        Interfaces to the Windows API
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/winapi
Source0:        https://static.crates.io/crates/winapi/winapi-%{version}.crate
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
use the "winapi" crate.

%package     -n %{name}+accctrl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+accctrl-devel

This package contains library source intended for building other packages which
use the "accctrl" feature of the "%{crate}" crate.

%package     -n %{name}+aclapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+aclapi-devel

This package contains library source intended for building other packages which
use the "aclapi" feature of the "%{crate}" crate.

%package     -n %{name}+activation-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+activation-devel

This package contains library source intended for building other packages which
use the "activation" feature of the "%{crate}" crate.

%package     -n %{name}+adhoc-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+adhoc-devel

This package contains library source intended for building other packages which
use the "adhoc" feature of the "%{crate}" crate.

%package     -n %{name}+appmgmt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+appmgmt-devel

This package contains library source intended for building other packages which
use the "appmgmt" feature of the "%{crate}" crate.

%package     -n %{name}+audioclient-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+audioclient-devel

This package contains library source intended for building other packages which
use the "audioclient" feature of the "%{crate}" crate.

%package     -n %{name}+audiosessiontypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+audiosessiontypes-devel

This package contains library source intended for building other packages which
use the "audiosessiontypes" feature of the "%{crate}" crate.

%package     -n %{name}+avrt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+avrt-devel

This package contains library source intended for building other packages which
use the "avrt" feature of the "%{crate}" crate.

%package     -n %{name}+basetsd-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+basetsd-devel

This package contains library source intended for building other packages which
use the "basetsd" feature of the "%{crate}" crate.

%package     -n %{name}+bcrypt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bcrypt-devel

This package contains library source intended for building other packages which
use the "bcrypt" feature of the "%{crate}" crate.

%package     -n %{name}+bits-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bits-devel

This package contains library source intended for building other packages which
use the "bits" feature of the "%{crate}" crate.

%package     -n %{name}+bits10_1-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bits10_1-devel

This package contains library source intended for building other packages which
use the "bits10_1" feature of the "%{crate}" crate.

%package     -n %{name}+bits1_5-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bits1_5-devel

This package contains library source intended for building other packages which
use the "bits1_5" feature of the "%{crate}" crate.

%package     -n %{name}+bits2_0-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bits2_0-devel

This package contains library source intended for building other packages which
use the "bits2_0" feature of the "%{crate}" crate.

%package     -n %{name}+bits2_5-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bits2_5-devel

This package contains library source intended for building other packages which
use the "bits2_5" feature of the "%{crate}" crate.

%package     -n %{name}+bits3_0-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bits3_0-devel

This package contains library source intended for building other packages which
use the "bits3_0" feature of the "%{crate}" crate.

%package     -n %{name}+bits4_0-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bits4_0-devel

This package contains library source intended for building other packages which
use the "bits4_0" feature of the "%{crate}" crate.

%package     -n %{name}+bits5_0-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bits5_0-devel

This package contains library source intended for building other packages which
use the "bits5_0" feature of the "%{crate}" crate.

%package     -n %{name}+bitscfg-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bitscfg-devel

This package contains library source intended for building other packages which
use the "bitscfg" feature of the "%{crate}" crate.

%package     -n %{name}+bitsmsg-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bitsmsg-devel

This package contains library source intended for building other packages which
use the "bitsmsg" feature of the "%{crate}" crate.

%package     -n %{name}+bluetoothapis-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bluetoothapis-devel

This package contains library source intended for building other packages which
use the "bluetoothapis" feature of the "%{crate}" crate.

%package     -n %{name}+bluetoothleapis-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bluetoothleapis-devel

This package contains library source intended for building other packages which
use the "bluetoothleapis" feature of the "%{crate}" crate.

%package     -n %{name}+bthdef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bthdef-devel

This package contains library source intended for building other packages which
use the "bthdef" feature of the "%{crate}" crate.

%package     -n %{name}+bthioctl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bthioctl-devel

This package contains library source intended for building other packages which
use the "bthioctl" feature of the "%{crate}" crate.

%package     -n %{name}+bthledef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bthledef-devel

This package contains library source intended for building other packages which
use the "bthledef" feature of the "%{crate}" crate.

%package     -n %{name}+bthsdpdef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bthsdpdef-devel

This package contains library source intended for building other packages which
use the "bthsdpdef" feature of the "%{crate}" crate.

%package     -n %{name}+bugcodes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+bugcodes-devel

This package contains library source intended for building other packages which
use the "bugcodes" feature of the "%{crate}" crate.

%package     -n %{name}+cderr-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+cderr-devel

This package contains library source intended for building other packages which
use the "cderr" feature of the "%{crate}" crate.

%package     -n %{name}+cfg-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+cfg-devel

This package contains library source intended for building other packages which
use the "cfg" feature of the "%{crate}" crate.

%package     -n %{name}+cfgmgr32-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+cfgmgr32-devel

This package contains library source intended for building other packages which
use the "cfgmgr32" feature of the "%{crate}" crate.

%package     -n %{name}+cguid-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+cguid-devel

This package contains library source intended for building other packages which
use the "cguid" feature of the "%{crate}" crate.

%package     -n %{name}+combaseapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+combaseapi-devel

This package contains library source intended for building other packages which
use the "combaseapi" feature of the "%{crate}" crate.

%package     -n %{name}+coml2api-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+coml2api-devel

This package contains library source intended for building other packages which
use the "coml2api" feature of the "%{crate}" crate.

%package     -n %{name}+commapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+commapi-devel

This package contains library source intended for building other packages which
use the "commapi" feature of the "%{crate}" crate.

%package     -n %{name}+commctrl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+commctrl-devel

This package contains library source intended for building other packages which
use the "commctrl" feature of the "%{crate}" crate.

%package     -n %{name}+commdlg-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+commdlg-devel

This package contains library source intended for building other packages which
use the "commdlg" feature of the "%{crate}" crate.

%package     -n %{name}+commoncontrols-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+commoncontrols-devel

This package contains library source intended for building other packages which
use the "commoncontrols" feature of the "%{crate}" crate.

%package     -n %{name}+consoleapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+consoleapi-devel

This package contains library source intended for building other packages which
use the "consoleapi" feature of the "%{crate}" crate.

%package     -n %{name}+corecrt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+corecrt-devel

This package contains library source intended for building other packages which
use the "corecrt" feature of the "%{crate}" crate.

%package     -n %{name}+corsym-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+corsym-devel

This package contains library source intended for building other packages which
use the "corsym" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1-devel

This package contains library source intended for building other packages which
use the "d2d1" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1_1-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1_1-devel

This package contains library source intended for building other packages which
use the "d2d1_1" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1_2-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1_2-devel

This package contains library source intended for building other packages which
use the "d2d1_2" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1_3-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1_3-devel

This package contains library source intended for building other packages which
use the "d2d1_3" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1effectauthor-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1effectauthor-devel

This package contains library source intended for building other packages which
use the "d2d1effectauthor" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1effects-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1effects-devel

This package contains library source intended for building other packages which
use the "d2d1effects" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1effects_1-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1effects_1-devel

This package contains library source intended for building other packages which
use the "d2d1effects_1" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1effects_2-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1effects_2-devel

This package contains library source intended for building other packages which
use the "d2d1effects_2" feature of the "%{crate}" crate.

%package     -n %{name}+d2d1svg-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2d1svg-devel

This package contains library source intended for building other packages which
use the "d2d1svg" feature of the "%{crate}" crate.

%package     -n %{name}+d2dbasetypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d2dbasetypes-devel

This package contains library source intended for building other packages which
use the "d2dbasetypes" feature of the "%{crate}" crate.

%package     -n %{name}+d3d-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d-devel

This package contains library source intended for building other packages which
use the "d3d" feature of the "%{crate}" crate.

%package     -n %{name}+d3d10-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d10-devel

This package contains library source intended for building other packages which
use the "d3d10" feature of the "%{crate}" crate.

%package     -n %{name}+d3d10_1-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d10_1-devel

This package contains library source intended for building other packages which
use the "d3d10_1" feature of the "%{crate}" crate.

%package     -n %{name}+d3d10_1shader-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d10_1shader-devel

This package contains library source intended for building other packages which
use the "d3d10_1shader" feature of the "%{crate}" crate.

%package     -n %{name}+d3d10effect-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d10effect-devel

This package contains library source intended for building other packages which
use the "d3d10effect" feature of the "%{crate}" crate.

%package     -n %{name}+d3d10misc-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d10misc-devel

This package contains library source intended for building other packages which
use the "d3d10misc" feature of the "%{crate}" crate.

%package     -n %{name}+d3d10sdklayers-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d10sdklayers-devel

This package contains library source intended for building other packages which
use the "d3d10sdklayers" feature of the "%{crate}" crate.

%package     -n %{name}+d3d10shader-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d10shader-devel

This package contains library source intended for building other packages which
use the "d3d10shader" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11-devel

This package contains library source intended for building other packages which
use the "d3d11" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11_1-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11_1-devel

This package contains library source intended for building other packages which
use the "d3d11_1" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11_2-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11_2-devel

This package contains library source intended for building other packages which
use the "d3d11_2" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11_3-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11_3-devel

This package contains library source intended for building other packages which
use the "d3d11_3" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11_4-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11_4-devel

This package contains library source intended for building other packages which
use the "d3d11_4" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11on12-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11on12-devel

This package contains library source intended for building other packages which
use the "d3d11on12" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11sdklayers-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11sdklayers-devel

This package contains library source intended for building other packages which
use the "d3d11sdklayers" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11shader-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11shader-devel

This package contains library source intended for building other packages which
use the "d3d11shader" feature of the "%{crate}" crate.

%package     -n %{name}+d3d11tokenizedprogramformat-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d11tokenizedprogramformat-devel

This package contains library source intended for building other packages which
use the "d3d11tokenizedprogramformat" feature of the "%{crate}" crate.

%package     -n %{name}+d3d12-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d12-devel

This package contains library source intended for building other packages which
use the "d3d12" feature of the "%{crate}" crate.

%package     -n %{name}+d3d12sdklayers-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d12sdklayers-devel

This package contains library source intended for building other packages which
use the "d3d12sdklayers" feature of the "%{crate}" crate.

%package     -n %{name}+d3d12shader-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d12shader-devel

This package contains library source intended for building other packages which
use the "d3d12shader" feature of the "%{crate}" crate.

%package     -n %{name}+d3d9-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d9-devel

This package contains library source intended for building other packages which
use the "d3d9" feature of the "%{crate}" crate.

%package     -n %{name}+d3d9caps-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d9caps-devel

This package contains library source intended for building other packages which
use the "d3d9caps" feature of the "%{crate}" crate.

%package     -n %{name}+d3d9types-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3d9types-devel

This package contains library source intended for building other packages which
use the "d3d9types" feature of the "%{crate}" crate.

%package     -n %{name}+d3dcommon-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dcommon-devel

This package contains library source intended for building other packages which
use the "d3dcommon" feature of the "%{crate}" crate.

%package     -n %{name}+d3dcompiler-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dcompiler-devel

This package contains library source intended for building other packages which
use the "d3dcompiler" feature of the "%{crate}" crate.

%package     -n %{name}+d3dcsx-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dcsx-devel

This package contains library source intended for building other packages which
use the "d3dcsx" feature of the "%{crate}" crate.

%package     -n %{name}+d3dkmdt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dkmdt-devel

This package contains library source intended for building other packages which
use the "d3dkmdt" feature of the "%{crate}" crate.

%package     -n %{name}+d3dkmthk-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dkmthk-devel

This package contains library source intended for building other packages which
use the "d3dkmthk" feature of the "%{crate}" crate.

%package     -n %{name}+d3dukmdt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dukmdt-devel

This package contains library source intended for building other packages which
use the "d3dukmdt" feature of the "%{crate}" crate.

%package     -n %{name}+d3dx10core-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dx10core-devel

This package contains library source intended for building other packages which
use the "d3dx10core" feature of the "%{crate}" crate.

%package     -n %{name}+d3dx10math-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dx10math-devel

This package contains library source intended for building other packages which
use the "d3dx10math" feature of the "%{crate}" crate.

%package     -n %{name}+d3dx10mesh-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+d3dx10mesh-devel

This package contains library source intended for building other packages which
use the "d3dx10mesh" feature of the "%{crate}" crate.

%package     -n %{name}+datetimeapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+datetimeapi-devel

This package contains library source intended for building other packages which
use the "datetimeapi" feature of the "%{crate}" crate.

%package     -n %{name}+davclnt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+davclnt-devel

This package contains library source intended for building other packages which
use the "davclnt" feature of the "%{crate}" crate.

%package     -n %{name}+dbghelp-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dbghelp-devel

This package contains library source intended for building other packages which
use the "dbghelp" feature of the "%{crate}" crate.

%package     -n %{name}+dbt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dbt-devel

This package contains library source intended for building other packages which
use the "dbt" feature of the "%{crate}" crate.

%package     -n %{name}+dcommon-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dcommon-devel

This package contains library source intended for building other packages which
use the "dcommon" feature of the "%{crate}" crate.

%package     -n %{name}+dcomp-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dcomp-devel

This package contains library source intended for building other packages which
use the "dcomp" feature of the "%{crate}" crate.

%package     -n %{name}+dcompanimation-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dcompanimation-devel

This package contains library source intended for building other packages which
use the "dcompanimation" feature of the "%{crate}" crate.

%package     -n %{name}+dcomptypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dcomptypes-devel

This package contains library source intended for building other packages which
use the "dcomptypes" feature of the "%{crate}" crate.

%package     -n %{name}+dde-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dde-devel

This package contains library source intended for building other packages which
use the "dde" feature of the "%{crate}" crate.

%package     -n %{name}+ddraw-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ddraw-devel

This package contains library source intended for building other packages which
use the "ddraw" feature of the "%{crate}" crate.

%package     -n %{name}+ddrawi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ddrawi-devel

This package contains library source intended for building other packages which
use the "ddrawi" feature of the "%{crate}" crate.

%package     -n %{name}+ddrawint-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ddrawint-devel

This package contains library source intended for building other packages which
use the "ddrawint" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+debugapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+debugapi-devel

This package contains library source intended for building other packages which
use the "debugapi" feature of the "%{crate}" crate.

%package     -n %{name}+devguid-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+devguid-devel

This package contains library source intended for building other packages which
use the "devguid" feature of the "%{crate}" crate.

%package     -n %{name}+devicetopology-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+devicetopology-devel

This package contains library source intended for building other packages which
use the "devicetopology" feature of the "%{crate}" crate.

%package     -n %{name}+devpkey-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+devpkey-devel

This package contains library source intended for building other packages which
use the "devpkey" feature of the "%{crate}" crate.

%package     -n %{name}+devpropdef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+devpropdef-devel

This package contains library source intended for building other packages which
use the "devpropdef" feature of the "%{crate}" crate.

%package     -n %{name}+dinput-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dinput-devel

This package contains library source intended for building other packages which
use the "dinput" feature of the "%{crate}" crate.

%package     -n %{name}+dinputd-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dinputd-devel

This package contains library source intended for building other packages which
use the "dinputd" feature of the "%{crate}" crate.

%package     -n %{name}+dispex-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dispex-devel

This package contains library source intended for building other packages which
use the "dispex" feature of the "%{crate}" crate.

%package     -n %{name}+dmksctl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dmksctl-devel

This package contains library source intended for building other packages which
use the "dmksctl" feature of the "%{crate}" crate.

%package     -n %{name}+dmusicc-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dmusicc-devel

This package contains library source intended for building other packages which
use the "dmusicc" feature of the "%{crate}" crate.

%package     -n %{name}+docobj-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+docobj-devel

This package contains library source intended for building other packages which
use the "docobj" feature of the "%{crate}" crate.

%package     -n %{name}+documenttarget-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+documenttarget-devel

This package contains library source intended for building other packages which
use the "documenttarget" feature of the "%{crate}" crate.

%package     -n %{name}+dot1x-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dot1x-devel

This package contains library source intended for building other packages which
use the "dot1x" feature of the "%{crate}" crate.

%package     -n %{name}+dpa_dsa-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dpa_dsa-devel

This package contains library source intended for building other packages which
use the "dpa_dsa" feature of the "%{crate}" crate.

%package     -n %{name}+dpapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dpapi-devel

This package contains library source intended for building other packages which
use the "dpapi" feature of the "%{crate}" crate.

%package     -n %{name}+dsgetdc-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dsgetdc-devel

This package contains library source intended for building other packages which
use the "dsgetdc" feature of the "%{crate}" crate.

%package     -n %{name}+dsound-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dsound-devel

This package contains library source intended for building other packages which
use the "dsound" feature of the "%{crate}" crate.

%package     -n %{name}+dsrole-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dsrole-devel

This package contains library source intended for building other packages which
use the "dsrole" feature of the "%{crate}" crate.

%package     -n %{name}+dvp-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dvp-devel

This package contains library source intended for building other packages which
use the "dvp" feature of the "%{crate}" crate.

%package     -n %{name}+dwmapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dwmapi-devel

This package contains library source intended for building other packages which
use the "dwmapi" feature of the "%{crate}" crate.

%package     -n %{name}+dwrite-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dwrite-devel

This package contains library source intended for building other packages which
use the "dwrite" feature of the "%{crate}" crate.

%package     -n %{name}+dwrite_1-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dwrite_1-devel

This package contains library source intended for building other packages which
use the "dwrite_1" feature of the "%{crate}" crate.

%package     -n %{name}+dwrite_2-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dwrite_2-devel

This package contains library source intended for building other packages which
use the "dwrite_2" feature of the "%{crate}" crate.

%package     -n %{name}+dwrite_3-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dwrite_3-devel

This package contains library source intended for building other packages which
use the "dwrite_3" feature of the "%{crate}" crate.

%package     -n %{name}+dxdiag-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxdiag-devel

This package contains library source intended for building other packages which
use the "dxdiag" feature of the "%{crate}" crate.

%package     -n %{name}+dxfile-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxfile-devel

This package contains library source intended for building other packages which
use the "dxfile" feature of the "%{crate}" crate.

%package     -n %{name}+dxgi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgi-devel

This package contains library source intended for building other packages which
use the "dxgi" feature of the "%{crate}" crate.

%package     -n %{name}+dxgi1_2-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgi1_2-devel

This package contains library source intended for building other packages which
use the "dxgi1_2" feature of the "%{crate}" crate.

%package     -n %{name}+dxgi1_3-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgi1_3-devel

This package contains library source intended for building other packages which
use the "dxgi1_3" feature of the "%{crate}" crate.

%package     -n %{name}+dxgi1_4-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgi1_4-devel

This package contains library source intended for building other packages which
use the "dxgi1_4" feature of the "%{crate}" crate.

%package     -n %{name}+dxgi1_5-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgi1_5-devel

This package contains library source intended for building other packages which
use the "dxgi1_5" feature of the "%{crate}" crate.

%package     -n %{name}+dxgi1_6-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgi1_6-devel

This package contains library source intended for building other packages which
use the "dxgi1_6" feature of the "%{crate}" crate.

%package     -n %{name}+dxgidebug-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgidebug-devel

This package contains library source intended for building other packages which
use the "dxgidebug" feature of the "%{crate}" crate.

%package     -n %{name}+dxgiformat-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgiformat-devel

This package contains library source intended for building other packages which
use the "dxgiformat" feature of the "%{crate}" crate.

%package     -n %{name}+dxgitype-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxgitype-devel

This package contains library source intended for building other packages which
use the "dxgitype" feature of the "%{crate}" crate.

%package     -n %{name}+dxva2api-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxva2api-devel

This package contains library source intended for building other packages which
use the "dxva2api" feature of the "%{crate}" crate.

%package     -n %{name}+dxvahd-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+dxvahd-devel

This package contains library source intended for building other packages which
use the "dxvahd" feature of the "%{crate}" crate.

%package     -n %{name}+eaptypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+eaptypes-devel

This package contains library source intended for building other packages which
use the "eaptypes" feature of the "%{crate}" crate.

%package     -n %{name}+enclaveapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+enclaveapi-devel

This package contains library source intended for building other packages which
use the "enclaveapi" feature of the "%{crate}" crate.

%package     -n %{name}+endpointvolume-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+endpointvolume-devel

This package contains library source intended for building other packages which
use the "endpointvolume" feature of the "%{crate}" crate.

%package     -n %{name}+errhandlingapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+errhandlingapi-devel

This package contains library source intended for building other packages which
use the "errhandlingapi" feature of the "%{crate}" crate.

%package     -n %{name}+everything-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+everything-devel

This package contains library source intended for building other packages which
use the "everything" feature of the "%{crate}" crate.

%package     -n %{name}+evntcons-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+evntcons-devel

This package contains library source intended for building other packages which
use the "evntcons" feature of the "%{crate}" crate.

%package     -n %{name}+evntprov-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+evntprov-devel

This package contains library source intended for building other packages which
use the "evntprov" feature of the "%{crate}" crate.

%package     -n %{name}+evntrace-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+evntrace-devel

This package contains library source intended for building other packages which
use the "evntrace" feature of the "%{crate}" crate.

%package     -n %{name}+excpt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+excpt-devel

This package contains library source intended for building other packages which
use the "excpt" feature of the "%{crate}" crate.

%package     -n %{name}+exdisp-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+exdisp-devel

This package contains library source intended for building other packages which
use the "exdisp" feature of the "%{crate}" crate.

%package     -n %{name}+fibersapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+fibersapi-devel

This package contains library source intended for building other packages which
use the "fibersapi" feature of the "%{crate}" crate.

%package     -n %{name}+fileapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+fileapi-devel

This package contains library source intended for building other packages which
use the "fileapi" feature of the "%{crate}" crate.

%package     -n %{name}+functiondiscoverykeys_devpkey-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+functiondiscoverykeys_devpkey-devel

This package contains library source intended for building other packages which
use the "functiondiscoverykeys_devpkey" feature of the "%{crate}" crate.

%package     -n %{name}+gl-gl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+gl-gl-devel

This package contains library source intended for building other packages which
use the "gl-gl" feature of the "%{crate}" crate.

%package     -n %{name}+guiddef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+guiddef-devel

This package contains library source intended for building other packages which
use the "guiddef" feature of the "%{crate}" crate.

%package     -n %{name}+handleapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+handleapi-devel

This package contains library source intended for building other packages which
use the "handleapi" feature of the "%{crate}" crate.

%package     -n %{name}+heapapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+heapapi-devel

This package contains library source intended for building other packages which
use the "heapapi" feature of the "%{crate}" crate.

%package     -n %{name}+hidclass-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+hidclass-devel

This package contains library source intended for building other packages which
use the "hidclass" feature of the "%{crate}" crate.

%package     -n %{name}+hidpi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+hidpi-devel

This package contains library source intended for building other packages which
use the "hidpi" feature of the "%{crate}" crate.

%package     -n %{name}+hidsdi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+hidsdi-devel

This package contains library source intended for building other packages which
use the "hidsdi" feature of the "%{crate}" crate.

%package     -n %{name}+hidusage-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+hidusage-devel

This package contains library source intended for building other packages which
use the "hidusage" feature of the "%{crate}" crate.

%package     -n %{name}+highlevelmonitorconfigurationapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+highlevelmonitorconfigurationapi-devel

This package contains library source intended for building other packages which
use the "highlevelmonitorconfigurationapi" feature of the "%{crate}" crate.

%package     -n %{name}+hstring-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+hstring-devel

This package contains library source intended for building other packages which
use the "hstring" feature of the "%{crate}" crate.

%package     -n %{name}+http-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+http-devel

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%package     -n %{name}+ifdef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ifdef-devel

This package contains library source intended for building other packages which
use the "ifdef" feature of the "%{crate}" crate.

%package     -n %{name}+ifmib-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ifmib-devel

This package contains library source intended for building other packages which
use the "ifmib" feature of the "%{crate}" crate.

%package     -n %{name}+imm-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+imm-devel

This package contains library source intended for building other packages which
use the "imm" feature of the "%{crate}" crate.

%package     -n %{name}+impl-debug-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+impl-debug-devel

This package contains library source intended for building other packages which
use the "impl-debug" feature of the "%{crate}" crate.

%package     -n %{name}+impl-default-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+impl-default-devel

This package contains library source intended for building other packages which
use the "impl-default" feature of the "%{crate}" crate.

%package     -n %{name}+in6addr-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+in6addr-devel

This package contains library source intended for building other packages which
use the "in6addr" feature of the "%{crate}" crate.

%package     -n %{name}+inaddr-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+inaddr-devel

This package contains library source intended for building other packages which
use the "inaddr" feature of the "%{crate}" crate.

%package     -n %{name}+inspectable-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+inspectable-devel

This package contains library source intended for building other packages which
use the "inspectable" feature of the "%{crate}" crate.

%package     -n %{name}+interlockedapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+interlockedapi-devel

This package contains library source intended for building other packages which
use the "interlockedapi" feature of the "%{crate}" crate.

%package     -n %{name}+intsafe-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+intsafe-devel

This package contains library source intended for building other packages which
use the "intsafe" feature of the "%{crate}" crate.

%package     -n %{name}+ioapiset-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ioapiset-devel

This package contains library source intended for building other packages which
use the "ioapiset" feature of the "%{crate}" crate.

%package     -n %{name}+ipexport-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ipexport-devel

This package contains library source intended for building other packages which
use the "ipexport" feature of the "%{crate}" crate.

%package     -n %{name}+iphlpapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+iphlpapi-devel

This package contains library source intended for building other packages which
use the "iphlpapi" feature of the "%{crate}" crate.

%package     -n %{name}+ipifcons-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ipifcons-devel

This package contains library source intended for building other packages which
use the "ipifcons" feature of the "%{crate}" crate.

%package     -n %{name}+ipmib-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ipmib-devel

This package contains library source intended for building other packages which
use the "ipmib" feature of the "%{crate}" crate.

%package     -n %{name}+iprtrmib-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+iprtrmib-devel

This package contains library source intended for building other packages which
use the "iprtrmib" feature of the "%{crate}" crate.

%package     -n %{name}+iptypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+iptypes-devel

This package contains library source intended for building other packages which
use the "iptypes" feature of the "%{crate}" crate.

%package     -n %{name}+jobapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+jobapi-devel

This package contains library source intended for building other packages which
use the "jobapi" feature of the "%{crate}" crate.

%package     -n %{name}+jobapi2-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+jobapi2-devel

This package contains library source intended for building other packages which
use the "jobapi2" feature of the "%{crate}" crate.

%package     -n %{name}+knownfolders-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+knownfolders-devel

This package contains library source intended for building other packages which
use the "knownfolders" feature of the "%{crate}" crate.

%package     -n %{name}+ks-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ks-devel

This package contains library source intended for building other packages which
use the "ks" feature of the "%{crate}" crate.

%package     -n %{name}+ksmedia-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ksmedia-devel

This package contains library source intended for building other packages which
use the "ksmedia" feature of the "%{crate}" crate.

%package     -n %{name}+ktmtypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ktmtypes-devel

This package contains library source intended for building other packages which
use the "ktmtypes" feature of the "%{crate}" crate.

%package     -n %{name}+ktmw32-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ktmw32-devel

This package contains library source intended for building other packages which
use the "ktmw32" feature of the "%{crate}" crate.

%package     -n %{name}+l2cmn-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+l2cmn-devel

This package contains library source intended for building other packages which
use the "l2cmn" feature of the "%{crate}" crate.

%package     -n %{name}+libloaderapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+libloaderapi-devel

This package contains library source intended for building other packages which
use the "libloaderapi" feature of the "%{crate}" crate.

%package     -n %{name}+limits-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+limits-devel

This package contains library source intended for building other packages which
use the "limits" feature of the "%{crate}" crate.

%package     -n %{name}+lmaccess-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmaccess-devel

This package contains library source intended for building other packages which
use the "lmaccess" feature of the "%{crate}" crate.

%package     -n %{name}+lmalert-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmalert-devel

This package contains library source intended for building other packages which
use the "lmalert" feature of the "%{crate}" crate.

%package     -n %{name}+lmapibuf-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmapibuf-devel

This package contains library source intended for building other packages which
use the "lmapibuf" feature of the "%{crate}" crate.

%package     -n %{name}+lmat-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmat-devel

This package contains library source intended for building other packages which
use the "lmat" feature of the "%{crate}" crate.

%package     -n %{name}+lmcons-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmcons-devel

This package contains library source intended for building other packages which
use the "lmcons" feature of the "%{crate}" crate.

%package     -n %{name}+lmdfs-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmdfs-devel

This package contains library source intended for building other packages which
use the "lmdfs" feature of the "%{crate}" crate.

%package     -n %{name}+lmerrlog-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmerrlog-devel

This package contains library source intended for building other packages which
use the "lmerrlog" feature of the "%{crate}" crate.

%package     -n %{name}+lmjoin-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmjoin-devel

This package contains library source intended for building other packages which
use the "lmjoin" feature of the "%{crate}" crate.

%package     -n %{name}+lmmsg-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmmsg-devel

This package contains library source intended for building other packages which
use the "lmmsg" feature of the "%{crate}" crate.

%package     -n %{name}+lmremutl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmremutl-devel

This package contains library source intended for building other packages which
use the "lmremutl" feature of the "%{crate}" crate.

%package     -n %{name}+lmrepl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmrepl-devel

This package contains library source intended for building other packages which
use the "lmrepl" feature of the "%{crate}" crate.

%package     -n %{name}+lmserver-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmserver-devel

This package contains library source intended for building other packages which
use the "lmserver" feature of the "%{crate}" crate.

%package     -n %{name}+lmshare-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmshare-devel

This package contains library source intended for building other packages which
use the "lmshare" feature of the "%{crate}" crate.

%package     -n %{name}+lmstats-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmstats-devel

This package contains library source intended for building other packages which
use the "lmstats" feature of the "%{crate}" crate.

%package     -n %{name}+lmsvc-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmsvc-devel

This package contains library source intended for building other packages which
use the "lmsvc" feature of the "%{crate}" crate.

%package     -n %{name}+lmuse-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmuse-devel

This package contains library source intended for building other packages which
use the "lmuse" feature of the "%{crate}" crate.

%package     -n %{name}+lmwksta-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lmwksta-devel

This package contains library source intended for building other packages which
use the "lmwksta" feature of the "%{crate}" crate.

%package     -n %{name}+lowlevelmonitorconfigurationapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lowlevelmonitorconfigurationapi-devel

This package contains library source intended for building other packages which
use the "lowlevelmonitorconfigurationapi" feature of the "%{crate}" crate.

%package     -n %{name}+lsalookup-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+lsalookup-devel

This package contains library source intended for building other packages which
use the "lsalookup" feature of the "%{crate}" crate.

%package     -n %{name}+memoryapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+memoryapi-devel

This package contains library source intended for building other packages which
use the "memoryapi" feature of the "%{crate}" crate.

%package     -n %{name}+minschannel-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+minschannel-devel

This package contains library source intended for building other packages which
use the "minschannel" feature of the "%{crate}" crate.

%package     -n %{name}+minwinbase-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+minwinbase-devel

This package contains library source intended for building other packages which
use the "minwinbase" feature of the "%{crate}" crate.

%package     -n %{name}+minwindef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+minwindef-devel

This package contains library source intended for building other packages which
use the "minwindef" feature of the "%{crate}" crate.

%package     -n %{name}+mmdeviceapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mmdeviceapi-devel

This package contains library source intended for building other packages which
use the "mmdeviceapi" feature of the "%{crate}" crate.

%package     -n %{name}+mmeapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mmeapi-devel

This package contains library source intended for building other packages which
use the "mmeapi" feature of the "%{crate}" crate.

%package     -n %{name}+mmreg-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mmreg-devel

This package contains library source intended for building other packages which
use the "mmreg" feature of the "%{crate}" crate.

%package     -n %{name}+mmsystem-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mmsystem-devel

This package contains library source intended for building other packages which
use the "mmsystem" feature of the "%{crate}" crate.

%package     -n %{name}+mprapidef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mprapidef-devel

This package contains library source intended for building other packages which
use the "mprapidef" feature of the "%{crate}" crate.

%package     -n %{name}+msaatext-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+msaatext-devel

This package contains library source intended for building other packages which
use the "msaatext" feature of the "%{crate}" crate.

%package     -n %{name}+mscat-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mscat-devel

This package contains library source intended for building other packages which
use the "mscat" feature of the "%{crate}" crate.

%package     -n %{name}+mschapp-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mschapp-devel

This package contains library source intended for building other packages which
use the "mschapp" feature of the "%{crate}" crate.

%package     -n %{name}+mssip-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mssip-devel

This package contains library source intended for building other packages which
use the "mssip" feature of the "%{crate}" crate.

%package     -n %{name}+mstcpip-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mstcpip-devel

This package contains library source intended for building other packages which
use the "mstcpip" feature of the "%{crate}" crate.

%package     -n %{name}+mswsock-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mswsock-devel

This package contains library source intended for building other packages which
use the "mswsock" feature of the "%{crate}" crate.

%package     -n %{name}+mswsockdef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+mswsockdef-devel

This package contains library source intended for building other packages which
use the "mswsockdef" feature of the "%{crate}" crate.

%package     -n %{name}+namedpipeapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+namedpipeapi-devel

This package contains library source intended for building other packages which
use the "namedpipeapi" feature of the "%{crate}" crate.

%package     -n %{name}+namespaceapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+namespaceapi-devel

This package contains library source intended for building other packages which
use the "namespaceapi" feature of the "%{crate}" crate.

%package     -n %{name}+nb30-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+nb30-devel

This package contains library source intended for building other packages which
use the "nb30" feature of the "%{crate}" crate.

%package     -n %{name}+ncrypt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ncrypt-devel

This package contains library source intended for building other packages which
use the "ncrypt" feature of the "%{crate}" crate.

%package     -n %{name}+netioapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+netioapi-devel

This package contains library source intended for building other packages which
use the "netioapi" feature of the "%{crate}" crate.

%package     -n %{name}+nldef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+nldef-devel

This package contains library source intended for building other packages which
use the "nldef" feature of the "%{crate}" crate.

%package     -n %{name}+ntddndis-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ntddndis-devel

This package contains library source intended for building other packages which
use the "ntddndis" feature of the "%{crate}" crate.

%package     -n %{name}+ntddscsi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ntddscsi-devel

This package contains library source intended for building other packages which
use the "ntddscsi" feature of the "%{crate}" crate.

%package     -n %{name}+ntddser-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ntddser-devel

This package contains library source intended for building other packages which
use the "ntddser" feature of the "%{crate}" crate.

%package     -n %{name}+ntdef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ntdef-devel

This package contains library source intended for building other packages which
use the "ntdef" feature of the "%{crate}" crate.

%package     -n %{name}+ntlsa-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ntlsa-devel

This package contains library source intended for building other packages which
use the "ntlsa" feature of the "%{crate}" crate.

%package     -n %{name}+ntsecapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ntsecapi-devel

This package contains library source intended for building other packages which
use the "ntsecapi" feature of the "%{crate}" crate.

%package     -n %{name}+ntstatus-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ntstatus-devel

This package contains library source intended for building other packages which
use the "ntstatus" feature of the "%{crate}" crate.

%package     -n %{name}+oaidl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+oaidl-devel

This package contains library source intended for building other packages which
use the "oaidl" feature of the "%{crate}" crate.

%package     -n %{name}+objbase-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+objbase-devel

This package contains library source intended for building other packages which
use the "objbase" feature of the "%{crate}" crate.

%package     -n %{name}+objidl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+objidl-devel

This package contains library source intended for building other packages which
use the "objidl" feature of the "%{crate}" crate.

%package     -n %{name}+objidlbase-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+objidlbase-devel

This package contains library source intended for building other packages which
use the "objidlbase" feature of the "%{crate}" crate.

%package     -n %{name}+ocidl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ocidl-devel

This package contains library source intended for building other packages which
use the "ocidl" feature of the "%{crate}" crate.

%package     -n %{name}+ole2-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ole2-devel

This package contains library source intended for building other packages which
use the "ole2" feature of the "%{crate}" crate.

%package     -n %{name}+oleauto-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+oleauto-devel

This package contains library source intended for building other packages which
use the "oleauto" feature of the "%{crate}" crate.

%package     -n %{name}+olectl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+olectl-devel

This package contains library source intended for building other packages which
use the "olectl" feature of the "%{crate}" crate.

%package     -n %{name}+oleidl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+oleidl-devel

This package contains library source intended for building other packages which
use the "oleidl" feature of the "%{crate}" crate.

%package     -n %{name}+opmapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+opmapi-devel

This package contains library source intended for building other packages which
use the "opmapi" feature of the "%{crate}" crate.

%package     -n %{name}+pdh-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+pdh-devel

This package contains library source intended for building other packages which
use the "pdh" feature of the "%{crate}" crate.

%package     -n %{name}+perflib-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+perflib-devel

This package contains library source intended for building other packages which
use the "perflib" feature of the "%{crate}" crate.

%package     -n %{name}+physicalmonitorenumerationapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+physicalmonitorenumerationapi-devel

This package contains library source intended for building other packages which
use the "physicalmonitorenumerationapi" feature of the "%{crate}" crate.

%package     -n %{name}+playsoundapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+playsoundapi-devel

This package contains library source intended for building other packages which
use the "playsoundapi" feature of the "%{crate}" crate.

%package     -n %{name}+portabledevice-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+portabledevice-devel

This package contains library source intended for building other packages which
use the "portabledevice" feature of the "%{crate}" crate.

%package     -n %{name}+portabledeviceapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+portabledeviceapi-devel

This package contains library source intended for building other packages which
use the "portabledeviceapi" feature of the "%{crate}" crate.

%package     -n %{name}+portabledevicetypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+portabledevicetypes-devel

This package contains library source intended for building other packages which
use the "portabledevicetypes" feature of the "%{crate}" crate.

%package     -n %{name}+powerbase-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+powerbase-devel

This package contains library source intended for building other packages which
use the "powerbase" feature of the "%{crate}" crate.

%package     -n %{name}+powersetting-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+powersetting-devel

This package contains library source intended for building other packages which
use the "powersetting" feature of the "%{crate}" crate.

%package     -n %{name}+powrprof-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+powrprof-devel

This package contains library source intended for building other packages which
use the "powrprof" feature of the "%{crate}" crate.

%package     -n %{name}+processenv-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+processenv-devel

This package contains library source intended for building other packages which
use the "processenv" feature of the "%{crate}" crate.

%package     -n %{name}+processsnapshot-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+processsnapshot-devel

This package contains library source intended for building other packages which
use the "processsnapshot" feature of the "%{crate}" crate.

%package     -n %{name}+processthreadsapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+processthreadsapi-devel

This package contains library source intended for building other packages which
use the "processthreadsapi" feature of the "%{crate}" crate.

%package     -n %{name}+processtopologyapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+processtopologyapi-devel

This package contains library source intended for building other packages which
use the "processtopologyapi" feature of the "%{crate}" crate.

%package     -n %{name}+profileapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+profileapi-devel

This package contains library source intended for building other packages which
use the "profileapi" feature of the "%{crate}" crate.

%package     -n %{name}+propidl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+propidl-devel

This package contains library source intended for building other packages which
use the "propidl" feature of the "%{crate}" crate.

%package     -n %{name}+propkey-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+propkey-devel

This package contains library source intended for building other packages which
use the "propkey" feature of the "%{crate}" crate.

%package     -n %{name}+propkeydef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+propkeydef-devel

This package contains library source intended for building other packages which
use the "propkeydef" feature of the "%{crate}" crate.

%package     -n %{name}+propsys-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+propsys-devel

This package contains library source intended for building other packages which
use the "propsys" feature of the "%{crate}" crate.

%package     -n %{name}+prsht-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+prsht-devel

This package contains library source intended for building other packages which
use the "prsht" feature of the "%{crate}" crate.

%package     -n %{name}+psapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+psapi-devel

This package contains library source intended for building other packages which
use the "psapi" feature of the "%{crate}" crate.

%package     -n %{name}+qos-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+qos-devel

This package contains library source intended for building other packages which
use the "qos" feature of the "%{crate}" crate.

%package     -n %{name}+realtimeapiset-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+realtimeapiset-devel

This package contains library source intended for building other packages which
use the "realtimeapiset" feature of the "%{crate}" crate.

%package     -n %{name}+reason-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+reason-devel

This package contains library source intended for building other packages which
use the "reason" feature of the "%{crate}" crate.

%package     -n %{name}+restartmanager-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+restartmanager-devel

This package contains library source intended for building other packages which
use the "restartmanager" feature of the "%{crate}" crate.

%package     -n %{name}+restrictederrorinfo-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+restrictederrorinfo-devel

This package contains library source intended for building other packages which
use the "restrictederrorinfo" feature of the "%{crate}" crate.

%package     -n %{name}+rmxfguid-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+rmxfguid-devel

This package contains library source intended for building other packages which
use the "rmxfguid" feature of the "%{crate}" crate.

%package     -n %{name}+roapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+roapi-devel

This package contains library source intended for building other packages which
use the "roapi" feature of the "%{crate}" crate.

%package     -n %{name}+robuffer-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+robuffer-devel

This package contains library source intended for building other packages which
use the "robuffer" feature of the "%{crate}" crate.

%package     -n %{name}+roerrorapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+roerrorapi-devel

This package contains library source intended for building other packages which
use the "roerrorapi" feature of the "%{crate}" crate.

%package     -n %{name}+rpc-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+rpc-devel

This package contains library source intended for building other packages which
use the "rpc" feature of the "%{crate}" crate.

%package     -n %{name}+rpcdce-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+rpcdce-devel

This package contains library source intended for building other packages which
use the "rpcdce" feature of the "%{crate}" crate.

%package     -n %{name}+rpcndr-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+rpcndr-devel

This package contains library source intended for building other packages which
use the "rpcndr" feature of the "%{crate}" crate.

%package     -n %{name}+rtinfo-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+rtinfo-devel

This package contains library source intended for building other packages which
use the "rtinfo" feature of the "%{crate}" crate.

%package     -n %{name}+sapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sapi-devel

This package contains library source intended for building other packages which
use the "sapi" feature of the "%{crate}" crate.

%package     -n %{name}+sapi51-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sapi51-devel

This package contains library source intended for building other packages which
use the "sapi51" feature of the "%{crate}" crate.

%package     -n %{name}+sapi53-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sapi53-devel

This package contains library source intended for building other packages which
use the "sapi53" feature of the "%{crate}" crate.

%package     -n %{name}+sapiddk-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sapiddk-devel

This package contains library source intended for building other packages which
use the "sapiddk" feature of the "%{crate}" crate.

%package     -n %{name}+sapiddk51-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sapiddk51-devel

This package contains library source intended for building other packages which
use the "sapiddk51" feature of the "%{crate}" crate.

%package     -n %{name}+schannel-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+schannel-devel

This package contains library source intended for building other packages which
use the "schannel" feature of the "%{crate}" crate.

%package     -n %{name}+sddl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sddl-devel

This package contains library source intended for building other packages which
use the "sddl" feature of the "%{crate}" crate.

%package     -n %{name}+securityappcontainer-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+securityappcontainer-devel

This package contains library source intended for building other packages which
use the "securityappcontainer" feature of the "%{crate}" crate.

%package     -n %{name}+securitybaseapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+securitybaseapi-devel

This package contains library source intended for building other packages which
use the "securitybaseapi" feature of the "%{crate}" crate.

%package     -n %{name}+servprov-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+servprov-devel

This package contains library source intended for building other packages which
use the "servprov" feature of the "%{crate}" crate.

%package     -n %{name}+setupapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+setupapi-devel

This package contains library source intended for building other packages which
use the "setupapi" feature of the "%{crate}" crate.

%package     -n %{name}+shellapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+shellapi-devel

This package contains library source intended for building other packages which
use the "shellapi" feature of the "%{crate}" crate.

%package     -n %{name}+shellscalingapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+shellscalingapi-devel

This package contains library source intended for building other packages which
use the "shellscalingapi" feature of the "%{crate}" crate.

%package     -n %{name}+shlobj-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+shlobj-devel

This package contains library source intended for building other packages which
use the "shlobj" feature of the "%{crate}" crate.

%package     -n %{name}+shobjidl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+shobjidl-devel

This package contains library source intended for building other packages which
use the "shobjidl" feature of the "%{crate}" crate.

%package     -n %{name}+shobjidl_core-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+shobjidl_core-devel

This package contains library source intended for building other packages which
use the "shobjidl_core" feature of the "%{crate}" crate.

%package     -n %{name}+shtypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+shtypes-devel

This package contains library source intended for building other packages which
use the "shtypes" feature of the "%{crate}" crate.

%package     -n %{name}+softpub-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+softpub-devel

This package contains library source intended for building other packages which
use the "softpub" feature of the "%{crate}" crate.

%package     -n %{name}+spapidef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+spapidef-devel

This package contains library source intended for building other packages which
use the "spapidef" feature of the "%{crate}" crate.

%package     -n %{name}+spellcheck-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+spellcheck-devel

This package contains library source intended for building other packages which
use the "spellcheck" feature of the "%{crate}" crate.

%package     -n %{name}+sporder-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sporder-devel

This package contains library source intended for building other packages which
use the "sporder" feature of the "%{crate}" crate.

%package     -n %{name}+sql-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sql-devel

This package contains library source intended for building other packages which
use the "sql" feature of the "%{crate}" crate.

%package     -n %{name}+sqlext-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sqlext-devel

This package contains library source intended for building other packages which
use the "sqlext" feature of the "%{crate}" crate.

%package     -n %{name}+sqltypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sqltypes-devel

This package contains library source intended for building other packages which
use the "sqltypes" feature of the "%{crate}" crate.

%package     -n %{name}+sqlucode-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sqlucode-devel

This package contains library source intended for building other packages which
use the "sqlucode" feature of the "%{crate}" crate.

%package     -n %{name}+sspi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sspi-devel

This package contains library source intended for building other packages which
use the "sspi" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+stralign-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+stralign-devel

This package contains library source intended for building other packages which
use the "stralign" feature of the "%{crate}" crate.

%package     -n %{name}+stringapiset-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+stringapiset-devel

This package contains library source intended for building other packages which
use the "stringapiset" feature of the "%{crate}" crate.

%package     -n %{name}+strmif-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+strmif-devel

This package contains library source intended for building other packages which
use the "strmif" feature of the "%{crate}" crate.

%package     -n %{name}+subauth-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+subauth-devel

This package contains library source intended for building other packages which
use the "subauth" feature of the "%{crate}" crate.

%package     -n %{name}+synchapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+synchapi-devel

This package contains library source intended for building other packages which
use the "synchapi" feature of the "%{crate}" crate.

%package     -n %{name}+sysinfoapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+sysinfoapi-devel

This package contains library source intended for building other packages which
use the "sysinfoapi" feature of the "%{crate}" crate.

%package     -n %{name}+systemtopologyapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+systemtopologyapi-devel

This package contains library source intended for building other packages which
use the "systemtopologyapi" feature of the "%{crate}" crate.

%package     -n %{name}+taskschd-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+taskschd-devel

This package contains library source intended for building other packages which
use the "taskschd" feature of the "%{crate}" crate.

%package     -n %{name}+tcpestats-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+tcpestats-devel

This package contains library source intended for building other packages which
use the "tcpestats" feature of the "%{crate}" crate.

%package     -n %{name}+tcpmib-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+tcpmib-devel

This package contains library source intended for building other packages which
use the "tcpmib" feature of the "%{crate}" crate.

%package     -n %{name}+textstor-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+textstor-devel

This package contains library source intended for building other packages which
use the "textstor" feature of the "%{crate}" crate.

%package     -n %{name}+threadpoolapiset-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+threadpoolapiset-devel

This package contains library source intended for building other packages which
use the "threadpoolapiset" feature of the "%{crate}" crate.

%package     -n %{name}+threadpoollegacyapiset-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+threadpoollegacyapiset-devel

This package contains library source intended for building other packages which
use the "threadpoollegacyapiset" feature of the "%{crate}" crate.

%package     -n %{name}+timeapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+timeapi-devel

This package contains library source intended for building other packages which
use the "timeapi" feature of the "%{crate}" crate.

%package     -n %{name}+timezoneapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+timezoneapi-devel

This package contains library source intended for building other packages which
use the "timezoneapi" feature of the "%{crate}" crate.

%package     -n %{name}+tlhelp32-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+tlhelp32-devel

This package contains library source intended for building other packages which
use the "tlhelp32" feature of the "%{crate}" crate.

%package     -n %{name}+transportsettingcommon-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+transportsettingcommon-devel

This package contains library source intended for building other packages which
use the "transportsettingcommon" feature of the "%{crate}" crate.

%package     -n %{name}+tvout-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+tvout-devel

This package contains library source intended for building other packages which
use the "tvout" feature of the "%{crate}" crate.

%package     -n %{name}+udpmib-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+udpmib-devel

This package contains library source intended for building other packages which
use the "udpmib" feature of the "%{crate}" crate.

%package     -n %{name}+unknwnbase-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+unknwnbase-devel

This package contains library source intended for building other packages which
use the "unknwnbase" feature of the "%{crate}" crate.

%package     -n %{name}+urlhist-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+urlhist-devel

This package contains library source intended for building other packages which
use the "urlhist" feature of the "%{crate}" crate.

%package     -n %{name}+urlmon-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+urlmon-devel

This package contains library source intended for building other packages which
use the "urlmon" feature of the "%{crate}" crate.

%package     -n %{name}+usb-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+usb-devel

This package contains library source intended for building other packages which
use the "usb" feature of the "%{crate}" crate.

%package     -n %{name}+usbioctl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+usbioctl-devel

This package contains library source intended for building other packages which
use the "usbioctl" feature of the "%{crate}" crate.

%package     -n %{name}+usbiodef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+usbiodef-devel

This package contains library source intended for building other packages which
use the "usbiodef" feature of the "%{crate}" crate.

%package     -n %{name}+usbscan-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+usbscan-devel

This package contains library source intended for building other packages which
use the "usbscan" feature of the "%{crate}" crate.

%package     -n %{name}+usbspec-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+usbspec-devel

This package contains library source intended for building other packages which
use the "usbspec" feature of the "%{crate}" crate.

%package     -n %{name}+userenv-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+userenv-devel

This package contains library source intended for building other packages which
use the "userenv" feature of the "%{crate}" crate.

%package     -n %{name}+usp10-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+usp10-devel

This package contains library source intended for building other packages which
use the "usp10" feature of the "%{crate}" crate.

%package     -n %{name}+utilapiset-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+utilapiset-devel

This package contains library source intended for building other packages which
use the "utilapiset" feature of the "%{crate}" crate.

%package     -n %{name}+uxtheme-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+uxtheme-devel

This package contains library source intended for building other packages which
use the "uxtheme" feature of the "%{crate}" crate.

%package     -n %{name}+vadefs-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+vadefs-devel

This package contains library source intended for building other packages which
use the "vadefs" feature of the "%{crate}" crate.

%package     -n %{name}+vcruntime-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+vcruntime-devel

This package contains library source intended for building other packages which
use the "vcruntime" feature of the "%{crate}" crate.

%package     -n %{name}+vsbackup-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+vsbackup-devel

This package contains library source intended for building other packages which
use the "vsbackup" feature of the "%{crate}" crate.

%package     -n %{name}+vss-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+vss-devel

This package contains library source intended for building other packages which
use the "vss" feature of the "%{crate}" crate.

%package     -n %{name}+vsserror-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+vsserror-devel

This package contains library source intended for building other packages which
use the "vsserror" feature of the "%{crate}" crate.

%package     -n %{name}+vswriter-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+vswriter-devel

This package contains library source intended for building other packages which
use the "vswriter" feature of the "%{crate}" crate.

%package     -n %{name}+wbemads-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wbemads-devel

This package contains library source intended for building other packages which
use the "wbemads" feature of the "%{crate}" crate.

%package     -n %{name}+wbemcli-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wbemcli-devel

This package contains library source intended for building other packages which
use the "wbemcli" feature of the "%{crate}" crate.

%package     -n %{name}+wbemdisp-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wbemdisp-devel

This package contains library source intended for building other packages which
use the "wbemdisp" feature of the "%{crate}" crate.

%package     -n %{name}+wbemprov-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wbemprov-devel

This package contains library source intended for building other packages which
use the "wbemprov" feature of the "%{crate}" crate.

%package     -n %{name}+wbemtran-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wbemtran-devel

This package contains library source intended for building other packages which
use the "wbemtran" feature of the "%{crate}" crate.

%package     -n %{name}+wct-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wct-devel

This package contains library source intended for building other packages which
use the "wct" feature of the "%{crate}" crate.

%package     -n %{name}+werapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+werapi-devel

This package contains library source intended for building other packages which
use the "werapi" feature of the "%{crate}" crate.

%package     -n %{name}+winbase-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winbase-devel

This package contains library source intended for building other packages which
use the "winbase" feature of the "%{crate}" crate.

%package     -n %{name}+wincodec-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wincodec-devel

This package contains library source intended for building other packages which
use the "wincodec" feature of the "%{crate}" crate.

%package     -n %{name}+wincodecsdk-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wincodecsdk-devel

This package contains library source intended for building other packages which
use the "wincodecsdk" feature of the "%{crate}" crate.

%package     -n %{name}+wincon-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wincon-devel

This package contains library source intended for building other packages which
use the "wincon" feature of the "%{crate}" crate.

%package     -n %{name}+wincontypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wincontypes-devel

This package contains library source intended for building other packages which
use the "wincontypes" feature of the "%{crate}" crate.

%package     -n %{name}+wincred-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wincred-devel

This package contains library source intended for building other packages which
use the "wincred" feature of the "%{crate}" crate.

%package     -n %{name}+wincrypt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wincrypt-devel

This package contains library source intended for building other packages which
use the "wincrypt" feature of the "%{crate}" crate.

%package     -n %{name}+windef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+windef-devel

This package contains library source intended for building other packages which
use the "windef" feature of the "%{crate}" crate.

%package     -n %{name}+windot11-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+windot11-devel

This package contains library source intended for building other packages which
use the "windot11" feature of the "%{crate}" crate.

%package     -n %{name}+windowsceip-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+windowsceip-devel

This package contains library source intended for building other packages which
use the "windowsceip" feature of the "%{crate}" crate.

%package     -n %{name}+windowsx-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+windowsx-devel

This package contains library source intended for building other packages which
use the "windowsx" feature of the "%{crate}" crate.

%package     -n %{name}+winefs-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winefs-devel

This package contains library source intended for building other packages which
use the "winefs" feature of the "%{crate}" crate.

%package     -n %{name}+winerror-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winerror-devel

This package contains library source intended for building other packages which
use the "winerror" feature of the "%{crate}" crate.

%package     -n %{name}+winevt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winevt-devel

This package contains library source intended for building other packages which
use the "winevt" feature of the "%{crate}" crate.

%package     -n %{name}+wingdi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wingdi-devel

This package contains library source intended for building other packages which
use the "wingdi" feature of the "%{crate}" crate.

%package     -n %{name}+winhttp-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winhttp-devel

This package contains library source intended for building other packages which
use the "winhttp" feature of the "%{crate}" crate.

%package     -n %{name}+wininet-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wininet-devel

This package contains library source intended for building other packages which
use the "wininet" feature of the "%{crate}" crate.

%package     -n %{name}+winineti-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winineti-devel

This package contains library source intended for building other packages which
use the "winineti" feature of the "%{crate}" crate.

%package     -n %{name}+winioctl-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winioctl-devel

This package contains library source intended for building other packages which
use the "winioctl" feature of the "%{crate}" crate.

%package     -n %{name}+winnetwk-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winnetwk-devel

This package contains library source intended for building other packages which
use the "winnetwk" feature of the "%{crate}" crate.

%package     -n %{name}+winnls-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winnls-devel

This package contains library source intended for building other packages which
use the "winnls" feature of the "%{crate}" crate.

%package     -n %{name}+winnt-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winnt-devel

This package contains library source intended for building other packages which
use the "winnt" feature of the "%{crate}" crate.

%package     -n %{name}+winreg-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winreg-devel

This package contains library source intended for building other packages which
use the "winreg" feature of the "%{crate}" crate.

%package     -n %{name}+winsafer-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winsafer-devel

This package contains library source intended for building other packages which
use the "winsafer" feature of the "%{crate}" crate.

%package     -n %{name}+winscard-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winscard-devel

This package contains library source intended for building other packages which
use the "winscard" feature of the "%{crate}" crate.

%package     -n %{name}+winsmcrd-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winsmcrd-devel

This package contains library source intended for building other packages which
use the "winsmcrd" feature of the "%{crate}" crate.

%package     -n %{name}+winsock2-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winsock2-devel

This package contains library source intended for building other packages which
use the "winsock2" feature of the "%{crate}" crate.

%package     -n %{name}+winspool-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winspool-devel

This package contains library source intended for building other packages which
use the "winspool" feature of the "%{crate}" crate.

%package     -n %{name}+winstring-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winstring-devel

This package contains library source intended for building other packages which
use the "winstring" feature of the "%{crate}" crate.

%package     -n %{name}+winsvc-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winsvc-devel

This package contains library source intended for building other packages which
use the "winsvc" feature of the "%{crate}" crate.

%package     -n %{name}+wintrust-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wintrust-devel

This package contains library source intended for building other packages which
use the "wintrust" feature of the "%{crate}" crate.

%package     -n %{name}+winusb-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winusb-devel

This package contains library source intended for building other packages which
use the "winusb" feature of the "%{crate}" crate.

%package     -n %{name}+winusbio-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winusbio-devel

This package contains library source intended for building other packages which
use the "winusbio" feature of the "%{crate}" crate.

%package     -n %{name}+winuser-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winuser-devel

This package contains library source intended for building other packages which
use the "winuser" feature of the "%{crate}" crate.

%package     -n %{name}+winver-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+winver-devel

This package contains library source intended for building other packages which
use the "winver" feature of the "%{crate}" crate.

%package     -n %{name}+wlanapi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wlanapi-devel

This package contains library source intended for building other packages which
use the "wlanapi" feature of the "%{crate}" crate.

%package     -n %{name}+wlanihv-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wlanihv-devel

This package contains library source intended for building other packages which
use the "wlanihv" feature of the "%{crate}" crate.

%package     -n %{name}+wlanihvtypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wlanihvtypes-devel

This package contains library source intended for building other packages which
use the "wlanihvtypes" feature of the "%{crate}" crate.

%package     -n %{name}+wlantypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wlantypes-devel

This package contains library source intended for building other packages which
use the "wlantypes" feature of the "%{crate}" crate.

%package     -n %{name}+wlclient-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wlclient-devel

This package contains library source intended for building other packages which
use the "wlclient" feature of the "%{crate}" crate.

%package     -n %{name}+wmistr-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wmistr-devel

This package contains library source intended for building other packages which
use the "wmistr" feature of the "%{crate}" crate.

%package     -n %{name}+wnnc-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wnnc-devel

This package contains library source intended for building other packages which
use the "wnnc" feature of the "%{crate}" crate.

%package     -n %{name}+wow64apiset-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wow64apiset-devel

This package contains library source intended for building other packages which
use the "wow64apiset" feature of the "%{crate}" crate.

%package     -n %{name}+wpdmtpextensions-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wpdmtpextensions-devel

This package contains library source intended for building other packages which
use the "wpdmtpextensions" feature of the "%{crate}" crate.

%package     -n %{name}+ws2bth-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ws2bth-devel

This package contains library source intended for building other packages which
use the "ws2bth" feature of the "%{crate}" crate.

%package     -n %{name}+ws2def-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ws2def-devel

This package contains library source intended for building other packages which
use the "ws2def" feature of the "%{crate}" crate.

%package     -n %{name}+ws2ipdef-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ws2ipdef-devel

This package contains library source intended for building other packages which
use the "ws2ipdef" feature of the "%{crate}" crate.

%package     -n %{name}+ws2spi-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ws2spi-devel

This package contains library source intended for building other packages which
use the "ws2spi" feature of the "%{crate}" crate.

%package     -n %{name}+ws2tcpip-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+ws2tcpip-devel

This package contains library source intended for building other packages which
use the "ws2tcpip" feature of the "%{crate}" crate.

%package     -n %{name}+wtsapi32-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wtsapi32-devel

This package contains library source intended for building other packages which
use the "wtsapi32" feature of the "%{crate}" crate.

%package     -n %{name}+wtypes-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wtypes-devel

This package contains library source intended for building other packages which
use the "wtypes" feature of the "%{crate}" crate.

%package     -n %{name}+wtypesbase-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+wtypesbase-devel

This package contains library source intended for building other packages which
use the "wtypesbase" feature of the "%{crate}" crate.

%package     -n %{name}+xinput-devel
Summary:        Interfaces to the Windows API
BuildArch:      noarch
%description -n %{name}+xinput-devel

This package contains library source intended for building other packages which
use the "xinput" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-winapi-devel -f %{oreon_filedir}/rust-winapi-devel.list

%changelog

%autochangelog
