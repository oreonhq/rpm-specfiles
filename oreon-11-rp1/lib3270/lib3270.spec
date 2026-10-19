%global source0_hash d61e9467662cb781463ea6fe8d4d74e640cf68e6bd6b2c7e9d69e355998328f8
%bcond docs 1
%global major_sover 5
%global minor_sover 5
Name:           lib3270
Version:        5.6.0
Release:        1%{?dist}
Summary:        TN3270 Protocol Library
License:        LGPL-3.0-only
URL:            https://github.com/PerryWerneck/lib3270
Source0:        https://github.com/PerryWerneck/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  graphviz
BuildRequires:  libcurl-devel
BuildRequires:  meson
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
# /oreon:deps
%description
lib3270 is a TN3270 protocol library, originally designed as part of the pw3270
application.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%if %{with docs}
doxygen doxygen
%endif
%install
%meson_install
%find_lang %{name}-%{major_sover}.%{minor_sover}
rm %{buildroot}%{_libdir}/%{name}.a
rm %{buildroot}%{_libdir}/pkgconfig/%{name}-static.pc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n lib3270-devel -f %{oreon_filedir}/lib3270-devel.list
%files -n lib3270-doc -f %{oreon_filedir}/lib3270-doc.list

%changelog

%autochangelog
