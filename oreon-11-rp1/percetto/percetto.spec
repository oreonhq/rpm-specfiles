%global source0_hash a9532581c6e4b60a147e1cabf35d6ba0ae74b2e75075a132c1ae9aa109c9c5eb
Name:           percetto
Version:        0.1.6
Release:        1%{?dist}
Summary:        Minimal C wrapper for Perfetto SDK to enable app tracing
License:        Apache-2.0
URL:            https://github.com/olvaffe/percetto
Source0:        https://github.com/olvaffe/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{url}/commit/fd59d8b9bf05f4b0e7b681623156b99d41a8f6a7.patch
Patch:          %{url}/commit/90912f0e119f7b067e0e4a3d1d540225df8936e6.patch
Patch:          percetto-soversion.patch
ExclusiveArch:  aarch64 x86_64
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  perfetto-sdk
# /oreon:deps
%description

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dperfetto-sdk=%{_datadir}/perfetto/sdk -Dwerror=false
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n percetto-devel -f %{oreon_filedir}/percetto-devel.list

%changelog

%autochangelog
