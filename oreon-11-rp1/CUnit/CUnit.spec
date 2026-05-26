# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 f5b29137f845bb08b77ec60584fdb728b4e58f1023e6f249a464efa49a40f214
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global tarver 2.1-3

Name:           CUnit
Version:        2.1.3
Release:        37%{?dist}
Summary:        Unit testing framework for C

License:        LGPL-2.0-or-later
URL:            http://cunit.sourceforge.net/
Provides:       cunit = %{version}-%{release}
Source0:        http://downloads.sourceforge.net/cunit/%{name}-%{tarver}.tar.bz2

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make

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
%oreon_verify_sources
%setup -q -n %{name}-%{tarver}
find -name *.c -exec chmod -x {} \;

%build
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f `find %{buildroot} -name *.la`

# work around bad docdir= in doc/Makefile*
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_prefix}/doc/%{name} %{buildroot}%{_docdir}/%{name}/html

# add some doc files into the buildroot manually (#1001276)
for f in AUTHORS ChangeLog COPYING NEWS README TODO VERSION ; do
    install -p -m0644 -D $f %{buildroot}%{_docdir}/%{name}/${f}
done

%ldconfig_scriptlets

%files
%{_datadir}/%{name}/
%{_libdir}/libcunit.so.*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README
%{_docdir}/%{name}/TODO
%{_docdir}/%{name}/VERSION

%files devel
%{_docdir}/%{name}/html/
%{_includedir}/%{name}/
%{_libdir}/libcunit.so
%{_libdir}/pkgconfig/cunit.pc
%{_mandir}/man3/CUnit.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.3-37
- Prepare for Oreon 11 (RP1)
