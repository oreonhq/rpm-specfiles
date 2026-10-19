%global source0_hash e6b532c78022709dcf8ae3db9cad0d687df12ec67141f688a01a1abd82ed2810
%global tag 0.7-4
Version:        %(echo %{tag} | sed 's/-/./')
Name:           foonathan-memory
Release:        1%{?dist}
Summary:        STL compatible C++ memory allocator library
License:        Zlib
URL:            https://github.com/foonathan/memory
Source0:        https://github.com/foonathan/memory/archive/v%{tag}/%{name}-%{tag}.tar.gz
Patch0:         https://github.com/foonathan/memory/pull/201.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(doctest)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
STL compatible C++ memory allocator library using a new RawAllocator concept
that is similar to an Allocator but easier to use and write.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%package        tools
Summary:        Tools about %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
This package contains tools about %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains the documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n memory-%{tag}

%build

%cmake \
    -GNinja \
    -DFOONATHAN_MEMORY_USE_SYSTEM_DOCTEST=ON \
    -DFOONATHAN_MEMORY_BUILD_TESTS=ON
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/%{name}/
cp -r example/ %{buildroot}%{_docdir}/%{name}/
rm -rf %{buildroot}%{_datadir}/foonathan_memory/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n foonathan-memory-devel -f %{oreon_filedir}/foonathan-memory-devel.list
%files -n foonathan-memory-tools -f %{oreon_filedir}/foonathan-memory-tools.list
%files -n foonathan-memory-doc -f %{oreon_filedir}/foonathan-memory-doc.list

%changelog

%autochangelog
