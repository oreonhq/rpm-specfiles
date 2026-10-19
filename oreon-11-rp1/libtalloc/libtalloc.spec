%global source1_hash c4c2b6f9f39a62146c5c52e52ce8843086bc6373c7e8a1b2ce0f80bcbe734913
%global source0_hash 912afa237510ae542a7733998eb18a12bcda35ab6729c8e2ddb43e8d0ebab007
%global source2_key_fpr 9147A339719518EE9011BCB54793916113084025
Name:            libtalloc
Version:         2.5.0
Release:        1%{?dist}
Summary:        The talloc library
License:         LGPL-3.0-or-later
URL:             https://talloc.samba.org/
Source0:        https://www.samba.org/ftp/talloc/talloc-%{version}.tar.gz
Source1:        https://www.samba.org/ftp/talloc/talloc-%{version}.tar.asc
Source2:        talloc.keyring
Provides: bundled(libreplace)
Obsoletes: python2-talloc < 2.2.0-1
Obsoletes: python2-talloc-devel < 2.2.0-1
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
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

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%autosetup -n talloc-%{version} -p1

%build

zcat %{SOURCE0} | gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} -
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
cp -a doc/man/man3 %{buildroot}%{_mandir}
%oreon_autofiles python3-talloc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-talloc-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtalloc-devel -f %{oreon_filedir}/libtalloc-devel.list
%files -n python3-talloc -f %{oreon_filedir}/python3-talloc.list
%files -n python3-talloc-devel -f %{oreon_filedir}/python3-talloc-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.4-1
- Prepare for Oreon 11 (RP1)
