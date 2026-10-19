%global source0_hash 1e572a0735b92aca5746c4528f9bebd35aa0ccf8619b22fa2756137a8cc9f912
%define abi 1.0
Name:           schroedinger
Version:        1.0.11
Release:        1%{?dist}
Summary:        Portable libraries for the high quality Dirac video codec
License:        GPL-1.0-or-later OR LicenseRef-Callaway-LGPLv2+ OR LicenseRef-Callaway-MIT OR LicenseRef-Callaway-MPLv1.1
URL:            http://schrodinger.sourceforge.net/schrodinger_faq.php
Source0:        http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  orc-devel
# /oreon:deps
%description
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package devel
Summary:        Development files for schroedinger
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       orc-devel%{?_isa} >= 0.4.10
%description devel
Development files for schroedinger

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# fix compatibility with gtk-doc 1.26
gtkdocize
autoreconf -fiv

%build

%configure --disable-static --enable-gtk-doc
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
find %{buildroot} -name \*.la -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n schroedinger-devel -f %{oreon_filedir}/schroedinger-devel.list

%changelog

%autochangelog
