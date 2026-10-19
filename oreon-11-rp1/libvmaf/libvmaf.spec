%global source0_hash 80090e29d7fd0db472ddc663513f5be89bc936815e62b767e630c1d627279fe2
Name:           vmaf
Version:        3.1.0
Release:        1%{?dist}
Summary:        Video Multi-Method Assessment Fusion
License:        BSD-2-Clause-Patent
URL:            https://github.com/netflix/vmaf
Source0:        https://github.com/netflix/vmaf/archive/refs/tags/v3.1.0.tar.gz#/vmaf-3.1.0.tar.gz
%if !0%{?oreon}
ExclusiveArch:  x86_64
%endif
Requires:       libvmaf%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  vim-common
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# Unbundle
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
%oreon_autofiles libvmaf usr/*/lib*.so.*
%oreon_autofiles libvmaf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd libvmaf
ninja -vC %{_vpath_builddir} test ||:
popd
%ldconfig_scriptlets -n libvmaf
%files -f %{oreon_filedir}/main.list
%files -n libvmaf -f %{oreon_filedir}/libvmaf.list
%files -n libvmaf-devel -f %{oreon_filedir}/libvmaf-devel.list
%files -n vmaf-models -f %{oreon_filedir}/vmaf-models.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.0-1
- Import
