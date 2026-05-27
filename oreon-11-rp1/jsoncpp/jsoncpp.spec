%global source0_hash f93b6dd7ce796b13d02c108bc9f79812245a82e577581c4c9aabe57075c90ea2

# Build documentation in HTML with images
%bcond_without jsoncpp_enables_doc

%global jsondir json

# Avoid accidental so-name bumps.
# ATTENTION!!!  You need to run a bootstrap build
# of cmake *BEFORE* bumping the so-name here!
%global sover 26


Name:           jsoncpp
Version:        1.9.6
Release:        3%{?dist}
Summary:        JSON library implemented in C++

License:        LicenseRef-Fedora-Public-Domain OR MIT
URL:            https://github.com/open-source-parsers/%{name}
Source0:        https://github.com/open-source-parsers/jsoncpp/archive/1.9.6.tar.gz#/jsoncpp-1.9.6.tar.gz

BuildRequires:  cmake >= 3.1
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%description
%{name} is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.


%package        devel
Summary:        Development headers and library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development headers and library for %{name}.


%if %{with jsoncpp_enables_doc}
%package        doc
Summary:        Documentation for %{name}

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  hardlink

BuildArch:      noarch

%description    doc
This package contains the documentation for %{name}.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p 1
%if %{with jsoncpp_enables_doc}
doxygen -s -u doc/doxyfile.in
sed -i -e 's!^DOT_FONTNAME.*=.*!DOT_FONTNAME =!g' doc/doxyfile.in
%endif


%build
%cmake                                         \
  -DBUILD_STATIC_LIBS:BOOL=OFF                 \
  -DBUILD_OBJECT_LIBS:BOOL=OFF                 \
  -DJSONCPP_WITH_CMAKE_PACKAGE:BOOL=ON         \
  -DJSONCPP_WITH_EXAMPLE:BOOL=OFF              \
  -DJSONCPP_WITH_PKGCONFIG_SUPPORT:BOOL=ON     \
  -DJSONCPP_WITH_POST_BUILD_UNITTEST:BOOL=OFF  \
  -DJSONCPP_WITH_STRICT_ISO:BOOL=ON            \
  -DJSONCPP_WITH_TESTS:BOOL=ON                 \
  -DJSONCPP_WITH_WARNING_AS_ERROR:BOOL=OFF     \
  -DPYTHON_EXECUTABLE:STRING="%{__python3}"
%cmake_build

%if %{with jsoncpp_enables_doc}
# Build the doc
cp -p %{__cmake_builddir}/version .
%{__python3} doxybuild.py --with-dot --doxygen /usr/bin/doxygen
rm -f version
%endif


%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}
install -pm 0644 README.md %{buildroot}%{_docdir}/%{name}

%if %{with jsoncpp_enables_doc}
mkdir -p %{buildroot}%{_docdir}/%{name}/html
cp -a dist/doxygen/jsoncpp-api-html-/* %{buildroot}%{_docdir}/%{name}/html
find %{buildroot}%{_docdir} -type d -print0 | xargs -0 chmod -c 0755
find %{buildroot}%{_docdir} -type f -print0 | xargs -0 chmod -c 0644
hardlink -cfv %{buildroot}%{_docdir}/%{name}
%endif


%check
# Run tests single threaded.
%global _smp_mflags -j1
%ctest


%ldconfig_scriptlets


%files
%license AUTHORS LICENSE
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.md
%if %{with jsoncpp_enables_doc}
%exclude %{_docdir}/%{name}/html
%endif
%{_libdir}/lib%{name}.so.%{sover}*
%{_libdir}/lib%{name}.so.%{version}


%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{jsondir}
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/%{name}.pc


%if %{with jsoncpp_enables_doc}
%files doc
%license %{_datadir}/licenses/%{name}
%doc %{_docdir}/%{name}
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.6-3
- Prepare for Oreon 11 (RP1)
