%global source0_hash f369d15cefc68d06c246881e8eba3c6091e532cb9de02d7f079a6686c1801e5e
%bcond_with doc
Name:           esmi_ib_library
Version:        5.2.1.1
%global major_version %(echo %{version} | cut -d. -f1)
%global minor_version %(echo %{version} | cut -d. -f2)
%global soversion %{version}.0
%global srcversion esmi_pkg_ver-%{version}
Release:        1%{?dist}
Summary:        E-SMI: EPYC System management Interface In-band Library
License:        NCSA
URL:            https://github.com/amd/esmi_ib_library
Source0:        https://github.com/amd/%{name}/archive/%{srcversion}/%{name}-%{srcversion}.tar.gz
Patch:          %{url}/pull/21.patch#/esmi_ib_library-fix-cflags.diff
ExclusiveArch:  x86_64
%if %{with system_amd_hsmp}
%endif
%if %{with doc}
%endif
Suggests:       %{name}-doc = %{version}-%{release}
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  texlive-latex
# /oreon:deps
%description
The EPYC System Management Interface In-band Library, or E-SMI library, is
part of the EPYC System Management Inband software stack. It is a C library
for Linux that provides a user space interface to monitor and control the CPU's
power, energy, performance and other system management features.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development headers and libraries for %{name}.

%package        doc
Summary:        Additional documentation for %{name}
BuildArch:      noarch
%description    doc
This package contains additional documentation for %{name}.

%package -n     e_smi_tool
Summary:        E-SMI: EPYC™ System management Interface tool
%description -n e_smi_tool
This package contains E-SMI tool, a program based on the E-SMI In-band library
that provides options to Monitor and Control System Management functionality.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n %{name}-%{srcversion}
%autopatch -p1

# Use FHS install paths and patch version detection
sed -i CMakeLists.txt \
    -e 's:${E_SMI}/bin:%{_bindir}:g' \
    -e 's:e_smi/include:%{_includedir}:g' \
    -e 's:${E_SMI}/lib/static:%{_libdir}:g' \
    -e 's:LIBRARY DESTINATION lib COMPONENT:LIBRARY DESTINATION %{_libdir} COMPONENT:g' \
    -e 's:${E_SMI}/doc:%{_pkgdocdir}:g' \
    -e 's:get_package_version_number("1.0.0.0":get_version_from_tag("%{soversion}":'

%if %{with doc}
# Remove prebuilt docs
rm ESMI_IB_Release_Notes.pdf ESMI_Manual.pdf
%endif

%build

%cmake -DCMAKE_C_FLAGS="$CFLAGS" -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build
%if %{with doc}
make -C %{_vpath_builddir} doc
%endif
%install
%cmake_install
chrpath -d %{buildroot}/%{_bindir}/e_smi_tool
%oreon_autofiles e_smi_tool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n esmi_ib_library-devel -f %{oreon_filedir}/esmi_ib_library-devel.list
%files -n esmi_ib_library-doc -f %{oreon_filedir}/esmi_ib_library-doc.list
%files -n e_smi_tool -f %{oreon_filedir}/e_smi_tool.list

%changelog

%autochangelog
