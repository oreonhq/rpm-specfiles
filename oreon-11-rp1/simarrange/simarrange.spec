%global source0_hash 8579627572422da56a6e46fa0e4270d8b7cd0e82cb07b63de38668d993cb7f3e
%global commit 8238ce568c3ce23e1ad5fbfec55031907bd23f77
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global datestamp 20170316
%global relstring %{datestamp}git%{shortcommit}
Name:           simarrange
Version:        0.0^%{relstring}
Release:        1%{?dist}
Summary:        STL 2D plate packer with collision simulation
License:        AGPL-3.0-or-later
URL:            https://github.com/kliment/%{name}
Source0:        https://github.com/kliment/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch:          simarrange-opencv4.patch
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
# oreon:deps
BuildRequires:  admesh-devel
BuildRequires:  argtable-devel
BuildRequires:  gcc-c++
BuildRequires:  opencv-devel
BuildRequires:  uthash-devel
# /oreon:deps
%description
Simarrange is a program that simulates collisions between STL meshes in 2D in
order to generate tightly packed sets of parts. It takes a directory of STL
files as input and outputs STL files with combined plates of parts.
The parts are assumed to be in the correct printable orientation already.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

# bundling
rm utlist.h

%build

g++ $CXXFLAGS $LDFLAGS simarrange.c -o ./%{name} -lm `pkg-config --cflags --libs opencv` \
    -ladmesh -largtable2 -fopenmp -DPARALLEL
%install
install -Dpm0755 ./%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 ./%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
