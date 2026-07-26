%global source0_hash 77fe893cbe6973afa85c736bc50f2a96888ba238b29b6aec8ecb60f81e2e899d

# no debug symbol in header only package
%global debug_package %{nil}

%global forgeurl https://github.com/free-audio/clap
Version:        1.2.7
%global tag %{version}
%forgemeta

Name:           clap
Release:        %autorelease
Summary:        Audio Plugin API
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
CLAP stands for CLever Audio Plugin. It is an interface that provides a stable
ABI to define a standard for Digital Audio Workstations and audio plugins
(synthesizers, audio effects, ...) to work together.

%package        devel
Summary:        Development files for CLAP
Provides:       %{name}-static = %{version}-%{release}

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
%{_includedir}/clap/
%{_libdir}/cmake/clap/
%{_libdir}/pkgconfig/clap.pc

%changelog
%autochangelog
