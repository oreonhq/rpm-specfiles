%global source0_hash fc5acdbdfd4c3a5d296732ccfb2fec1fcfb3e7e5f41bf9a0789f8b54c161f5f7
%global source1_hash 99218ce2597be53e11b1d92f35d35a71332d01a87264f27561eaafc56de27394
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: rpm-sequoia
Version: 1.9.0
Release: 1%{?dist}
Summary: RPM OpenPGP backend
License: LGPL-2.0-or-later
URL: https://github.com/rpm-software-management/rpm-sequoia
Source0: https://github.com/rpm-software-management/rpm-sequoia/archive/refs/tags/v%{version}.tar.gz
Source1: rpm-sequoia-%{version}-vendor.tar.xz
Patch0: rpm-sequoia-nettle-sys-2.3.2.patch

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: rustc
BuildRequires: cargo
BuildRequires: pkgconf
BuildRequires: clang
BuildRequires: nettle-devel
BuildRequires: gmp-devel
BuildRequires: patchelf
%endif

%description
rpm-sequoia is the OpenPGP backend used by rpm.

%package devel
Summary: RPM OpenPGP backend
Requires: rpm-sequoia%{?_isa} = %{version}-%{release}

%description devel
rpm-sequoia is the OpenPGP backend used by rpm.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n rpm-sequoia-%{version} -p1
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
%oreon_cargo_build

%install
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir} %{buildroot}%{_libdir}/pkgconfig
so=$(find target/release -name 'librpm_sequoia.so' -type f | head -1)
install -p -m 755 "$so" %{buildroot}%{_libdir}/librpm_sequoia.so.1
ln -sf librpm_sequoia.so.1 %{buildroot}%{_libdir}/librpm_sequoia.so
patchelf --set-soname librpm_sequoia.so.1 %{buildroot}%{_libdir}/librpm_sequoia.so.1
hdr=$(find target -name 'rpm-sequoia.h' | head -1)
install -p -m 644 "$hdr" %{buildroot}%{_includedir}/rpm-sequoia.h
cat > %{buildroot}%{_libdir}/pkgconfig/rpm-sequoia.pc << EOF
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: rpm-sequoia
Description: RPM OpenPGP backend
Version: %{version}
Libs: -L\${libdir} -lrpm_sequoia
Cflags: -I\${includedir}
EOF
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE.txt

%files devel -f %{_builddir}/%{name}-devel.files
