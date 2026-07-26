%global source0_hash 9c6c11ec8e08aa37ce8ef7c5bcbdee60bac2428faeffb07d072e572ed05eb8cd

Name:          volk
Version:       3.2.0
Release:       9%{?dist}
Summary:       The Vector Optimized Library of Kernels
License:       LGPL-3.0-or-later
URL:           https://github.com/gnuradio/%{name}
Source0:       https://github.com/gnuradio/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:       https://github.com/gnuradio/volk/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:       https://github.com/gnuradio/volk/releases/download/v2.4.1/gpg_volk_release_key.asc
# Patches:
#  https://github.com/gnuradio/volk/issues/794
Patch1:        0001-rotator2-disable-SSE-4.1-kernels-wildly-incorrect-re.patch

BuildRequires: gnupg2
BuildRequires: make
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-mako
BuildRequires: orc-devel
BuildRequires: sed
%ifnarch s390x
BuildRequires: google-cpu_features-devel
%endif
Conflicts:     python3-gnuradio < 3.9.0.0
Conflicts:     gnuradio-devel < 3.9.0.0

%description
VOLK is the Vector-Optimized Library of Kernels. It is a library that contains
kernels of hand-written SIMD code for different mathematical operations.
Since each SIMD architecture can be very different and no compiler has yet
come along to handle vectorization properly or highly efficiently, VOLK
approaches the problem differently. VOLK is a sub-project of GNU Radio.

%package devel
Summary:       Development files for VOLK
Requires:      %{name}%{?_isa} = %{version}-%{release}
Conflicts:     vulkan-volk-devel

%description devel
%{summary}.
%ifarch s390x
Conflicts:     google-cpu_features-devel
%endif

%package doc
Summary:       Documentation files for VOLK
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# fix shebangs
pushd python/volk_modtool
sed -i '1 {/#!\s*\/usr\/bin\/env\s\+python/ d}' __init__.py cfg.py
popd

%build
%cmake
%cmake_build
%cmake_build -t volk_doc

%check
cd %{__cmake_builddir}
ctest --output-on-failure

%install
%cmake_install

# docs
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a %{__cmake_builddir}/html %{buildroot}%{_docdir}/%{name}

%files
%license COPYING
%doc README.md docs/CHANGELOG.md
%{_bindir}/volk-config-info
%{_bindir}/volk_modtool
%{_bindir}/volk_profile
%{_libdir}/libvolk*.so.*
%{python3_sitearch}/volk_modtool

%files devel
%{_includedir}/volk
%{_libdir}/libvolk.so
%{_libdir}/cmake/volk
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/%{name}/html

%changelog
%autochangelog
