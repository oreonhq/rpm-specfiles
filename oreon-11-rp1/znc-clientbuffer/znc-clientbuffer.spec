%global source0_hash 9d06192979aac34267141d799b05a3f91c1311714703347bda2a896c38de9a80

%global forgeurl https://github.com/CyberShadow/znc-clientbuffer
%global commit 9766a4ad5d27e815bbbc8b6842e13b7b4b5826f6
%forgemeta

%global modname clientbuffer
%global znc_version %((znc -v 2>/dev/null || echo 'a 0') | head -1 | awk '{print $2}')

Name:           znc-%{modname}
Version:        0
Release:        0.32%{?dist}
Summary:        ZNC module for client specific buffers

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  gcc-c++
BuildRequires:  python-devel
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  znc-devel
Requires:       znc%{?_isa} = %znc_version

%description
The client buffer module maintains client specific buffers for identified
clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" znc-buildmod %{modname}.cpp

%install
install -Dpm0755 %{modname}.so %{buildroot}%{_libdir}/znc/%{modname}.so

%files
%{_libdir}/znc/%{modname}.so

%changelog
%autochangelog
