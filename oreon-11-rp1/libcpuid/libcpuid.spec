%global source0_hash 81f2f40da5d66b8220476e116cb40bca4e6a62c0d22bdeeb8e3856cf14607007

Name:           libcpuid
Version:        0.8.1
Release:        5%{?dist}
Summary:        Provides CPU identification for x86 and ARM
License:        BSD-2-Clause
URL:            https://github.com/anrieff/libcpuid
Source0:        https://github.com/anrieff/libcpuid/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
Libcpuid provides CPU identification for the x86 (x86_64) and ARM architectures.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
For details about the programming API, please see the docs
on the project's site (http://libcpuid.sourceforge.net/)

%package static
Summary:        Static development files for %{name}
Requires:       %{name}-devel%{_isa} = %{version}-%{release}

%description static
The %{name}-static package contains a library for developing applications
that need to use %{name} statically.

%package -n python3-%{name}
Summary:        Python bindings for the libcpuid library
Requires:       %{name}%{_isa} = %{version}-%{release}

%description -n python3-%{name}
The python3-%{name} package contains Python bindings for the libcpuid library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
cd python
# CFFI tries to compile the bindings when get_requires_for_build_wheel is called
# https://github.com/python-cffi/cffi/issues/190
mv setup.py{,.ignore}
%pyproject_buildrequires
mv setup.py{.ignore,}

%build
autoreconf -vfi
%configure
%make_build

pushd python
%pyproject_wheel
popd

%install
%make_install
# WARNING: empty dependency_libs variable. remove the pointless .la
rm %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

pushd python
%pyproject_install
popd

%pyproject_save_files -L %{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %pytest python/tests

%files
%doc Readme.md
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_bindir}/cpuid_tool
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.*

%files static
%{_libdir}/%{name}.a

%files -n python3-%{name} -f %{pyproject_files}
%doc python/README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.1-5
- Prepare for Oreon 11 (RP1)
