%global source0_hash 33c42ebc2e6088570421e282c6332e899705d42b4f73ebd1212e6a11da714dd4

%global sover 1.7.0

Name:           liquid-dsp
Version:        1.7.0
Release:        2%{?dist}
Summary:        Digital Signal Processing Library for Software-Defined Radios

License:        MIT
URL:            http://liquidsdr.org/
Source0:        https://github.com/jgaeddert/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch configure.ac for ppc64
Patch1:         ppc64-configureac.patch
# fixes ppc64 altivec, other 64-bit problems. Patch by Dan Horák.
# https://github.com/jgaeddert/liquid-dsp/pull/136
Patch3:         ppc64.patch

ExcludeArch:    i686

BuildRequires:  gcc
BuildRequires:  fftw-devel fftw-libs-single
BuildRequires:  autoconf automake libtool
BuildRequires:  make

%description
Digital signal processing library for software-defined radios

%package -n %{name}-devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
Digital signal processing library for software-defined radios

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
autoreconf -f -i

%build
%configure --exec_prefix=/ --enable-simdoverride
%make_build

%check
make check

%install
%make_install
pushd ${RPM_BUILD_ROOT}/%{_libdir} > /dev/null 2>&1
rm libliquid.a
chmod a+x libliquid.so.%{sover}
popd > /dev/null 2>&1

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libliquid.so.1
%{_libdir}/libliquid.so.%{sover}

%files -n %{name}-devel
%{_includedir}/liquid/
%{_libdir}/libliquid.so

%changelog
%autochangelog
