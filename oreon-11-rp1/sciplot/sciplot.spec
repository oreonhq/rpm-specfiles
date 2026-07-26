%global source0_hash d5f8fa7783920c0db4f54d8d9cea8a5e50be99153e81dcaccf91532994ebbad0

%global forgeurl https://github.com/sciplot/sciplot

%global common_description %{expand:
The goal of the sciplot project is to enable a C++ programmer to conveniently
plot beautiful graphs as easy as in other high-level programming languages.
sciplot is a header-only library that needs a C++17-capable compiler, but has
no external dependencies for compiling. The only external runtime dependencies
are gnuplot-palettes for providing color palettes and a gnuplot executable.}

Name:           sciplot
Version:        0.3.1
Release:        %autorelease
Summary:        Modern C++ scientific plotting library powered by gnuplot

License:        MIT
URL:            https://sciplot.github.io/
Source:         %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Enable testing with CMake and ctest
Patch:          %{forgeurl}/pull/115.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description    %{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

%description    devel %{common_description}

%package        examples
Summary:        Various examples showcasing %{name}
Requires:       /usr/bin/gnuplot

%description    examples %{common_description}

This package contains a number of examples using and showcasing %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix permissions
chmod -x LICENSE README.md

%build
# Building docs requires mkdocs which isn't packaged
%cmake -DSCIPLOT_BUILD_DOCS=OFF
%cmake_build

%install
%cmake_install

# Install examples manually and rename them for clarity
for f in %{_vpath_builddir}/examples/example-*; do
  install -Dpm0755 "$f" "%{buildroot}%{_bindir}/sciplot-$(basename "$f")"
done

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}/
%{_datadir}/%{name}/

%files examples
%license LICENSE
%{_bindir}/sciplot-example-*

%changelog
%autochangelog
