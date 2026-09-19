%global source0_hash none

Name:           apr-api-docs
Version:        1.7.6
Release:        3%{?dist}
Summary:        Apache Portable Runtime API documentation

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://apr.apache.org/
Source0:        http://svn.apache.org/repos/asf/apr/apr/tags/%{version}/docs/doxygen.conf
Source1:        http://svn.apache.org/repos/asf/apr/apr/tags/%{version}/LICENSE.APR
Source2:        http://svn.apache.org/repos/asf/apr/apr-util/tags/%{version}/LICENSE.APU
Patch0:         apr-api-docs-doxygen.patch
BuildRequires:  apr-devel = %{version}, apr-util-devel, doxygen
BuildArch:      noarch

%description
The mission of the Apache Portable Runtime (APR) is to provide a free library
of C data structures and routines, forming a system portability layer to as
many operating systems as possible, including Unices, MS Win32, BeOS and OS/2.
This package provides APR and APR-util API documentation for developers.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
cd %{name}-%{version}
cp %{SOURCE0} doxygen.conf
%patch -P 0 -p0 -b .doxygen-apu

%build
cd %{name}-%{version}
sed -e 's,\(INPUT *= *\).*$,\1%{_includedir}/apr-1,' \
    -e 's,\(OUTPUT_DIRECTORY *= *\).*$,\1docs,' \
    -e 's,\(GENERATE_TAGFILE *= *\).*$,\1docs/apr.tag,' \
doxygen.conf | doxygen -
sed -i -e 's,^\[<a class="el" href="group___a_p_r.html">Apache Portability Runtime library</a>\],&'\
'<br><strong><font color="red">'\
'WARNING: The actual values of macros and typedefs<br>'\
'are platform specific and should NOT be relied upon!'\
'</font></strong>,' docs/html/group__apr__platform.html

%install
cd %{name}-%{version}
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/apr/api-docs/search
install -m 644 docs/apr.tag $RPM_BUILD_ROOT%{_docdir}/apr/api-docs
install -m 644 docs/html/search/* $RPM_BUILD_ROOT%{_docdir}/apr/api-docs/search
install -m 644 `find docs/html -type f -maxdepth 1` $RPM_BUILD_ROOT%{_docdir}/apr/api-docs
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/apr/api-docs
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/apr/api-docs

%files
%doc %dir %{_docdir}/apr
%doc %dir %{_docdir}/apr/api-docs
%doc %{_docdir}/apr/api-docs/*

%changelog
%autochangelog
