%global source0_hash b394e3bf633888f9f4a3e1449d7c7eb39b778a2e657424177a04cde4afe6965a

# Force out of source build
%undefine __cmake_in_source_build

Name:           liborigin
Version:        3.0.3
Release:        6%{?dist}
Epoch:          1
Summary:        Library for reading OriginLab OPJ project files

License:        GPL-3.0-only
URL:            https://sourceforge.net/projects/liborigin/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

Provides:       liborigin2 = 2.0.0-21
Obsoletes:      liborigin2 < 2.0.0-21

%description
A library for reading OriginLab OPJ project files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       liborigin2-devel = 2.0.0-21
Obsoletes:      liborigin2-devel < 2.0.0-21

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
%cmake -DBUILD_STATIC_LIBS=off
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README
%license COPYING
%{_libdir}/%{name}.so.3*
%{_bindir}/opj2dat
%exclude %{_docdir}/%{name}/html
# We have license in different location and FORMAT in -doc
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/FORMAT

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc FORMAT README
%license COPYING
%{_docdir}/%{name}/html/

%changelog
%autochangelog
