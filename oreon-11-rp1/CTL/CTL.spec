%global source0_hash 0a9f5f3de8964ac5cca31597aca74bf915a3d8214e3276fdcb52c80ad25b0096
Name:           CTL
Version:        1.5.3
Release:        1%{?dist}
Summary:        The Color Transformation Language
License:        AMPAS
URL:            http://github.com/ampas/CTL
Source0:        http://github.com/ampas/%{name}/archive/ctl-%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-ctlrender-Add-missing-Half-Iex-libraries-at-link-tim.patch
Provides: ctl = %{version}-%{release}
Provides:       OpenEXR_CTL-libs = %{version}-%{release}
Obsoletes:      OpenEXR_CTL-libs < 1.5.2-1
# oreon:deps
BuildRequires:  aces_container-devel
BuildRequires:  cmake
BuildRequires:  cmake(OpenEXR)
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel
# /oreon:deps
%description
The Color Transformation Language, or CTL, is a programming language
for digital color management.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ilmbase-devel%{?_isa}
Requires:       OpenEXR-devel%{?_isa}
Provides:       OpenEXR_CTL-devel = %{version}-%{release}
Obsoletes:      OpenEXR_CTL-devel < 1.5.2-1
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package docs
Summary:        Documentation for %{name}
%description docs
This package contains documentation files for %{name}.

%package -n     OpenEXR_CTL
Summary:        A simplified OpenEXR interface to CTL
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n  OpenEXR_CTL
exrdpx is an initial version of a CTL-driven file converter
that translates DPX files into OpenEXR files and vice versa.
The conversion between the DPX and OpenEXR color spaces is
handled by CTL transforms.

exr_ctl_exr is an initial version of a program that can bake
the effect of a series of CTL transforms into the pixels of
an OpenEXR file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n CTL-ctl-%{version}
# remove executable bit
chmod -x lib/IlmCtl/Ctl*.cpp

%build

%cmake \
  -DCTL_BUILD_TESTS=OFF
%cmake_build
%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_prefix}/doc
%oreon_autofiles CTL-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles CTL-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles OpenEXR_CTL usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n CTL-devel -f %{oreon_filedir}/CTL-devel.list
%files -n CTL-docs -f %{oreon_filedir}/CTL-docs.list
%files -n OpenEXR_CTL -f %{oreon_filedir}/OpenEXR_CTL.list

%changelog

%autochangelog
