%global source0_hash 8a851ee54cac2ea87e1b22745d98ea06b062884c948f35fede238f2520bc26d0
Name:           libocxl
Version:        1.2.1
Release:        13%{?dist}
Summary:        Allows to implement a user-space driver for an OpenCAPI accelerator
License:        Apache-2.0
URL:            https://github.com/OpenCAPI/libocxl
Source0:        https://github.com/OpenCAPI/libocxl/archive/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  ppc64le
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(English)
# /oreon:deps
%description
Access library which allows to implement a user-space
driver for an OpenCAPI accelerator.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-docs
%package        docs
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description    devel
The *-devel package contains header file and man pages for
developing applications that use %{name}.

%description    docs
The *-docs package contains doxygen pages for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%undefine _auto_set_build_flags
make testobj/unittests V=1
%files -f %{oreon_filedir}/main.list
%files -n libocxl-devel -f %{oreon_filedir}/libocxl-devel.list
%files -n libocxl-docs -f %{oreon_filedir}/libocxl-docs.list

%changelog

%autochangelog
