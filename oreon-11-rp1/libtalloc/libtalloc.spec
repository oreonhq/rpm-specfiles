%global source0_hash none

%global source2_key_fpr 9147A339719518EE9011BCB54793916113084025

Name:            libtalloc
Version:         2.4.4
Release:         %autorelease
Summary:         The talloc library
License:         LGPL-3.0-or-later
URL:             https://talloc.samba.org/

Source0:        https://www.samba.org/ftp/talloc/talloc-2.4.4.tar.gz
Source1:        talloc-2.4.4.tar.asc
Source2:         talloc.keyring

BuildRequires: make
BuildRequires: gcc
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: python3-devel
BuildRequires: doxygen
BuildRequires: gnupg2

Provides: bundled(libreplace)
Obsoletes: python2-talloc < 2.2.0-1
Obsoletes: python2-talloc-devel < 2.2.0-1

%description
A library that implements a hierarchical allocator with destructors.

%package devel
Summary:         Developer tools for the Talloc library

Requires: libtalloc = %{version}-%{release}

%description devel
Header files needed to develop programs that link against the Talloc library.

%package -n python3-talloc
Summary:         Python bindings for the Talloc library

Requires: libtalloc = %{version}-%{release}
%{?python_provide:%python_provide python3-talloc}

%description -n python3-talloc
Python 3 libraries for creating bindings using talloc

%package -n python3-talloc-devel
Summary:         Development libraries for python3-talloc

Requires: python3-talloc = %{version}-%{release}
%{?python_provide:%python_provide python3-talloc-devel}

%description -n python3-talloc-devel
Development libraries for python3-talloc

%prep
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n talloc-%{version} -p1

%build
zcat %{SOURCE0} | gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} -

# workaround https://gitlab.com/ita1024/waf/-/issues/2472
export PYTHONARCHDIR=%{python3_sitearch}
%configure --disable-rpath \
           --disable-rpath-install \
           --bundled-libraries=NONE \
           --builtin-libraries=replace \
           --disable-silent-rules

%make_build
doxygen doxy.config

%check
%make_build check

%install
%make_install

# Install API docs
cp -a doc/man/man3 %{buildroot}%{_mandir}

%files
%license LICENSE
%{_libdir}/libtalloc.so.*

%files devel
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc
%{_mandir}/man3/talloc*.3*
%{_mandir}/man3/libtalloc*.3*

%files -n python3-talloc
%{_libdir}/libpytalloc-util.cpython*.so.*
%{python3_sitearch}/talloc.cpython*.so

%files -n python3-talloc-devel
%{_includedir}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.cpython-*.pc
%{_libdir}/libpytalloc-util.cpython*.so

%ldconfig_scriptlets
%ldconfig_scriptlets -n python3-talloc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.4-1
- Prepare for Oreon 11 (RP1)
