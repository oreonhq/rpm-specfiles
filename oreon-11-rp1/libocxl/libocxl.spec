%global source0_hash 8a851ee54cac2ea87e1b22745d98ea06b062884c948f35fede238f2520bc26d0

Name:           libocxl
Version:        1.2.1
Release:        13%{?dist}
Summary:        Allows to implement a user-space driver for an OpenCAPI accelerator

License:        Apache-2.0
URL:            https://github.com/OpenCAPI/libocxl
Source0:        https://github.com/OpenCAPI/libocxl/archive/%{version}/%{name}-%{version}.tar.gz#/libocxl-1.2.1.tar.gz

ExclusiveArch:  ppc64le

BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  perl(English)
# for tests
BuildRequires:  fuse-devel

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print \$1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
%undefine _auto_set_build_flags
make testobj/unittests V=1


%files
%license COPYING
%doc README.md
%{_libdir}/libocxl.so.*

%files devel
%{_includedir}/*
%{_libdir}/libocxl.so
%{_mandir}/man3/*

%files docs
%{_pkgdocdir}


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-13
- Import
