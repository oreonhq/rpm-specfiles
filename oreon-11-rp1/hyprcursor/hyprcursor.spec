%global source0_hash 17e4576b884e6bdb463b445cffff099ad16647b826a87a67b78d38b8cad4c39e

Name:           hyprcursor
Version:        0.1.11
Release:        %autorelease
Summary:        The hyprland cursor format, library and utilities

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprcursor
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# test data
Source:         HyprBibataModernClassicSVG.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(tomlplusplus)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a1
mkdir -p $HOME/.icons
mv HyprBibataModernClassicSVG $HOME/.icons

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
%{_bindir}/hyprcursor-util
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.0

%files devel
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
