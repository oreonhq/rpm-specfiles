%global source0_hash 238c95ddd1a63105913d9354045eb329ad9002903a407b5cf1ab16bad324c245

Name:           xeve
Version:        0.5.1
Release:        %autorelease
Summary:        Reference MPEG-5 Part 1 (EVC) encoder

License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xeve
Source0:        https://github.com/mpeg5/xeve/archive/v%{version}/xeve-%{version}.tar.gz

Patch0:         xeve-fix-build-on-non-x86.patch
Patch1:         xeve-link-libm.patch

BuildRequires:  cmake >= 3.12
BuildRequires:  gcc
%ifarch aarch64
BuildRequires:  sse2neon-static
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The eXtra-fast Essential Video Encoder (XEVE) is an open source MPEG-5 EVC
encoder baseline profile implementation.

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
%ifarch aarch64
rm src_base/neon/sse2neon.h
%endif
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
%{_libdir}/libxeveb.so.0{,.*}

%files devel
%{_libdir}/libxeveb.so
%{_includedir}/%{name}*/
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
%autochangelog
