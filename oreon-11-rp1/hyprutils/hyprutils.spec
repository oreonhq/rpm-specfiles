%global source0_hash bcbf05252b392b8837eec9ba9855ff6ddab571f9795917c7139215ae4b2cf1bc

Name:           hyprutils
Version:        0.7.1
Release:        %autorelease
Summary:        Hyprland utilities library used across the ecosystem

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprutils
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(pixman-1)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.6

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
