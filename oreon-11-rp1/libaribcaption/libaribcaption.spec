%global source0_hash 278d03a0a662d00a46178afc64f32535ede2d78c603842b6fd1c55fa9cd44683
Name:           libaribcaption
Version:        1.1.1
Release:        1%{?dist}
Summary:        Portable ARIB STD-B24 Caption Decoder/Renderer
License:        MIT
URL:            https://github.com/xqq/libaribcaption
Source0:        https://github.com/xqq/libaribcaption/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         libaribcaption-version.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(fontconfig)
# /oreon:deps
%description
Decoder and renderer for handling ARIB STD-B24 based broadcast captions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libaribcaption-devel -f %{oreon_filedir}/libaribcaption-devel.list

%changelog

%autochangelog
