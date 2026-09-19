%global source0_hash 627774783cf16016e6500c38f095bf5f1e12354e56f1839c821e5cca8b459b9a

Name:           usnic-tools
Version:        1.1.2.2
Release:        3%{?dist}
Summary:        Diagnostic tool for Cisco usNIC devices
# Automatically converted from old format: GPLv2 or BSD - review is highly recommended.
License:        GPL-2.0-only OR LicenseRef-Callaway-BSD
Url:            https://github.com/cisco/usnic_tools
Source0:        https://github.com/cisco/usnic_tools/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires: make
BuildRequires:  libfabric-devel >= 1.3.0
BuildRequires:  gcc
BuildRequires:  chrpath
ExcludeArch:    %{arm}

%description
This is a simple tool for extracting some diagnostics and informational
meta data out of Cisco usNIC devices using the Cisco usNIC extensions
in libfabric.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%{make_install}
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/usnic_devinfo

%files
%{_bindir}/*
%license COPYING
%doc README.md
%{_mandir}/man1/usnic_devinfo.1.gz

%changelog
%autochangelog
