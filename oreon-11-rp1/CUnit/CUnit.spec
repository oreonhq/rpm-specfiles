%global source0_hash f5b29137f845bb08b77ec60584fdb728b4e58f1023e6f249a464efa49a40f214
%global tarver 2.1-3
Name:           CUnit
Version:        2.1.3
Release:        37%{?dist}
Summary:        Unit testing framework for C
License:        LGPL-2.0-or-later
URL:            http://cunit.sourceforge.net/
Provides:       cunit = %{version}-%{release}
Source0:        https://downloads.sourceforge.net/cunit/%{name}-2.1-3.tar.bz2
# oreon:deps
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description 
CUnit is a lightweight system for writing, administering,
and running unit tests in C.  It provides C programmers a basic
testing functionality with a flexible variety of user interfaces.

%package devel
Summary:        Header files and libraries for CUnit development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       cunit-devel = %{version}-%{release}
%description devel 
The %{name}-devel package contains the header files
and libraries for use with CUnit package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{tarver}
find -name *.c -exec chmod -x {} \;

%build

autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f `find %{buildroot} -name *.la`
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_prefix}/doc/%{name} %{buildroot}%{_docdir}/%{name}/html
for f in AUTHORS ChangeLog COPYING NEWS README TODO VERSION ; do
    install -p -m0644 -D $f %{buildroot}%{_docdir}/%{name}/${f}
done
%ldconfig_scriptlets
%oreon_autofiles CUnit-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n CUnit-devel -f %{oreon_filedir}/CUnit-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.3-37
- Prepare for Oreon 11 (RP1)
