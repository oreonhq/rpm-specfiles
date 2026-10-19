%global source0_hash 3daa1bdd4cb48628f2d137af6643203030199c48cbc88ec1e862a6830a047769
%global git_commit 84dcf73625513af44e711b2c99e21ee2c33b7eff
%global git_date 20250331
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
Name:             libosmocore
URL:              https://osmocom.org/projects/libosmocore
Version:          0.9.6
Release:        1%{?dist}
License:          GPL-2.0-or-later AND GPL-3.0-or-later AND AGPL-3.0-or-later
Summary:        Utility functions for OsmocomBB, OpenBSC and related projects
Source0:        %{name}-%{version}-%{git_date}git%{git_short_commit}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  gnutls-devel
BuildRequires:  libmnl-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtool
BuildRequires:  liburing-devel
BuildRequires:  libusb1-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  make
BuildRequires:  pcsc-lite-devel
BuildRequires:  python3
BuildRequires:  sed
# /oreon:deps
%description
A collection of common code used in various sub-projects inside the Osmocom
family of projects (OsmocomBB, OpenBSC, ...).

%package devel
Summary:          Development files for libosmocore
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         libosmo-dsp-devel, libtalloc-devel
%description devel
Development files for libosmocore.

%package doc
Summary:        Documentation files for libosmocore
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
Documentation files for libosmocore.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} \;
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%ifnarch s390x
make check
%endif
%files -f %{oreon_filedir}/main.list
%files -n libosmocore-devel -f %{oreon_filedir}/libosmocore-devel.list
%files -n libosmocore-doc -f %{oreon_filedir}/libosmocore-doc.list

%changelog

%autochangelog
