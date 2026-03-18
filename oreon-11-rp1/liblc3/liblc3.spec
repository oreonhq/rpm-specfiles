Name:          liblc3
Version:       1.1.3
Release:       7%{?dist}
Summary:       Low Complexity Communication Codec (LC3)

License:       Apache-2.0
URL:           https://github.com/google/liblc3
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:        0001-Revert-build-fix-rpath-issue.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: python3-devel

%description
The Low Complexity Communication Codec (LC3) is used by
Bluetooth as the codec for LE Audio. It enables high
quality audio over the low bandwidth connections provided
by Bluetooth LE.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package -n python3-lc3
Summary: Python3 bindings for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description -n python3-lc3
Python3 bindings for %{name}.

%package utils
Summary: Utility package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Uitlities for command line use of and testing
the %{name} library.

%prep
%autosetup -p1

%build
%meson -Dtools=true -Dpython=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%{_libdir}/liblc3.so.1{,.*}

%files devel
%{_includedir}/lc3*
%{_libdir}/pkgconfig/lc3.pc
%{_libdir}/liblc3.so

%files -n python3-lc3
%pycached %{python3_sitelib}/lc3.py

%files utils
%{_bindir}/dlc3
%{_bindir}/elc3

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-7
- Prepare for Oreon 11 (RP1)
