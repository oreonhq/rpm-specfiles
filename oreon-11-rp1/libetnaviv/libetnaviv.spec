%global source0_hash cc234638dffb3faf2696f8b5fb91a157416674c86fb2701800dac55f502ffabd
%global commit 60105d1b0755e48b37d779d8a2b9c4b458b5a2fd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%undefine _debugsource_packages
Name:           libetnaviv
Version:        1.0.0
Release:        1%{?dist}
Summary:        Vivante GPU user-space driver
License:        MIT
URL:            https://github.com/etnaviv/libetnaviv.git
Source0:        https://github.com/etnaviv/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         https://github.com/lkundrak/libetnaviv/commit/e61d9e169.patch#/0001-etna.h-include-other-headers-from-the-same-directory.patch
# oreon:deps

# /oreon:deps
%description
Project Etnaviv is an open source user-space driver for the Vivante GCxxx
series of embedded GPUs.

%package -n etnaviv-headers
Summary:        Header files for etnaviv.
BuildArch:      noarch
%description -n etnaviv-headers
Header files for etnaviv.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1

%build

%install
mkdir -p %{buildroot}%{_includedir}/etnaviv/
install -pm644 src/*.h %{buildroot}%{_includedir}/etnaviv/
%oreon_autofiles etnaviv-headers usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n etnaviv-headers -f %{oreon_filedir}/etnaviv-headers.list

%changelog

%autochangelog
