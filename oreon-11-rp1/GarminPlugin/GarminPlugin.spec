%global source0_hash 7b907a4b5b201ce0d321b7d3e4190735bfde20f6e158bf4ab8ac4016b1436899
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%global with_license 1
%endif # 0%%{?fedora} >= 22 || 0%%{?rhel} >= 8
Name:		GarminPlugin
Version:	0.3.27
Release:        28%{?dist}
Summary:        Garmin Communicator Plugin port for Linux
License:	LicenseRef-Callaway-BSD AND GPL-3.0-or-later AND (LicenseRef-Callaway-MPLv1.1 AND (GPL-2.0-only OR LicenseRef-Callaway-LGPLv2))
URL:		http://www.andreas-diesner.de/garminplugin
Source0:        https://github.com/adiesner/%{name}/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:	garmintools%{?_isa}
Requires:	mozilla-filesystem%{?_isa}
# oreon:deps
BuildRequires:  garmintools-devel
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  tinyxml-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This browser plugin has the same methods and properties as the
official Garmin Communicator Plugin.  It can be used to transfer
GPX files (Geocache Descriptions) to your garmin device using
the official Garmin Javascript API.  Its functionality depends
on the device you use:
  * Edge305/Forerunner305: ReadFitnessData, ReadGpsData, No write support
  * Edge705/Oregon/Dakota: ReadFitnessData, ReadGpsData, Write Gpx files
  * Edge800: ReadFitnessData, Write Gpx/Tcx Files
  * Other devices: Executes external command to write Gpx to device

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Remove unneeded stuff.
%{__rm} -rf build/

%build

pushd src
%configure --without-optflags
%{__make} %{?_smp_mflags}
popd
%install
%{__mkdir} -p %{buildroot}%{_libdir}/mozilla/plugins
%{__install} -pm 0755 src/np%{name}.so			\
	%{buildroot}%{_libdir}/mozilla/plugins
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
