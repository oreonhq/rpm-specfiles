%global source0_hash 5613e60b1273bc2199a8b1a69dd6c211cd2db79b132796db286e572a9c672b2a
%global oiio_major_minor_ver %(rpm -q --queryformat='%%{version}' OpenImageIO-devel | cut -d . -f 1-2)
%bcond  qt5     1
%bcond  qt6     1
%bcond  ninja   1
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%global llvm_compat 19
%endif
Name:           openshadinglanguage
Version:        1.15.2.0%{?commit:~%{snapdate}git%{sub %{commit} 1 7}}
%global so_version 1.15
Release:        1%{?dist}
Summary:        Advanced shading language for production GI renderers
License:        %{shrink:
                BSD-3-Clause AND
                Apache-2.0 AND
                LicenseRef-Fedora-Public-Domain AND
                CC-BY-4.0 AND
                MIT
                }
SourceLicense:  %{shrink:
                %{license} AND
                BSD-2-Clause AND
                (BSD-2-Clause OR LicenseRef-Fedora-Public-Domain)
                }
URL:            https://github.com/AcademySoftwareFoundation/OpenShadingLanguage
%if %{undefined commit}
Source0:        https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/archive/v%{so_version}.2.0/OpenShadingLanguage-%{so_version}.2.0.tar.gz
%else
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if %{with ninja}
%endif
%if %{with qt5}
%endif
%if %{with qt6}
%endif
ExcludeArch:    %{ix86} %{arm}
Obsoletes:      %{name}-doc < 1.12.13.0-6
%global common_description %{expand:
Open Shading Language (OSL) is a small but rich language for programmable
shading in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.}
# oreon:deps
BuildRequires:  bison
BuildRequires:  clang19-devel
BuildRequires:  cmake
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenImageIO)
BuildRequires:  cmake(pybind11)
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  llvm19-devel
BuildRequires:  ninja-build
BuildRequires:  partio-devel
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  robin-map-static
# /oreon:deps
%description %{common_description}

%package example-shaders-source
Summary:        OSL shader examples
License:        BSD-3-Clause AND Apache-2.0
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-common-headers
%description example-shaders-source %{common_description}

This package contains some OSL example shaders.

%package common-headers
Summary:        OSL standard library and auxiliary headers
License:        BSD-3-Clause AND Apache-2.0
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description common-headers %{common_description}

This package contains the OSL standard library headers, as well
as some additional headers useful for writing shaders.

%package -n OpenImageIO-plugin-osl
Summary:        OpenImageIO input plugin
License:        BSD-3-Clause AND Apache-2.0
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description -n OpenImageIO-plugin-osl %{common_description}

This is a plugin to access OSL from OpenImageIO.

%package        libs
Summary:        OpenShadingLanguage's libraries
%description    libs %{common_description}

%package        devel
Summary:        Development files for %{name}
License:        BSD-3-Clause AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python3-%{name}
Summary:        Advanced shading language for production GI renderers
License:        BSD-3-Clause AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain
BuildRequires:  cmake(pybind11)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    -n python3-%{name} %{common_description}

%prep

%if %{undefined commit}
%autosetup -p1 -n OpenShadingLanguage-%{version}
%else
%autosetup -p1 -n OpenShadingLanguage-%{commit}
%endif

# Use python3 binary instead of unversioned python
sed -i -e "s|COMMAND python|COMMAND python3|" $(find . -iname CMakeLists.txt)

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

# Remove files that are under licenses that are acceptable in Fedora, but which
# we haven’t included in any License field, so we want to make sure that the
# files bearing them aren’t installed.
#
# Pixar (https://github.com/spdx/license-list-XML/issues/2225):
rm -v doc/build_install/windows/build_osl.py
# BSD-2-Clause
rm -v src/doc/markdeep.min.js
# BSD-2-Clause OR LicenseRef-Fedora-Public-Domain:
rm -v src/doc/docs.css

# Make sure we didn’t miss any bundled and pre-minified JavaScript
# https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/#_compilationminification
find . -type f -name '*.min.js' -print -delete

%build

%cmake \
%if %{with ninja}
   -G Ninja \
%endif
   -DCMAKE_CXX_STANDARD=17 \
   -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
   -DCMAKE_SKIP_RPATH=TRUE \
   -DCMAKE_SKIP_INSTALL_RPATH=YES \
   -DLLVM_STATIC=0 \
   -DLLVM_CONFIG=$(which llvm-config%{?llvm_compat:-%{llvm_compat}}) \
   -DOSL_SHADER_INSTALL_DIR:PATH=%{_datadir}/%{name}/shaders/ \
   -Dpartio_DIR=%{_prefix} \
   -DPARTIO_INCLUDE_DIR=%{_includedir} \
   -DPARTIO_LIBRARIES=%{_libdir}/libpartio.so \
   -DPYTHON_VERSION=%{python3_version} \
   -DSTOP_ON_WARNING=OFF \
   -DINSTALL_DOCS=OFF
%cmake_build
mkdir -p %{_vpath_builddir}/man/man1
for cmd in oslc oslinfo osltoy testrender testshade testshade_dso
do
  cmdpath="%{_vpath_builddir}/bin/${cmd}"
  summary="$(
    LD_LIBRARY_PATH='%{_vpath_builddir}/lib' "${cmdpath}" --help |
    head -n 1 |
    sed -r 's/.* -- //'
  )"
  LD_LIBRARY_PATH='%{_vpath_builddir}/lib' help2man \
      --no-info \
      --version-string='%{version}' \
      --name="${summary}" \
      --output="%{_vpath_builddir}/man/man1/${cmd}.1" \
      "${cmdpath}"
done
%install
%cmake_install
mkdir %{buildroot}%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}
mv %{buildroot}%{_libdir}/osl.imageio.so %{buildroot}%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/
ln -s %{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/osl.imageio.so \
    %{buildroot}%{_libdir}/osl.imageio.so
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    %{_vpath_builddir}/man/man1/*.1
rm -fr %{buildroot}%{_prefix}/build-scripts
rm -fr %{buildroot}%{_prefix}/cmake/llvm_macros.cmake
%oreon_autofiles OpenImageIO-plugin-osl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openshadinglanguage-example-shaders-source -f %{oreon_filedir}/openshadinglanguage-example-shaders-source.list
%files -n openshadinglanguage-common-headers -f %{oreon_filedir}/openshadinglanguage-common-headers.list
%files -n OpenImageIO-plugin-osl -f %{oreon_filedir}/OpenImageIO-plugin-osl.list
%files -n openshadinglanguage-libs -f %{oreon_filedir}/openshadinglanguage-libs.list
%files -n openshadinglanguage-devel -f %{oreon_filedir}/openshadinglanguage-devel.list
%files -n python3-openshadinglanguage -f %{oreon_filedir}/python3-openshadinglanguage.list

%changelog

%autochangelog
