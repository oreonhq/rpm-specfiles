%global source0_hash d8f5ebf6b4e15b181b34c16cccb8d6e56ca657c940e8aa9513b06cc908deb91a

# http://git.osmocom.org/osmo-fl2k
# https://github.com/osmocom/osmo-fl2k/
#%%global git_commit f8cdd64b7607f43e9813d60f473905c679bb4c19
#%%global git_date 20230403

#%%global git_short_commit %%(echo %%{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%%{git_short_commit}

Name:             osmo-fl2k
URL:              https://osmocom.org/projects/osmo-fl2k/wiki
Version:          0.2.1
Release:          2%{?dist}
# Automatically converted from old format: GPLv2+ and GPLv3+ - review is highly recommended.
License:          GPL-2.0-or-later AND GPL-3.0-or-later
BuildRequires:    cmake
BuildRequires:    gcc-c++
BuildRequires:    libusbx-devel
Requires:         systemd-udev
Summary:          Turns FL2000-based USB 3.0 to VGA adapters into low cost DACs
#Source0:          https://github.com/osmocom/osmo-fl2k/archive/%%{git_commit}/%%{name}-%%{git_suffix}.tar.gz
Source0:          https://github.com/osmocom/osmo-fl2k/archive/v%{version}/%{name}-%{version}.tar.gz

%description
Turns FL2000-based USB 3.0 to VGA adapters into low cost DACs.

%package libs
Summary:          Libraries for osmo-fl2k

%description libs
Libraries for osmo-fl2k.

%package devel
Summary:          Development files for osmo-fl2k
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for osmo-fl2k.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# Remove static objects
rm -f %{buildroot}%{_libdir}/libosmo-fl2k.a

# Fix udev rule
sed -i 's/MODE:="0666"/MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' ./osmo-fl2k.rules
install -Dpm 644 ./osmo-fl2k.rules %{buildroot}%{_prefix}/lib/udev/rules.d/10-osmo-fl2k.rules

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/fl2k_file
%{_bindir}/fl2k_fm
%{_bindir}/fl2k_tcp
%{_bindir}/fl2k_test
%{_prefix}/lib/udev/rules.d/10-osmo-fl2k.rules

%files libs
%doc AUTHORS README.md
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
