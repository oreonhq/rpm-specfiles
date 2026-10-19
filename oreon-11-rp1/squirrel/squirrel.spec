%global source0_hash 02805414cfadd5bbb921891d3599b83375a40650abd6404a8ab407dc5e86a996
Name:           squirrel
Version:        3.2
Release:        6%{?dist}
Summary:        High level imperative/OO programming language
License:        Zlib
URL:            http://squirrel-lang.org/
Source0:        https://github.com/albertodemichelis/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sq.1
Patch0:         squirrel-3.2-fedora.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# /oreon:deps
%description
Squirrel is a high level imperative/OO programming language, designed
to be a powerful scripting tool that fits in the size, memory bandwidth,
and real-time requirements of applications like games.

%package libs
Summary:        Libraries needed to run Squirrel scripts
%description libs
Libraries needed to run Squirrel scripts.

%package devel
Summary:        Development files needed to use Squirrel libraries
Requires:       %{name}-libs = %{version}-%{release}
%description devel
Development files needed to use Squirrel libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DDISABLE_STATIC=1
%cmake_build
pushd doc
make html
popd
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n squirrel-libs -f %{oreon_filedir}/squirrel-libs.list
%files -n squirrel-devel -f %{oreon_filedir}/squirrel-devel.list

%changelog

%autochangelog
