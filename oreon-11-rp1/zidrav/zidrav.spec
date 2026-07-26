%global source0_hash 151218577d0088a578f3a52873e3615c2595674008fdac663f35bd2c2af6e91c

Summary: Zorba's Incredible Data Repairer And Verifier
Name: zidrav
Version: 1.2.0
Release: 40%{?dist}
URL: https://sourceforge.net/projects/zidrav
Source: https://downloads.sourceforge.net/project/zidrav/zidrav4unix/%{version}/zidrav4unix-%{version}.tar.gz
Patch0: %{name}-rpm.patch
Patch1: %{name}-gcc43.patch
Patch2: %{name}-gcc60.patch
Patch3: %{name}-cxx11.patch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later

BuildRequires: make
BuildRequires:  gcc-c++
%description
ZIDRAV stands for "Zorba's Incredible Data Repairer And Verifier", and is an
extremely useful tool for cross-checking files that have been transfered via
HTTP, FTP, or some other method. What it does, is generates a checksum file,
and then by comparing that checksum with the original file, it creates a patch
file that can repair the corrupted file. Very cool, and saves re-downloading.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n zidrav4unix-%{version}
# fix DOS line endings
tr -d '\r' <zidrav.txt >zidrav.txt.cr && mv zidrav.txt.cr zidrav.txt

%build
%set_build_flags
%ifarch ppc64 s390x
export CXXFLAGS="$CXXFLAGS -DCPU_BIGENDIAN"
%endif
%make_build CXXFLAGS="$CXXFLAGS"

%install
%make_install

%files
%doc Changelog README TODO zidrav.txt
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
