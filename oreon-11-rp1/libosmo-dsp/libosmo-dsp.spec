%global source0_hash 73e6793a0289f17996e605188e63963ef413cd42a9fddfbe233ef3aa735aa810

Name:             libosmo-dsp
URL:              http://osmocom.org/projects/libosmo-dsp
Version:          0.4.0
Release:          3%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
BuildRequires:    fftw-devel
BuildRequires:    doxygen
BuildRequires:    graphviz
BuildRequires:    make
Summary:          A library with SDR DSP primitives
# workaround for https://osmocom.org/issues/6765
Source0:          https://gitea.osmocom.org/sdr/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source0:          http://cgit.osmocom.org/libosmo-dsp/snapshot/%{name}-%{version}.tar.bz2

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

%autosetup -p1

%build
# Fix pkg-config version, related to rhbz#1692517, it could be dropped
# when fixed upstream
test -x ./git-version-gen && echo %{version}-%{release} > .tarball-version 2>/dev/null

autoreconf -fi
%configure --disable-static
# -lm is due to https://osmocom.org/issues/6764
make CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags} -lm" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# remove libtool
rm -f %{buildroot}%{_libdir}/*.la

# fix docs location
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/libosmodsp %{buildroot}%{_docdir}/%{name}/html

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/osmocom
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%files doc
%{_docdir}/%{name}/html

%changelog
%autochangelog
