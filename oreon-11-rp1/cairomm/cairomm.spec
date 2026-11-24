# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7e0d5c7f29175d573a03ab5c45aef63f48dd91a5caf335a404cd763e4b7cea4a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global so_version 1
%global apiver 1.0

%bcond maintainer_mode 1

Name:           cairomm
Summary:        C++ API for the cairo graphics library
Version:        1.14.6
Release:        1%{?dist}

URL:            https://www.cairographics.org
License:        LGPL-2.0-or-later
SourceLicense:  %{shrink:
                %{license} AND
                FSFAP AND
                GPL-2.0-or-later AND
                LGPL-2.1-or-later AND
                MIT
                }

%global src_base https://www.cairographics.org/releases
Source0:        https://www.cairographics.org/releases/cairomm-%{version}.tar.xz


BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  meson

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(fontconfig)

BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(cairo-xlib-xrender)

%if %{with maintainer_mode}
BuildRequires:  mm-common >= 1.0.4
%endif

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libxslt
BuildRequires:  pkgconfig(mm-common-libstdc++)

BuildRequires:  boost-devel

Provides:       cairomm%{apiver}%{?_isa} = %{version}-%{release}

%description
This library provides a C++ interface to cairo.

The API/ABI version series is %{apiver}.

%package        devel
Summary:        Development files for cairomm
Requires:       cairomm%{?_isa} = %{version}-%{release}

Provides:       cairomm%{apiver}-devel%{?_isa} = %{version}-%{release}

%description    devel
The cairomm-devel package contains libraries and header files for developing
applications that use cairomm.

The API/ABI version series is %{apiver}.

%package        doc
Summary:        Documentation for cairomm

License:        %{license} AND MIT

BuildArch:      noarch

Provides:       cairomm%{apiver}-doc = %{version}-%{release}

%{?doxygen_js_requires}

%description    doc
Documentation for cairomm can be viewed through the devhelp documentation
browser.

The API/ABI version series is %{apiver}.

%prep
%oreon_sha256
%autosetup -p1
chmod -v a-x NEWS

rm -rf untracked/docs/reference/html
rm untracked/docs/reference/cairomm-%{apiver}.tag \
   untracked/docs/reference/cairomm-%{apiver}.devhelp2

%conf
%meson \
  -Dmaintainer-mode=%{?with_maintainer_mode:true}%{?!with_maintainer_mode:false} \
  -Dbuild-documentation=true \
  -Dbuild-examples=false \
  -Dbuild-tests=true \
  -Dboost-shared=true \
  -Dwarnings=max

%build
%meson_build

%install
%meson_install

install -t %{buildroot}%{_docdir}/cairomm-%{apiver} -m 0644 -p \
    ChangeLog NEWS README.md
cp -rp examples %{buildroot}%{_docdir}/cairomm-%{apiver}/

%{doxygen_unbundle_buildroot}

%check
%meson_test

%files
%license COPYING
%{_libdir}/libcairomm-%{apiver}.so.%{so_version}{,.*}

%files devel
%{_includedir}/cairomm-%{apiver}/
%{_libdir}/libcairomm-%{apiver}.so
%{_libdir}/pkgconfig/cairomm-%{apiver}.pc
%{_libdir}/pkgconfig/cairomm-*-%{apiver}.pc
%{_libdir}/cairomm-%{apiver}/

%files doc
%license COPYING
%doc %{_docdir}/cairomm-%{apiver}/
%doc %{_datadir}/devhelp/

%changelog
%autochangelog
