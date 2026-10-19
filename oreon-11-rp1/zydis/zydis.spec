%global source0_hash daa10b9148817ab57967b6e2e84462a0c905f33c013137b306777719517912be
Name:           zydis
Version:        5.0.0
%global forgeurl https://github.com/zyantific/zydis
%global commit 5091440c2a1f963e00c6e6aceec7c4346e656fa4
%forgemeta
Release:        1%{?dist}
Summary:        Fast and lightweight x86/x86-64 disassembler and code generation library
License:        MIT
URL:            %forgeurl
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
ExcludeArch:    s390x
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(zycore)
BuildRequires:  python3
BuildRequires:  rubygem-ronn-ng
# /oreon:deps
%description
Zydis is fast and lightweight x86/x86-64 disassembler and code generation
library.

- Supports all x86 and x86-64 (AMD64) instructions and extensions
- Optimized for high performance
- No dynamic memory allocation ("malloc")
- Thread-safe by design
- Very small file-size overhead compared to other common disassembler libraries
- Complete doxygen documentation
- Absolutely no third party dependencies — not even libc
  - Should compile on any platform with a working C11 compiler
  - Tested on Windows, macOS, FreeBSD, Linux and UEFI, both user and kernel mode

%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
The %{name}-tools package contains tools about %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%meson \
    -Dtools=enabled \
    -Dman=enabled \
    -Ddoc=enabled \
    -Dtests=enabled \
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifnarch %{ix86}
%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n zydis-devel -f %{oreon_filedir}/zydis-devel.list
%files -n zydis-doc -f %{oreon_filedir}/zydis-doc.list
%files -n zydis-tools -f %{oreon_filedir}/zydis-tools.list

%changelog

%autochangelog
