%global source0_hash none

Name:           subversion-api-docs
Version:        1.14.5
Release:        3%{?dist}
Summary:        Subversion API documentation

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://subversion.tigris.org/
Source0:        http://svn.collab.net/repos/svn/tags/%{version}/doc/doxygen.conf
Source1:        http://svn.collab.net/repos/svn/tags/%{version}/COPYING
BuildRequires:  subversion-devel = %{version}, doxygen
BuildArch:      noarch

%description
Subversion is a concurrent version control system which enables one or more
users to collaborate in developing and maintaining a hierarchy of files and
directories while keeping a history of all changes. This package provides
Subversion API documentation for developers.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
cd %{name}-%{version}
cp %{SOURCE0} doxygen.conf

%build
cd %{name}-%{version}
sed -e 'N;N;s,^\(INPUT *= *\).*$,\1%{_includedir}/subversion-1\n,' \
doxygen.conf | 
sed -e 's,^\(OUTPUT_DIRECTORY *= *\).*$,\1docs,' \
    -e 's,^\(GENERATE_TAGFILE *= *\).*$,\1docs/svn.tag,' | \
doxygen -

%install
cd %{name}-%{version}
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs/search
install -m 644 docs/svn.tag $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs
install -m 644 docs/html/search/* $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs/search
install -m 644 `find docs/html -type f -maxdepth 1` $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs

%files
%doc %dir %{_docdir}/subversion
%doc %dir %{_docdir}/subversion/api-docs
%doc %{_docdir}/subversion/api-docs/*

%changelog
%autochangelog
