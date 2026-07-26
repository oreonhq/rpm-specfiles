%global source0_hash 2f1e54336ed6cc3dbab5ad5279f2520eae1a90fc80852ab005a8250a5a15d1ac

Name:           hyprwayland-scanner
Version:        0.4.2
Release:        %autorelease
Summary:        A Hyprland implementation of wayland-scanner, in and for C++

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwayland-scanner
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  cmake(pugixml)
BuildRequires:  gcc-c++

%description
%{summary}.

%package        devel
Summary:        A Hyprland implementation of wayland-scanner, in and for C++

%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
