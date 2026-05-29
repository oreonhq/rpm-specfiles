%global source0_hash none
%global source1_hash 9f79e813c08fc86cfa46dd75c4fcda1a4a51b482db2607e1fcfaafb92f588a31
%global source2_hash 8bfa8306ca63e1d0cbe80be984660273b91bd5b7dd0800a6c5aa71dd8c8d775c

#define  prever     rc3
#define  prever_dot .rc3
#define  postver    a

%define version_alsa_lib  1.2.15.3
%define version_alsa_ucm  1.2.15.3
%define version_alsa_tplg 1.2.5

%global lib_patch         0
%global ucm_patch         0

Summary:  The Advanced Linux Sound Architecture (ALSA) library
Name:     alsa-lib
Version:  %{version_alsa_lib}
Release:  3%{?prever_dot}%{?dist}
License:  LGPL-2.1-or-later
URL:      https://www.alsa-project.org/
# HTTPS so spectool/mock can fetch without FTP (often blocked in builders).
Source:        https://www.alsa-project.org/files/pub/lib/alsa-lib-%{?prever}%{?postver}.tar.bz2
Source1:        https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-1.2.15.3.tar.bz2
Source2:        https://www.alsa-project.org/files/pub/lib/alsa-topology-conf-1.2.5.tar.bz2
Source10: asound.conf
Source11: modprobe-dist-alsa.conf
Source12: modprobe-dist-oss.conf
%if %{ucm_patch}
Source40: alsa-ucm-conf.patch
%endif
%if %{lib_patch}
Patch0:   alsa-git.patch
%endif
Patch1:   alsa-lib-1.2.3.1-config.patch
Patch2:   alsa-lib-1.2.10-glibc-open.patch

BuildRequires:  doxygen
BuildRequires:  autoconf automake libtool
BuildRequires: make

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA runtime libraries to simplify application
programming and provide higher level functionality as well as support for
the older OSS API, providing binary compatibility for most OSS programs.

%package  devel
Summary:  Development files from the ALSA library
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA development libraries for developing
against the ALSA libraries and interfaces.

%package  -n alsa-ucm
Summary:   ALSA Use Case Manager configuration
BuildArch: noarch
License:   BSD-3-Clause
Requires:  %{name} >= %{version_alsa_lib}

%description -n alsa-ucm
The Advanced Linux Sound Architecture (ALSA) Use Case Manager configuration
contains alsa-lib configuration of Audio input/output names and routing

%package  -n alsa-topology
Summary:   ALSA Topology configuration
BuildArch: noarch
License:   BSD-3-Clause
Requires:  %{name} >= %{version_alsa_lib}

%description -n alsa-topology
The Advanced Linux Sound Architecture (ALSA) topology configuration
contains alsa-lib configuration of SoC topology

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%(test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}%{?prever}%{?postver}
%if %{lib_patch}
%patch -P0 -p1 -b .alsa-git
%endif
%patch -P1 -p1 -b .config
%patch -P2 -p1 -b .glibc-open

%build
# This package uses top level ASM constructs which are incompatible with LTO.
# Top level ASMs are often used to implement symbol versioning.  gcc-10
# introduces a new mechanism for symbol versioning which works with LTO.
# Converting packages to use that mechanism instead of toplevel ASMs is
# recommended.
# Note: The v1.2.4 contains changes wich are compatible with gcc-10 LTO
# although using the old ASM constructs.
# Enable custom LTO flags
%define _lto_cflags -flto -ffat-lto-objects -flto-partition=none

autoreconf -vif
%configure --disable-aload --with-plugindir=%{_libdir}/alsa-lib --disable-alisp

# Remove useless /usr/lib64 rpath on 64bit archs
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1
make doc

%install
%global sysmodprobedir %{_prefix}/lib/modprobe.d

make DESTDIR=%{buildroot} install

# Install global configuration files
mkdir -p -m 755 %{buildroot}/etc
install -p -m 644 %{SOURCE10} %{buildroot}/etc

# Install the modprobe files for ALSA
mkdir -p -m 755 %{buildroot}%{sysmodprobedir}
install -p -m 644 %{SOURCE11} %{buildroot}%{sysmodprobedir}/dist-alsa.conf
# bug#926973, place this file to the doc directory
install -p -m 644 %{SOURCE12} .

# Create UCM directories
mkdir -p %{buildroot}/%{_datadir}/alsa/ucm
mkdir -p %{buildroot}/%{_datadir}/alsa/ucm2

# Unpack UCMs
tar xvjf %{SOURCE1} -C %{buildroot}/%{_datadir}/alsa --strip-components=1 "*/ucm" "*/ucm2"
%if %{ucm_patch}
patch -d %{buildroot}/%{_datadir}/alsa -p1 < %{SOURCE40}
%endif

# Create topology directory
mkdir -p %{buildroot}/%{_datadir}/alsa/topology

# Unpack topologies
tar xvjf %{SOURCE2} -C %{buildroot}/%{_datadir}/alsa --strip-components=1 "*/topology"

# Remove libtool archives.
find %{buildroot} -name '*.la' -delete

# Remove /usr/include/asoundlib.h
rm %{buildroot}/%{_includedir}/asoundlib.h

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc doc/asoundrc.txt modprobe-dist-oss.conf
%config %{_sysconfdir}/asound.conf
/%{_libdir}/libasound.so.*
/%{_libdir}/libatopology.so.*
%{_bindir}/aserver
#{_libdir}/alsa-lib/
%{_datadir}/alsa/
%exclude %{_datadir}/alsa/ucm
%exclude %{_datadir}/alsa/ucm2
%exclude %{_datadir}/alsa/topology
%{sysmodprobedir}/dist-*

%files devel
%doc TODO doc/doxygen/
%{_includedir}/alsa/
%{_includedir}/sys/asoundlib.h
%{_libdir}/libasound.so
%{_libdir}/libatopology.so
%{_libdir}/pkgconfig/alsa.pc
%{_libdir}/pkgconfig/alsa-topology.pc
%{_datadir}/aclocal/alsa.m4

%files -n alsa-ucm
# BSD
%{_datadir}/alsa/ucm
%{_datadir}/alsa/ucm2

%files -n alsa-topology
# BSD
%{_datadir}/alsa/topology

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{version_alsa_lib}-3
- Prepare for Oreon 11 (RP1)
