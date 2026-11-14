# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 18ff5504fa9cc8a2b1f3591180d90ead16c8a2ea78e530523b46eab70e1ca6b9

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           lcms2
Version:        2.20
Release:        1%{?dist}
Summary:        Color Management Engine
License:        MIT
URL:            https://www.littlecms.com/
Source0:        https://github.com/mm2/Little-CMS/releases/download/lcms2.%{version}/lcms2-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  oreon-rpm-macros
BuildRequires:  zlib-devel

%description
LittleCMS intends to be a small-footprint color management engine, with
special focus on accuracy and performance. It uses the International Color
Consortium standard (ICC), which is the modern standard when regarding color
management. The ICC specification is widely used and is referred to in many
International and other de-facto standards.

%package        devel
Summary:        Development files for LittleCMS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Development files for LittleCMS.

%package        utils
Summary:        Utility applications for LittleCMS
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The utility applications for LittleCMS. Includes the ICC profile linker,
the transform tool, the PostScript tool and the JPEG and TIFF colour
conversion tools.

%prep
%oreon_sha256
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

install -d %{buildroot}%{_docdir}/%{name}-devel
for pdf in doc/*.pdf; do
  install -p -m 0644 "$pdf" "%{buildroot}%{_docdir}/%{name}-devel/$(basename "$pdf" | tr ' ' '_')"
done

%check
%make_build check

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/liblcms2.so.2*

%files devel
%{_docdir}/%{name}-devel
%{_includedir}/lcms2.h
%{_includedir}/lcms2_plugin.h
%{_libdir}/liblcms2.so
%{_libdir}/pkgconfig/lcms2.pc

%files utils
%{_bindir}/jpgicc
%{_bindir}/linkicc
%{_bindir}/psicc
%{_bindir}/tificc
%{_bindir}/transicc
%{_mandir}/man1/jpgicc.1*
%{_mandir}/man1/linkicc.1*
%{_mandir}/man1/psicc.1*
%{_mandir}/man1/tificc.1*
%{_mandir}/man1/transicc.1*

%changelog
%autochangelog
