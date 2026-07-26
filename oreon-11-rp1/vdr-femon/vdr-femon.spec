%global source0_hash bbcda3ebb98074f4569613b9ee3be99f7156d5cf63c9641e4fe7511c4b421286

%global pname   femon
%global __provides_exclude_from ^%{vdr_libdir}/.*\\.so.*$

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.8.1
%endif

Name:           vdr-%{pname}
Version:        2.4.0
Release:        41%{?dist}
Summary:        DVB frontend status monitor plugin for VDR
License:        GPL-2.0-or-later
URL:            https://github.com/rofafor/vdr-plugin-femon
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Patch0:         %{name}-gcc11.patch
# https://www.vdr-portal.de/index.php?attachment/49666-0002-femon-removal-of-deprecated-interface-functions-zip/
Patch1:         0002-femon-Removal-of-deprecated-interface-functions.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
DVB frontend status monitor is a plugin that displays some signal
information parameters of the current tuned channel on VDR's OSD.  You
can zap through all your channels and the plugin should be monitoring
always the right frontend.  The transponder and stream information are
also available in advanced display modes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n vdr-plugin-femon-%{version}

%build
%make_build

%install
%make_install
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_libdir}/libvdr-%{pname}.so.%{vdr_apiversion}

%changelog
%autochangelog
