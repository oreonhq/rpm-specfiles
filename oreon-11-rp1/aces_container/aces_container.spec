%global source0_hash cbbba395d2425251263e4ae05c4829319a3e399a0aee70df2eb9efb6a8afdbae
Name:           aces_container
Version:        1.0.2
Release:        1%{?dist}
Summary:        ACES Container Reference
License:        AMPAS
URL:            https://github.com/ampas/aces_container
Source0:        https://github.com/ampas/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         Switch-to-CMAKE-default-variables.patch
Patch1:         Set-the-appropriate-SONAME-for-the-library.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
This folder contains a reference implementation for an ACES container
file writer intended to be used with the Academy Color Encoding
System (ACES). The resulting file is compliant with the ACES container
specification (SMPTE S2065-4). However, there are a few things that are
not demonstrated by this reference implementation.

    Stereo channels
    EndOfFileFiller
    Arbitrary attributes and naming validations
    half type attributes
    keycode value validations

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod -x aces_writeattributes.*

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles aces_container-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n aces_container-devel -f %{oreon_filedir}/aces_container-devel.list

%changelog

%autochangelog
