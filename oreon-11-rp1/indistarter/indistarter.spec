%global source0_hash 1d3acc0c25ac844e9100794e57d1def73993332452d859d7c841cb59573b4ea2
%global _smp_build_ncpus 1
%global gittag v2.5.2
Name:           indistarter
%if "%{?gittag}"
Version:        2.5.2
%else
Version:        2.3.1^%{date}%{shortcommit}
%endif
Release:        1%{?dist}
Summary:        GUI to start, stop and control an INDI server
License:        GPL-3.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND BSD-3-Clause AND MPL-1.1
URL:            https://github.com/pchev/%{name}
%if "%{?gittag}"
Source0:        https://github.com/pchev/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
%else
%endif
Patch100:       indistarter-2.0.0_fix_debuginfo.patch
ExclusiveArch:  %{fpc_arches}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  fpc-src
BuildRequires:  lazarus-lcl-nogui
BuildRequires:  lazarus-lcl-qt6
BuildRequires:  lazarus-tools
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Indistarter is a user interface to run a INDI server.
You can configure different profile for your astronomical equipment.
The INDI server can be launched locally or remotely on another computer.
In this last case a ssh tunnel is established to allow local client connection.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

%build

./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}
%make_build fpcopts="-O1 -gw3 -fPIC" LCL_PLATFORM=qt6
%install
%make_install PREFIX=%{buildroot}%{_prefix}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
