%global source0_hash 98f0a3ea26b4aec051e533cb1750db2998ab8e82eda97269ed6efe66ec94a240
%global source1_hash c1031afde6e9eb042e6fcfbc17078f4b437a7e8d55482a1ca6e0fa762d262a89

%global cl_ver 2025.07.22
%global cl_hpp_ver 2025.07.22

Name:           opencl-headers
Version:        3.0
Release:        2%{?dist}
Summary:        OpenCL (Open Computing Language) header files

License:        Apache-2.0
URL:            https://www.khronos.org/registry/cl/

Source0:        https://github.com/KhronosGroup/OpenCL-Headers/archive/refs/tags/v%{cl_ver}.tar.gz#/OpenCL-Headers-v%{cl_ver}.tar.gz
Source1:        https://github.com/KhronosGroup/OpenCL-CLHPP/archive/refs/tags/v%{cl_hpp_ver}.tar.gz#/OpenCL-CLHPP-v%{cl_hpp_ver}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n OpenCL-Headers-%{cl_ver}

tar -xf %{SOURCE1}
cp -p OpenCL-CLHPP-%{cl_hpp_ver}/include/CL/{cl2,opencl}.hpp .

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_includedir}/CL/
install -p -m 0644 *hpp CL/* -t %{buildroot}%{_includedir}/CL/
# We're not interested in Direct3D things
rm -vf %{buildroot}%{_includedir}/CL/cl_{dx9,d3d}*
# Install pkgconfig files
mkdir -p %{buildroot}%{_datadir}/pkgconfig
sed -e 's|@CMAKE_INSTALL_PREFIX@|%{_prefix}|' -e 's|@OPENCL_INCLUDEDIR_PC@|%{_includedir}|' OpenCL-Headers.pc.in > %{buildroot}%{_datadir}/pkgconfig/OpenCL-Headers.pc
sed -e 's|@CMAKE_INSTALL_PREFIX@|%{_prefix}|' -e 's|@OPENCLHPP_INCLUDEDIR_PC@|%{_includedir}|' OpenCL-CLHPP-%{cl_hpp_ver}/OpenCL-CLHPP.pc.in > %{buildroot}%{_datadir}/pkgconfig/OpenCL-CLHPP.pc

%files
%dir %{_includedir}/CL
%{_includedir}/CL/cl2.hpp
%{_includedir}/CL/cl_egl.h
%{_includedir}/CL/cl_ext.h
%{_includedir}/CL/cl_ext_intel.h
%{_includedir}/CL/cl_function_types.h
%{_includedir}/CL/cl_gl_ext.h
%{_includedir}/CL/cl_gl.h
%{_includedir}/CL/cl.h
%{_includedir}/CL/cl_half.h
%{_includedir}/CL/cl_icd.h
%{_includedir}/CL/cl_layer.h
%{_includedir}/CL/cl_platform.h
%{_includedir}/CL/cl_va_api_media_sharing_intel.h
%{_includedir}/CL/cl_version.h
%{_includedir}/CL/opencl.h
%{_includedir}/CL/opencl.hpp
%{_datadir}/pkgconfig/OpenCL-Headers.pc
%{_datadir}/pkgconfig/OpenCL-CLHPP.pc

%changelog
%autochangelog
