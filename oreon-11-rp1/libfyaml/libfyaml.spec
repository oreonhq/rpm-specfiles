%global source0_hash 2d016379a69f6cf6beaf06d12bcefe1ad1784bab28fbb41a6fa8d49d25f1bc0a

Name:           libfyaml
Version:        0.9.6
Release:        1%{?dist}
Summary:        Complete YAML parser and emitter
License:        MIT and GPL-2.0-only and BSD-2-Clause
URL:            https://github.com/pantoniou/libfyaml
Source0:        https://github.com/pantoniou/libfyaml/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        LICENSE-GPL-2.0
Source2:        LICENSE-BSD-2-Clause

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: check
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: libyaml-devel
BuildRequires: make
BuildRequires: python3-sphinx
BuildRequires: sed
Provides: bundled(libxxhash)

%description
A fancy 1.2 YAML and JSON parser/writer.

%package -n fyaml-utils
Summary:  Utility tools for libfyaml
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n fyaml-utils
Utility tools for libfyaml

%package devel
Summary:  Complete YAML parser and emitter
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for libfyaml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup

%build
cp %{SOURCE1} .
cp %{SOURCE2} .
autoreconf -fi
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install

%check
make check

%files
%license LICENSE
%license LICENSE-GPL-2.0
%license LICENSE-BSD-2-Clause
%doc README.md AUTHORS
%{_libdir}/libfyaml.so.0
%{_libdir}/libfyaml.so.0.0.0

%{_mandir}/man3/libfyaml-core.3.gz
%{_mandir}/man3/libfyaml-misc.3.gz
%{_mandir}/man3/libfyaml.3.gz
%files -n fyaml-utils
%{_bindir}/fy-compose
%{_bindir}/fy-dump
%{_bindir}/fy-filter
%{_bindir}/fy-join
%{_bindir}/fy-testsuite
%{_bindir}/fy-tool
%{_bindir}/fy-ypath
%{_mandir}/man1/fy-compose.1.gz
%{_mandir}/man1/fy-dump.1.gz
%{_mandir}/man1/fy-filter.1.gz
%{_mandir}/man1/fy-join.1.gz
%{_mandir}/man1/fy-testsuite.1.gz
%{_mandir}/man1/fy-tool.1.gz
%{_mandir}/man1/fy-ypath.1.gz

%files devel
%{_includedir}/libfyaml.h
%{_libdir}/libfyaml.so
%{_libdir}/pkgconfig/libfyaml.pc

%changelog
%autochangelog
%{_includedir}/libfyaml/libfyaml-align.h
%{_includedir}/libfyaml/libfyaml-allocator.h
%{_includedir}/libfyaml/libfyaml-atomics.h
%{_includedir}/libfyaml/libfyaml-blake3.h
%{_includedir}/libfyaml/libfyaml-composer.h
%{_includedir}/libfyaml/libfyaml-core.h
%{_includedir}/libfyaml/libfyaml-docbuild.h
%{_includedir}/libfyaml/libfyaml-dociter.h
%{_includedir}/libfyaml/libfyaml-endian.h
%{_includedir}/libfyaml/libfyaml-path-exec.h
%{_includedir}/libfyaml/libfyaml-thread.h
%{_includedir}/libfyaml/libfyaml-util.h
%{_includedir}/libfyaml/libfyaml-vlsize.h
