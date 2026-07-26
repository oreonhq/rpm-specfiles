%global source0_hash 7b907a4b5b201ce0d321b7d3e4190735bfde20f6e158bf4ab8ac4016b1436899

# Are licenses packaged using %%license?
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 8
%global with_license 1
%endif # 0%%{?fedora} >= 22 || 0%%{?rhel} >= 8

Name:		GarminPlugin
Version:	0.3.27
Release:	28%{?dist}
Summary:	Garmin Communicator Plugin port for Linux
%if 0%{?rhel} && 0%{?rhel} <= 5
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

# ===== License-breakdown =====
#
# GPLv3+
# ------
# * except the files explicitly named below
#
# BSD (3 clause)
# --------------
# src/npapi/npruntime.h
#
# MPLv1.1 and (GPLv2 or LGPLv2)
# -----------------------------
# src/npapi/npapi.h
# src/npapi/npfunctions.h
# src/npapi/nptypes.h
#
# Automatically converted from old format: BSD and GPLv3+ and (MPLv1.1 and (GPLv2 or LGPLv2)) - review is highly recommended.
License:	LicenseRef-Callaway-BSD AND GPL-3.0-or-later AND (LicenseRef-Callaway-MPLv1.1 AND (GPL-2.0-only OR LicenseRef-Callaway-LGPLv2))
URL:		http://www.andreas-diesner.de/garminplugin
Source0:	https://github.com/adiesner/%{name}/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?rhel} && 0%{?rhel} <= 5
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

BuildRequires:  gcc-c++
BuildRequires:	garmintools-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	tinyxml-devel
BuildRequires:	zlib-devel
BuildRequires: make

Requires:	garmintools%{?_isa}
Requires:	mozilla-filesystem%{?_isa}

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
%if 0%{?rhel} && 0%{?rhel} <= 5
%{__rm} -rf %{buildroot}
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

%{__mkdir} -p %{buildroot}%{_libdir}/mozilla/plugins
%{__install} -pm 0755 src/np%{name}.so			\
	%{buildroot}%{_libdir}/mozilla/plugins

%files
%if 0%{?with_license}
%license COPYING
%else  # 0%%{?with_license}
%doc COPYING
%endif # 0%%{?with_license}
%doc HISTORY README test.html
%{_libdir}/mozilla/plugins/np%{name}.so

%changelog
%autochangelog
