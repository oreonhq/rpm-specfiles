%global source0_hash 10de306f03897572b30ce68ca80dffd04ec218f6842bbe0a47bb8cce933698d0

Name:           meanwhile
Version:        1.1.1
Release:        11%{?dist}
Summary:        Lotus Sametime Community Client library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/obriencj/%{name}

Source:        https://github.com/obriencj/meanwhile/archive/refs/tags/v1.1.1.tar.gz#/meanwhile-1.1.1.tar.gz
Patch0:         %{name}-file-transfer.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0) >= 2.0.0

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
# Automatically converted from old format: GFDL - review is highly recommended.
License:        LicenseRef-Callaway-GFDL
BuildArch:      noarch

%description doc
Documentation for the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
export CFLAGS="%{optflags} -fno-tree-vrp"
autoreconf -vif
%configure --enable-doxygen
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

# Prepare documents for inclusion through %%doc in the %%files section
mkdir docs
mv %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/{html,samples} docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/

%ldconfig_scriptlets libs

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc docs/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.1-11
- Prepare for Oreon 11 (RP1)
