%global source0_hash 64066fbd54e71d7ae4c8a4116997448a72808a2813cff3bb5d2c28f0fce9e0e5
%undefine __cmake_in_source_build
%global apidocs 1
%global tests 1
%if 0%{?fedora} < 24 && 0%{?rhel} <= 7 || (0%{?oreon} >= 11) 
%global virtuoso 1
%endif
Summary:        Qt wrapper API to different RDF storage solutions
Name:    soprano
Version: 2.9.4
Release:        1%{?dist}
License: LicenseRef-Callaway-LGPLv2+
URL:     https://quickgit.kde.org/?p=soprano.git
%if 0%{?snap:1}
Source0:        https://downloads.sf.net/soprano/soprano-%{version}.tar.bz2
%else
%endif
Patch1:        soprano-2.9.4-gcc6.patch
%if 0%{?apidocs}
%endif
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
Provides: soprano-backend = %{version}-%{release}
Provides: soprano-backend-redland =  %{version}-%{release}
%if 0%{?virtuoso}
Requires: redland-virtuoso
Provides: soprano-backend-virtuoso = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  clucene-core-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  kde4-macros(api)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtXml)
BuildRequires:  pkgconfig(raptor2)
BuildRequires:  pkgconfig(rasqal)
BuildRequires:  pkgconfig(redland)
BuildRequires:  qt4-doc
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package backend-redland 
Summary: Redland backend for %{name}
Provides: %{name}-backend = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description backend-redland 
%{summary}.

%if 0%{?virtuoso}
%package backend-virtuoso
Summary: Virtuoso backend for %{name}
BuildRequires: libiodbc-devel
%if 0%{?tests}
BuildRequires: virtuoso-opensource
%endif
Provides: %{name}-backend = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: redland-virtuoso
%description backend-virtuoso 
%{summary}.
%endif

%package apidocs
Summary: Soprano API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the Soprano API documentation in HTML
format for easy browsing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n soprano-%{version}%{?pre:-%{pre}}

%patch -P1 -p1 -b .gcc6

%build

%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DDATA_INSTALL_DIR:PATH=%{_kde4_appsdir} \
  -DQT_DOC_DIR=%{?_qt4_docdir}%{!?_qt4_docdir:%(pkg-config --variable=docdir Qt)} \
  -DSOPRANO_BUILD_API_DOCS:BOOL=%{!?apidocs:0}%{?apidocs} \
  -DSOPRANO_BUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DSOPRANO_DISABLE_SESAME2_BACKEND:BOOL=ON \
  %{!?virtuoso:-DSOPRANO_DISABLE_VIRTUOSO_BACKEND:BOOL=ON}
%cmake_build
%install
%cmake_install
%if 0%{?apidocs}
mkdir -p %{buildroot}%{_kde4_docdir}/HTML/en
cp -a %{_vpath_builddir}/docs/html %{buildroot}%{_kde4_docdir}/HTML/en/soprano-apidocs
find %{buildroot}%{_kde4_docdir}/HTML/en/ -name 'installdox' -exec rm -fv {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion soprano)" = "%{version}"
%if 0%{?tests:1}
export CTEST_OUTPUT_ON_FAILURE=1
time make -C %{_vpath_builddir} test ARGS="--timeout 300 --output-on-failure -R virtuosobackendtest" ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n soprano-devel -f %{oreon_filedir}/soprano-devel.list
%files -n soprano-backend-redland -f %{oreon_filedir}/soprano-backend-redland.list
%files -n soprano-apidocs -f %{oreon_filedir}/soprano-apidocs.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.4-38
- Import
