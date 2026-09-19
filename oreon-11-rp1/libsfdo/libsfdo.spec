%global source0_hash d1f2d8b5edec827fd386c22d6f9151377ec7c194dca4d293e3abad9df9974209

Name:           libsfdo
Version:        0.1.3
Release:        5%{?dist}
Summary:        A collection of libraries implementing freedesktop.org specifications

License:        BSD-2-Clause
URL:            https://gitlab.freedesktop.org/vyivel/libsfdo
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libsfdo-*.so.0

%files devel
%{_includedir}/sfdo-*.h
%{_libdir}/libsfdo-*.so
%{_libdir}/pkgconfig/libsfdo-*.pc

%changelog
%autochangelog
