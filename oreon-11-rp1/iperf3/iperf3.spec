%global source0_hash 4dc1bc31ef4a4018973a6f543a3229fab020b20b26229bc7a40ed6779e367699

Name:           iperf3
Version:        3.22
Release:        1%{?dist}
Summary:        Measurement tool for TCP/UDP bandwidth performance

# src/cjson.{c,h} and src/net.{c,h} are MIT
# part of the code is dtoa
# part of src/net.c is BSD-3-Clause-HP
# src/queue.h is BSD-3-Clause
# src/units.{c.h} is NCSA
# src/portable_endian.h is LicenseRef-Fedora-Public-Domain
License:        BSD-3-Clause-LBNL AND MIT AND dtoa AND BSD-3-Clause AND NCSA AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/esnet/iperf
Source0:        https://github.com/esnet/iperf/archive/refs/tags/3.22.tar.gz#/iperf-3.20.tar.gz
BuildRequires:  libuuid-devel
BuildRequires:  gcc
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel
BuildRequires:  make

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
various parameters and UDP characteristics. Iperf reports bandwidth, delay
jitter, data-gram loss.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n iperf-%{version} -p1

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall -C src INSTALL_DIR="%{buildroot}%{_bindir}"
mkdir -p %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_libdir}/libiperf.la

%files
%doc README.md LICENSE RELNOTES.md
%{_mandir}/man1/iperf3.1.gz
%{_mandir}/man3/libiperf.3.gz
%{_bindir}/iperf3
%{_libdir}/*.so.*

%files          devel
%{_includedir}/iperf_api.h
%{_libdir}/*.so

%changelog
%autochangelog
