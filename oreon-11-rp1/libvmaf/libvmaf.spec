# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 80090e29d7fd0db472ddc663513f5be89bc936815e62b767e630c1d627279fe2
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           vmaf
Version:        3.1.0
Release:        1%{?dist}
Summary:        Video Multi-Method Assessment Fusion

License:        BSD-2-Clause-Patent
URL:            https://github.com/netflix/vmaf
Source0:        https://github.com/netflix/vmaf/archive/v3.1.0/vmaf-3.1.0.tar.gz

# This project relies on AVX for the default x86 tuning; other arches are allowed on Oreon
%if !0%{?oreon}
ExclusiveArch:  x86_64
%endif

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  vim-common


# Enforce our own build version for library
Requires:       libvmaf%{?_isa} = %{version}-%{release}
# Upstream only provides a static library
# Packages using libvmaf must Requires this:
#%%{?libvmaf_version:Requires: libvmaf%%{?_isa} = %%{libvmaf_version}}


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
#Some repo provides it
Provides: %{name}-static = %{version}-%{release}
Obsoletes: %{name}-static < %{version}-%{release}

%description -n libvmaf
Library for %{name}.

%package -n     libvmaf-devel
Summary:        Development files for %{name}
Requires:       libvmaf%{?_isa} = %{version}-%{release}
#Some repo provides it
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
%oreon_verify_sources
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

#RPM Macros support
mkdir -p %{buildroot}%{rpmmacrodir}
cat > %{buildroot}%{rpmmacrodir}/macros.%{name} << EOF
# libvmaf RPM Macros
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.0-1
- Import
