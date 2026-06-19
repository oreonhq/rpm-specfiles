%global source0_hash 8d55c7ec1a9ad4e70fe91fbe129a1d4dd288bce766f466cba07a29452b3cecd8

Name:           xevd
Version:        0.5.0
Release:        %autorelease
Summary:        Reference MPEG-5 Part 1 (EVC) decoder

License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xevd
Source0:        https://github.com/mpeg5/xevd/archive/v%{version}/xevd-%{version}.tar.gz

Patch0:         xevd-fix-build-on-non-x86.patch
Patch1:         xevd-fix-neon-header.patch
Patch2:         xevd-link-libm.patch

BuildRequires:  cmake >= 3.12
BuildRequires:  gcc

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The eXtra-fast Essential Video Decoder (XEVD) is an open source MPEG-5 EVC
decoder baseline profile implementation.

%package libs
Summary:        Library files for %{name}

%description libs
Library files for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
rm -rf src_main
echo "v%{version}" > version.txt

%build
%cmake -DSET_PROF=BASE
%cmake_build

%install
%cmake_install
rm -rfv %{buildroot}%{_libdir}/%{name}*

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}*

%files libs
%license COPYING
%{_libdir}/lib%{name}*.so.0{,.*}
%{_libdir}/libxevdb.so.0{,.*}

%files devel
%{_libdir}/lib%{name}*.so
%{_libdir}/libxevdb.so
%{_includedir}/%{name}*/
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
%autochangelog
