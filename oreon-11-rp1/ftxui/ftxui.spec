%global source0_hash 45819c1e54914783d4a1ca5633885035d74146778a1f74e1213cdb7b76340e71

%global forgeurl https://github.com/ArthurSonzogni/FTXUI
Version:        6.1.9
%forgemeta

Name:           ftxui
Release:        %autorelease
Summary:        A simple cross-platform C++ library for terminal based user interfaces

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
%if 0%{?fedora}
# testing dependencies
BuildRequires:  cmake(gtest)
BuildRequires:  cmake(benchmark)
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake \
    -GNinja \
%if 0%{?fedora}
    -DFTXUI_BUILD_TESTS=ON \
%else
    -DFTXUI_BUILD_TESTS=OFF \
%endif

%cmake_build

%install
%cmake_install

%check
%if 0%{?fedora}
%ctest
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/libftxui-*.so.%{version}

%files devel
%{_includedir}/ftxui/
%{_libdir}/cmake/ftxui/
%{_libdir}/pkgconfig/ftxui.pc
%{_libdir}/libftxui-*.so

%changelog
%autochangelog
