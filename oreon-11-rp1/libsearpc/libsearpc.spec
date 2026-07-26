%global source0_hash 912ded178bb3030594e48832c3c19c31c1447d38bb77efdfbb70005320da36ed

%global _hardened_build 1
# checkout by commit for a valid persistent source link
# the corresponding git tag is v3.3-latest
%global commit      7f275255f089c72f3b3fb8128212fb58aad44b05
%global date        20241024
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libsearpc
Version:        3.3
Release:        12%{?dist}
Summary:        A simple and easy-to-use C language RPC framework

# Main package license: Apache-2.0
# debian/*: GPL-2.0-only (as stated in debian/copyright)
# tests/clar*, tests/generate.py, tests/main.c: ISC
License:        Apache-2.0
URL:            https://github.com/haiwen/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{version}%{?date:-%{date}git%{shortcommit}}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  python3-devel

%description
Searpc is a simple C language RPC framework based on GObject system. Searpc
handles the serialization/deserialization part of RPC, the transport part is
left to users.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}
%py3_shebang_fix ./lib/searpc-codegen.py ./pysearpc/test_pysearpc.py \
    ./tests/generate.py ./pysearpc/pygencode.py

%build
./autogen.sh
%configure --disable-static --disable-compile-demo --with-python3
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
# tests are failing on big endian arches
# https://bugzilla.redhat.com/show_bug.cgi?id=1388453
%ifnarch ppc ppc64 s390 s390x
%make_build check
%endif

%ldconfig_scriptlets

%files
%doc AUTHORS README.markdown
%license LICENSE.txt
%{_libdir}/%{name}.so.1*
%{_bindir}/searpc-codegen.py
%{python3_sitearch}/pysearpc/

%files devel
%license LICENSE.txt
%{_includedir}/searpc*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
