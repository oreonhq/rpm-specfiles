%global source2_hash 0a6f979c9d88b0d72310b8462d2066a60b657a2f188a74c3cb19cac0064616ce
%global source1_hash fe21e7f53706176803a3d5f6e97f9c2fe0ecf8786a4a855cbc00e9e786f59541
%global source0_hash c056420ac634c8c71870ece6d7ab3986f406d1495c009fce5e14559acebc754f
Name:          notcurses
Version:       3.0.17
Release:        1%{?dist}
Summary:        Character graphics and TUI library
License:       Apache-2.0
URL:           https://nick-black.com/dankwiki/index.php/Notcurses
Source0:        https://github.com/dankamongmen/%{name}/releases/download/v%{version}/notcurses_%{version}+dfsg.orig.tar.xz
Source1:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/notcurses_%{version}+dfsg.orig.tar.xz.asc
Source2:       https://nick-black.com/dankamongmen.gpg
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-notcurses = %{version}-%{release}
# /oreon:deps
%description
Notcurses facilitates the creation of modern TUI programs,
making full use of Unicode and 24-bit TrueColor. It presents
an API similar to that of Curses, and rides atop Terminfo.
This package includes C and C++ shared libraries.

%package devel
Summary:       Development files for the Notcurses library
License:       Apache-2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the notcurses library.

%package static
Summary:       Static library for the Notcurses library
License:       Apache-2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description static
A statically-linked version of the notcurses library.

%package utils
Summary:       Binaries from the Notcurses project
License:       Apache-2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description utils
Binaries from Notcurses, and multimedia content used thereby.

%package -n python3-%{name}
Summary:       Python wrappers for notcurses
License:       Apache-2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description -n python3-%{name}
Python wrappers and a demonstration script for the notcurses library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%define __cmake_in_source_build 1

%build

%cmake -DUSE_QRCODEGEN=on -DDFSG_BUILD=on -DUSE_GPM=on \
 -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build
cd cffi
CFLAGS="-I../include -L../" %pyproject_wheel
%check

%install
%cmake_install
cd cffi
%pyproject_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/notcurses* usr/lib64/python3*/site-packages/notcurses* usr/bin/*

%files
%files -n notcurses-devel -f %{oreon_filedir}/notcurses-devel.list
%files -n notcurses-static -f %{oreon_filedir}/notcurses-static.list
%files -n notcurses-utils -f %{oreon_filedir}/notcurses-utils.list
%files -n python3-notcurses -f %{oreon_filedir}/python3-notcurses.list

%changelog

%autochangelog
