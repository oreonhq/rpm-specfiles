%global source0_hash 649b50bde99272b97c66af2a8400163e2f84eae072d252daa26baaaf0866a1c2

Name:           libaribcaption
Version:        1.1.2
Release:        %autorelease
Summary:        Portable ARIB STD-B24 Caption Decoder/Renderer

License:        MIT
URL:            https://github.com/xqq/libaribcaption
Source0:        https://github.com/xqq/libaribcaption/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         libaribcaption-version.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(fontconfig)

%description
Decoder and renderer for handling ARIB STD-B24 based broadcast captions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/aribcaption/*
%{_libdir}/cmake/aribcaption/aribcaption-*.cmake
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
