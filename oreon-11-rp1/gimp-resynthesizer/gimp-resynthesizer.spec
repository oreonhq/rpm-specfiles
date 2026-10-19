%global source0_hash d0f459e551d428e3cd3fec4c3ebfe448e6e2947d9b24553373308d6d41ddd580
%global pkgname     resynthesizer
%global srcversion  3.0
Name:     gimp-%{pkgname}
Version:  3.0.1
Release:        1%{?dist}
Summary:        GIMP plug-in for texture synthesis
License:  GPL-3.0-or-later
URL:      https://github.com/bootchk/%{pkgname}
Source0:        https://github.com/bootchk/%{pkgname}/archive/refs/tags/v%{srcversion}/%{pkgname}-%{version}.tar.gz
Requires:       gimp >= 3.0
Requires:       python3-gobject >= 3.40
Requires:       gegl04
ExcludeArch: s390x
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gimp-devel-tools
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gegl-0.4)
BuildRequires:  pkgconfig(gimp-3.0)
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
Modern texture synthesis plugin for GIMP 3 implementing:
- AI-assisted inpainting and object removal
- Neural texture synthesis
- Seamless pattern generation
- Context-aware image manipulation
- GPU-accelerated processing (CUDA/OpenCL)

%prep

%autosetup -n %{pkgname}-%{?commit:%{commit}}%{!?commit:%{srcversion}}

%build

%meson 
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_metainfodir}
install -Dpm 644 %{name}.metainfo.xml %{buildroot}%{_metainfodir}/
%oreon_autofiles main

%check

%meson_test
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
