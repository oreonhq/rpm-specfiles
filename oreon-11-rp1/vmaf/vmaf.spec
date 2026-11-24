# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5df7386911bc15fd1ca783132528748d219768ae4fc5f8e0b61184f041648092
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           vmaf
Version:        3.2.1
Release:        1%{?dist}
Summary:        Video Multi-Method Assessment Fusion

License:        BSD-2-Clause-Patent
URL:            https://github.com/netflix/vmaf
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  vim-common

Requires:       libvmaf%{?_isa} = %{version}-%{release}

%description
VMAF is a perceptual video quality assessment algorithm developed by
Netflix. VMAF Development Kit (VDK) is a software package that contains
the VMAF algorithm implementation, as well as a set of tools that allows
a user to train and test a custom VMAF model. For an overview, read this
tech blog post, or this slide deck.

https://github.com/Netflix/vmaf/blob/master/resource/doc/VMAF_ICIP17.pdf

%package -n     libvmaf
Summary:        Library for %{name}
Provides:       bundled(libsvm) = 3.24
Provides: %{name}-static = %{version}-%{release}
Obsoletes: %{name}-static < %{version}-%{release}

%description -n libvmaf
Library for %{name}.

%package -n     libvmaf-devel
Summary:        Development files for %{name}
Requires:       libvmaf%{?_isa} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{name}-devel < %{version}-%{release}

%description -n libvmaf-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        models
Summary:        Model files for %{name}
Requires:       libvmaf = %{version}-%{release}
BuildArch:      noarch

%description    models
The %{name}-models package contains model files.
These are needed for apps that can't use the builtin models.

%prep
%oreon_sha256
%autosetup -p1
rm -rf third_party/

%build
pushd libvmaf
%meson \
 -Ddefault_library=shared
%meson_build
popd

%install
pushd libvmaf
%meson_install
popd

mkdir -p %{buildroot}%{rpmmacrodir}
cat > %{buildroot}%{rpmmacrodir}/macros.%{name} << EOF
%libvmaf_version %{version}
EOF
touch -r LICENSE %{buildroot}%{rpmmacrodir}/macros.%{name}

mkdir -p %{buildroot}%{_datadir}/model/
cp -Rp model/* %{buildroot}%{_datadir}/model/

%check
pushd libvmaf
ninja -vC %{_vpath_builddir} test ||:
popd

%ldconfig_scriptlets -n libvmaf

%files
%doc README.md
%{_bindir}/vmaf

%files models
%{_datadir}/model/

%files -n libvmaf
%doc CHANGELOG.md
%license LICENSE
%{_libdir}/*.so.3*

%files -n libvmaf-devel
%doc CONTRIBUTING.md
%{rpmmacrodir}/macros.%{name}
%{_includedir}/libvmaf/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvmaf.pc

%changelog
%autochangelog
