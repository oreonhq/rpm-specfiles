%global source0_hash 9387082434a2176a01a20f64d0d35acd34dc1901e80db428689cc60ddbf49c53

Name:       vnc-reflector
Version:    1.2.4 
Release:    43%{?dist}
Summary:    A specialized, multiplexing vnc proxy server
# LICENSE:  BSD-3-Clause
# region.c: MIT-open-group AND SMLNJ
License:    BSD-3-Clause AND MIT-open-group AND SMLNJ
URL:        http://sourceforge.net/projects/vnc-reflector
Source0:    http://dl.sf.net/vnc-reflector/vnc_reflector-%{version}.tar.gz
# Bug #569350, submitted to upstream
# <http://sourceforge.net/tracker/?func=detail&aid=2984246&group_id=38605&atid=422840>
Patch0:     %{name}-1.2.4-loggingfix.patch
# In upstream after 1.2.4 as commit r192
Patch1:     %{name}-1.2.4-rfb_format_buffer_overflow.patch
# Remove _LITTLE_ENDIAN identifier clash, bug #1125258, submitted to upstream
# <https://sourceforge.net/p/vnc-reflector/bugs/8/>
Patch2:     %{name}-1.2.4-unionfix.patch
# Respect compiler and linker flags, submitted to upstream
# <https://sourceforge.net/p/vnc-reflector/bugs/9/>
Patch3:     %{name}-1.2.4-Respect-external-CFLAGS-and-LDFLAGS.patch
# Adapt to GCC 15, bug #2341514, porposed upstream
# <>https://sourceforge.net/p/vnc-reflector/bugs/10/
Patch4:     %{name}-1.2.4-Port-to-ISO-C23.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  zlib-devel 

%description
Reflector is a specialized VNC server which acts as a proxy sitting between
real VNC server (a host) and a number of VNC clients. It was designed to work
efficiently with large number of clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n vnc_reflector
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p1
%patch -P4 -p1

%build
%{make_build} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS='%{__global_ldflags}'

%install
# No install target in the makefile.
install -D -t %{buildroot}%{_bindir} vncreflector

%files
%license LICENSE
%doc README ChangeLog
%{_bindir}/vncreflector

%changelog
%autochangelog
