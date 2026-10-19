%global source0_hash 6afb5c231613d2fab4f1c668b7243ff9a7d6d78a7f5a2692c133f026fe508506
%global debug_package %{nil}
Name:           miniaudio
Version:        0.11.21
Release:        5%{?dist}
Summary:        Audio playback and capture library
License:        MIT-0
URL:            https://miniaud.io/
Source0:        https://github.com/mackron/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps

# /oreon:deps
%package devel
Summary: %summary
Provides:       miniaudio-static = %{version}-%{release}
BuildArch:      noarch
%description
%summary

%description devel
%summary

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%check

%install
mkdir -p %{buildroot}%{_includedir}
install -p %{name}.h %{buildroot}%{_includedir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n miniaudio-devel -f %{oreon_filedir}/miniaudio-devel.list

%changelog

%autochangelog
