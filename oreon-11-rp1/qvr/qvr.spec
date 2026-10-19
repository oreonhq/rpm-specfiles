%global source2_hash 4e3a0863dd448b928c5acba130974a16c1aff9a396a1b9e9cca067a198265f5e
%global source0_hash e6f83f89da8dccdc7dfedf726d2ee742336668549599a74574df928b162b1d53
Name:           qvr
Version:        4.1.0
Release:        1%{?dist}
Summary:        QT library for VR applications
License:        MIT
URL:            https://marlam.de/qvr
Source0:        https://marlam.de/%{name}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libxkbcommon-devel
BuildRequires:  make
BuildRequires:  openvr-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  texlive-amsmath
BuildRequires:  texlive-babel-english
BuildRequires:  texlive-beamer
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-latex
BuildRequires:  texlive-textpos
BuildRequires:  vrpn-devel
# /oreon:deps
%description
QVR is a library that makes writing Virtual Reality (VR) applications very
easy. It is based on Qt and requires no other libraries.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxkbcommon-devel
Requires:       openvr-devel
Requires:       qt6-qtbase-devel
Requires:       vrpn-devel
%description    devel
This package provides development headers and libraries for %{name}.

%package        doc
Summary:        Additional documentation for %{name}
BuildArch:      noarch
%description    doc
This package provides additional documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

pushd doc/intro-slides
%make_build
popd
pushd libqvr
%cmake -DQVR_BUILD_DOCUMENTATION=ON
%cmake_build
popd
%install
pushd libqvr
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd libqvr
%ctest
%files -f %{oreon_filedir}/main.list
%files -n qvr-devel -f %{oreon_filedir}/qvr-devel.list
%files -n qvr-doc -f %{oreon_filedir}/qvr-doc.list

%changelog

%autochangelog
