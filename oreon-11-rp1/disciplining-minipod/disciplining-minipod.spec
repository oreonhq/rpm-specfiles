%global source0_hash d268fbd0869110f066b00eb1557e632bcdc1e61b63295c701a4aa582de7ca477
%global libname liboscillator-disciplining
Name:           disciplining-minipod
Version:        3.10.0
Release:        1%{?dist}
Summary:        Disciplining algorithm for Atomic Reference Time Card
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/Orolia2s/disciplining-minipod
Source0:        https://github.com/Orolia2s/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description

%package -n     %{libname}
Summary:        Disciplining algorithm for Atomic Reference Time Card
%description -n %{libname}

%package -n     %{libname}-devel
Summary:        Development files for %{libname}
Requires:       %{libname} = %{version}-%{release}
%description -n %{libname}-devel
This package contains development headers and files for %{libname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Drop forced optimization flag
sed -i 's/-O3//' CMakeLists.txt
# Do not install static library
sed -i 's/^install.*-static.*$//' src/CMakeLists.txt

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%set_build_flags
%if 0%{?el8}
export CC="%{__cc}"
%endif
%cmake -DBUILD_TESTS=true -DCMAKE_PREFIX_PATH="%{buildroot}%{_prefix}"
%cmake_build
for t in test-checks test-utils test-minipod-lib test-fine-circular-buffer; do
%if 0%{?el8}
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test/$t
%else
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./%{_vpath_builddir}/test/$t
%endif
done
%files -f %{oreon_filedir}/main.list
%files -n liboscillator-disciplining -f %{oreon_filedir}/liboscillator-disciplining.list
%files -n liboscillator-disciplining-devel -f %{oreon_filedir}/liboscillator-disciplining-devel.list

%changelog

%autochangelog
