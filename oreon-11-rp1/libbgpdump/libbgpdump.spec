%global source0_hash 7c6dc32c367590a527752ca84c727ab4cbedc16a5abe5384dc523e563907abe0

Summary:        C library for analyzing BGP related dump files
Name:           libbgpdump
Version:        1.6.2
Release:        8%{?dist}
License:        MIT AND GPL-2.0-or-later
URL:            https://github.com/RIPE-NCC/bgpdump/wiki
Source0:        https://github.com/RIPE-NCC/bgpdump/releases/download/v%{version}/%{name}-%{version}.tgz
# Upstream .so name versioning proposed at https://github.com/RIPE-NCC/bgpdump/issues/11
Patch0:         https://github.com/RIPE-NCC/bgpdump/commit/2fc04a828fe35dc84654164157966b0823429c81.patch#/libbgpdump-1.6.2-soname-versioning.patch
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel

%description
Libbgpdump is a C library designed to help with analyzing BGP related
dump files in Zebra/Quagga or MRT RIB (Multi-Threaded Routing Toolkit
Routing Information Base) format, e.g. produced by Zebra/Quagga, BIRD,
OpenBGPD or PyRT.

%package devel
Summary:        Development files for the bgpdump library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libbgpdump-devel package includes header files and libraries necessary
for developing programs which use the bgpdump C library.

%package -n bgpdump
Summary:        MRT file reader for handling BGP related data
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n bgpdump
Bgpdump translates (possibly compressed) binary MRT RIB dump files, e.g.
produced by Zebra/Quagga, BIRD, OpenBGPD or PyRT, into human readable
output. Publicly available MRT RIB dump files are e.g. supplied by the
RIPE NCC routing information service (RIPE RIS).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.a

%check
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$RPM_BUILD_ROOT%{_libdir}"
$RPM_BUILD_ROOT%{_bindir}/bgpdump -T

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog README
%{_libdir}/%{name}.so.0*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/bgpdump_attr.h
%{_includedir}/bgpdump_formats.h
%{_includedir}/bgpdump_lib.h
%{_includedir}/bgpdump_mstream.h

%files -n bgpdump
%{_bindir}/bgpdump

%changelog
%autochangelog
