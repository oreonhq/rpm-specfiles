%global source0_hash 9737c0e52b893e9085de80fa2369e97af2be16c3a71298f88fd2cfaa1f205fca
%global forgeurl https://github.com/phkehl/ubloxcfg
%global commit 499048ba8b3b9d0ca5d752c56f14c48117ebbb8e
%forgemeta
Name:           ubloxcfg
Version:        1.16
Release:        1%{?dist}
Summary:        u-blox 9 positioning receivers configuration library and tool
License:        GPL-3.0-only AND LGPL-3.0-only
URL:            %forgeurl
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         001-rpath-remove.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  perl-Data-Float
BuildRequires:  perl-Path-Tiny
BuildRequires:  sed
# /oreon:deps
%description
This package implements a library (API) to deal with the new configuration
interface introduced in u-blox 9 positioning receivers.

A command line "cfgtool" is provided to configure a receiver from the
configuration defined in a human-readable configuration file, as well as a few
other functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
This package contains development headers and files for %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%autopatch -p1

# drop hardcoded CFLAGS
sed -e 's/-O3//g' -i */CMakeLists.txt
# copy various docs to be unique names
cp ff/LICENSE ff-LICENSE
cp ubloxcfg/LICENSE ubloxcfg-LICENSE
cp cfgtool/LICENSE cfgtool-LICENSE
cp cfgtool/README.md cfgtool-README.md
cp ff/README.md ff-README.md

%build

%cmake
%cmake_build
doxygen ubloxcfg/
%install
%cmake_install
rm -rf %{buildroot}/usr/share/doc/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch s390x x86_64
make test || true
%else
make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ubloxcfg-devel -f %{oreon_filedir}/ubloxcfg-devel.list
%files -n ubloxcfg-doc -f %{oreon_filedir}/ubloxcfg-doc.list

%changelog

%autochangelog
