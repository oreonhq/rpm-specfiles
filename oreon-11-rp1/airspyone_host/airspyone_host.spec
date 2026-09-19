%global source0_hash fcca23911c9a9da71cebeffeba708c59d1d6401eec6eb2dd73cae35b8ea3c613

#%%global git_commit bfb667080936ca5c2d23b3282f5893931ec38d3f
#%%global git_date 20180615

#%%global git_short_commit %%(echo %%{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%%{git_short_commit}

Name:           airspyone_host
Version:        1.0.10
Release:        15%{?git_suffix}%{?dist}
Summary:        AirSpy host tools and library

# following is LGPL-2.1-or-later
# airspy-tools/getopt/getopt.*
# following is BSD-3-Clause
# libairspy/src/airspy.*
# libairspy/src/airspy_commands.h
# following is MIT
# libairspy/src/filters.h
# libairspy/iqconverter_*
# everything else is GPL-2.0-or-later
License:        GPL-2.0-or-later AND MIT AND BSD-3-Clause AND LGPL-2.1-or-later
URL:            http://airspy.com/
#Source:        https://github.com/airspy/%%{name}/archive/%%{git_commit}/%%{name}-%%{git_suffix}.tar.gz
Source:         https://github.com/airspy/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/airspy/airspyone_host/pull/98
Patch:          airspyone_host-1.0.10-c23-fix.patch
# CMake 4.0 and GNUInstallDirs support
# Cherry-picked from https://github.com/airspy/airspyone_host/pull/100
Patch:          100.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libusbx-devel
BuildRequires:  systemd
Requires:       systemd-udev

%description
Software for AirSpy, a project to produce a low cost, open
source software radio platform.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        MIT AND BSD-3-Clause
Summary:        Development files for %{name}

%description devel
Files needed to develop software against libairspy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove win stuff
rm -rf libairspy/vc

# Fix udev rule
sed -i -e 's/GROUP="plugdev"/ENV{ID_SOFTWARE_RADIO}="1"/g' airspy-tools/52-airspy.rules

%build
%cmake -DINSTALL_UDEV_RULES=on

%cmake_build

%install
%cmake_install

# Remove static object
rm -f %{buildroot}%{_libdir}/libairspy.a

# Move udev rule to correct location
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspy.rules %{buildroot}%{_udevrulesdir}

%post
%?ldconfig
%udev_rules_update

%postun
%?ldconfig
%udev_rules_update

%files
%license airspy-tools/LICENSE.md
%doc README.md
%{_bindir}/airspy_*
%{_libdir}/libairspy.so.*
%{_udevrulesdir}/52-airspy.rules

%files devel
%{_includedir}/libairspy
%{_libdir}/pkgconfig/libairspy.pc
%{_libdir}/libairspy.so

%changelog
%autochangelog
