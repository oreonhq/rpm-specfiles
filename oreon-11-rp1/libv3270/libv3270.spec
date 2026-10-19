%global source0_hash 74a20001fe2e8752af32be8b2f5d71e561b5b28f0a27be826ce69f9a092effb9
%bcond docs 1
%global major_sover 5
%global minor_sover 5
Name:           libv3270
Version:        5.5.0
Release:        1%{?dist}
Summary:        3270 Virtual Terminal for GTK+3
License:        LGPL-3.0-only
URL:            https://github.com/PerryWerneck/libv3270
Source0:        https://github.com/PerryWerneck/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  graphviz
BuildRequires:  gtk3-devel
BuildRequires:  lib3270-devel
BuildRequires:  meson
# /oreon:deps
%description
Originally designed as part of the pw3270 application, this library provides a
TN3270 virtual terminal widget for GTK+3.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel%{?_isa}
Requires:       lib3270-devel%{?_isa}
Requires:       glade-libs%{?_isa}
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
rm -r %{buildroot}%{_datadir}/glade/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libv3270-devel -f %{oreon_filedir}/libv3270-devel.list
%files -n libv3270-doc -f %{oreon_filedir}/libv3270-doc.list

%changelog

%autochangelog
