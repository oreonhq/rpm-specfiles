%global source2_hash 4e3a0863dd448b928c5acba130974a16c1aff9a396a1b9e9cca067a198265f5e
%global source0_hash fb9ad1d429ac1765e4b192502a5ca93a54a17dbf51bdf09e4a43d2ed571555a5
Name:           glinf
Version:        1.1
Release:        1%{?dist}
Summary:        Print information about OpenGL or OpenGLES contexts
License:        MIT
URL:            https://marlam.de/glinf
Source0:        https://marlam.de/%{name}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
This is a simple tool that prints information about OpenGL or OpenGLES
contexts. It is roughly comparable to glewinfo or glxinfo, with the
following differences:
- it uses Qt for platform abstraction
- it focusses on modern OpenGL
- it prints implementation limits such as GL_MAX_DRAW_BUFFERS
- it omits information about GLX and visuals

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
