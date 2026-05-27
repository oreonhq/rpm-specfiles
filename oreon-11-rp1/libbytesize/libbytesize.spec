%global source0_hash 8356bac2cafd2f31f39bf1ad373cef8448cab08b817aeaee5c526d54e81c3c5a

%define realname bytesize
%define with_python3 1
%define with_gtk_doc 1
%define with_tools 1

%if (! 0%{?fedora} && 0%{?rhel} <= 7) || %{with_python3} == 0
%define with_python3 0
%define python3_opts --without-python3
%define with_tools 0
%endif

%if %{with_tools} != 1
%define tools_opts --without-tools
%endif

%define configure_opts %{?python3_opts} %{?tools_opts}

Name:        libbytesize
Version:     2.12
Release:     2%{?dist}
Summary:     A library for working with sizes in bytes
License:     LGPL-2.1-or-later
URL:         https://github.com/storaged-project/libbytesize
Source0:     https://github.com/storaged-project/libbytesize/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: gmp-devel
BuildRequires: mpfr-devel
BuildRequires: pcre2-devel
BuildRequires: gettext-devel
%if %{with_python3}
BuildRequires: python3-devel
%endif
%if %{with_gtk_doc}
BuildRequires: gtk-doc
%endif

%description
The libbytesize is a C library that facilitates work with sizes in
bytes. Be it parsing the input from users or producing a nice human readable
representation of a size in bytes this library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package devel
Summary:  Development files for libbytesize
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files and pkg-config files needed for development
with the libbytesize library.

%if %{with_python3}
%package -n python3-%{realname}
Summary: Python 3 bindings for libbytesize
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{realname}
This package contains Python 3 bindings for libbytesize making the use of
the library from Python 3 easier and more convenient.
%endif

%if %{with_tools}
%package tools
Summary: Various nice tools based on libbytesize
Requires: python3-%{realname} = %{version}-%{release}

%description tools
Various nice tools based on libbytesize, in particular the calculator
for doing calculations with storage sizes.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}

%build
%configure %{?configure_opts}
%make_build

%install
%{make_install}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}
%find_lang %{name}


%ldconfig_scriptlets


%files -f %{name}.lang
%doc README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libbytesize.so.*

%files devel
%{_libdir}/libbytesize.so
%dir %{_includedir}/bytesize
%{_includedir}/bytesize/bs_size.h
%{_libdir}/pkgconfig/bytesize.pc
%if %{with_gtk_doc}
%{_datadir}/gtk-doc/html/libbytesize
%endif

%if %{with_python3}
%files -n python3-%{realname}
%dir %{python3_sitearch}/bytesize
%{python3_sitearch}/bytesize/*
%endif

%if %{with_tools}
%files tools
%{_bindir}/bscalc
%{_mandir}/man1/bscalc.1*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12-2
- Prepare for Oreon 11 (RP1)
