%global source0_hash 73e6793a0289f17996e605188e63963ef413cd42a9fddfbe233ef3aa735aa810
Name:             libosmo-dsp
URL:              http://osmocom.org/projects/libosmo-dsp
Version:          0.4.0
Release:        1%{?dist}
License:          GPL-2.0-or-later
Summary:        A library with SDR DSP primitives
Source0:        https://gitea.osmocom.org/sdr/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
A library with SDR DSP primitives.

%package devel
Summary:          Development files for libosmo-dsp
Requires:         %{name} = %{version}-%{release}
%description devel
Development files for libosmo-dsp.

%package doc
Summary:          Documentation files for libosmo-dsp
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch
%description doc
Documentation files for libosmo-dsp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

test -x ./git-version-gen && echo %{version}-%{release} > .tarball-version 2>/dev/null
autoreconf -fi
%configure --disable-static
make CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags} -lm" %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/libosmodsp %{buildroot}%{_docdir}/%{name}/html
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libosmo-dsp-devel -f %{oreon_filedir}/libosmo-dsp-devel.list
%files -n libosmo-dsp-doc -f %{oreon_filedir}/libosmo-dsp-doc.list

%changelog

%autochangelog
