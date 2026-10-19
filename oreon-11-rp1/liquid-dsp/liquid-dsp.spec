%global source0_hash a0adbc3ec5630d620a55351285573f59948153a14c703fb64b4ad58989bd6e2f
%global sover 1.8.2
Name:           liquid-dsp
Version:        1.8.2
Release:        1%{?dist}
Summary:        Digital Signal Processing Library for Software-Defined Radios
License:        MIT
URL:            http://liquidsdr.org/
Source0:        https://github.com/jgaeddert/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         ppc64-configureac.patch
Patch3:         ppc64.patch
ExcludeArch:    i686
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fftw-devel
BuildRequires:  fftw-libs-single
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liquid-dsp-devel -f %{oreon_filedir}/liquid-dsp-devel.list

%changelog

%autochangelog
