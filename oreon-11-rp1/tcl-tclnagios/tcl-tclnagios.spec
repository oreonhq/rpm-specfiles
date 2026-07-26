%global source0_hash 6f7b142a5a2c8c8a2ce007500514937b81ec67185e0fb68f1ffec86602875e39

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}

%global shortname tclnagios

Name:           tcl-tclnagios
Version:        1.3
Release:        22%{?dist}
Summary:        Library to assist with writing Nagios plugins in Tcl

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/gitwart/%{shortname}
Source0:        https://github.com/gitwart/%{shortname}/archive/v%{version}/%{shortname}-%{version}.tar.gz

Provides:       tclnagios = %{version}-%{release}
BuildArch:      noarch
BuildRequires: make
BuildRequires:  tcl-devel
Requires:       tcllib

%description
A set of library functions to make it easier to write Nagios plugins in Tcl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{shortname}-%{version}
chmod a-x examples/*

%build
%configure --datadir=%{tcl_sitelib}
%make_build

%install
%make_install

%files
%doc examples/
%license COPYING
%{tcl_sitelib}/%{shortname}%{version}

%changelog
%autochangelog
