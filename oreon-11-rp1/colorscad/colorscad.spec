%global source0_hash 5b9ee7fee6f5a8dee31088b537bd3550eafdfa59e361a5cd4685d178dff8f482

%global forgeurl https://github.com/jschobben/colorscad

Name:    colorscad
Version: 0.8.0
Release: 1%{?dist}
Summary: Helps with exporting an OpenSCAD model with color information preserved

%forgemeta
License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}

Requires: openscad
Requires: sed

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(lib3mf)

# Tests
BuildRequires: openscad
BuildRequires: sed
BuildRequires: /usr/bin/shasum

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
    ExcludeArch: %{ix86}
%endif

%description
This script helps with exporting an OpenSCAD model to AMF or 3MF format,
with color information preserved. The colors are simply assigned using
OpenSCADs color() statement, so generally speaking the output will look
like the preview (F5) view in OpenSCAD.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
PATH=%{buildroot}%{_bindir}:$PATH test/run.sh

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%doc %attr(0644, -, -) colors.scad
%{_bindir}/colorscad
%{_bindir}/3mfmerge

%changelog
%autochangelog
