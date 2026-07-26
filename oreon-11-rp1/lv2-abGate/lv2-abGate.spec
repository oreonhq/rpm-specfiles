%global source0_hash ebee1cc545b088bf6e5989c114e7e34fa9f21ac7fdb1eee3fd067bcf98703b86

%global pname abGate
Name:           lv2-abGate
Version:        1.2.0
Release:        13%{?dist}
Summary:        An LV2 Noise Gate

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://abgate.sourceforge.io/
Source0:        https://github.com/antanasbruzas/%{pname}/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Patch0:         Makefile.patch
# Patch backported from upstream https://github.com/antanasbruzas/abGate/commit/32131d50babf380e5e8f4f0bd226272df201d55a
Patch1:         %{name}-gate-ttl.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  gtkmm24-devel
Requires:       lv2 >= 1.8.1

%description
A Noise Gate plugin 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{pname}-%{version}

# Do not build Qt5 GUI for now
rm -rf abGateQt

# Fix plugin path
sed -i -e "s|/usr/lib/lv2|%{_libdir}/lv2|g" plugin_configuration.h

%build
%set_build_flags
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} INSTALL_DIR=%{buildroot}/%{_libdir}/lv2

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/%{pname}.lv2

%changelog
%autochangelog
