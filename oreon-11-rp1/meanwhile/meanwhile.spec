%global source0_hash 10de306f03897572b30ce68ca80dffd04ec218f6842bbe0a47bb8cce933698d0
Name:           meanwhile
Version:        1.1.1
Release:        11%{?dist}
Summary:        Lotus Sametime Community Client library
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/obriencj/%{name}
Source0:        https://github.com/obriencj/meanwhile/archive/refs/tags/v1.1.1.tar.gz#/meanwhile-1.1.1.tar.gz
Patch0:         %{name}-file-transfer.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
The heart of the %{name} Project is the %{name} library, providing the basic
Lotus Sametime session functionality along with the core services; Presence
Awareness, Instant Messaging, Multi-user Conferencing, Preferences Storage,
Identity Resolution, and File Transfer.

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name}, you
will need to install %{name}-devel.

%package doc
Summary:        Documentation for the %{name} library
License:        LicenseRef-Callaway-GFDL
BuildArch:      noarch
%description doc
Documentation for the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{optflags} -fno-tree-vrp"
autoreconf -vif
%configure --enable-doxygen
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
mkdir docs
mv %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/{html,samples} docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/
%ldconfig_scriptlets libs
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n meanwhile-devel -f %{oreon_filedir}/meanwhile-devel.list
%files -n meanwhile-doc -f %{oreon_filedir}/meanwhile-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.1-11
- Prepare for Oreon 11 (RP1)
