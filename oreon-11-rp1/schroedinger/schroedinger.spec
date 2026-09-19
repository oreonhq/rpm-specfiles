%global source0_hash 1e572a0735b92aca5746c4528f9bebd35aa0ccf8619b22fa2756137a8cc9f912

%define abi 1.0

Name:           schroedinger
Version:        1.0.11
Release:        35%{?dist}
Summary:        Portable libraries for the high quality Dirac video codec

# No version is given for the GPL or the LGPL
# Automatically converted from old format: GPL+ or LGPLv2+ or MIT or MPLv1.1 - review is highly recommended.
License:        GPL-1.0-or-later OR LicenseRef-Callaway-LGPLv2+ OR LicenseRef-Callaway-MIT OR LicenseRef-Callaway-MPLv1.1
URL:            http://schrodinger.sourceforge.net/schrodinger_faq.php
Source0:        http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  glew-devel >= 1.5.1
BuildRequires:  gtk-doc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

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

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install
find %{buildroot} -name \*.la -delete

%ldconfig_scriptlets

%files
%doc NEWS TODO
%license COPYING*
%{_libdir}/libschroedinger-%{abi}.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/schroedinger
%{_includedir}/schroedinger-%{abi}
%{_libdir}/*.so
%{_libdir}/pkgconfig/schroedinger-%{abi}.pc

%changelog
%autochangelog
