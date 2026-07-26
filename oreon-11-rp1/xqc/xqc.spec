%global source0_hash b5507b214af9b38e70bec8b37d0485ba32541b76ae890210bd8c715aff9ad881

%global snapshot 20101120svn7

Name:           xqc
Version:        1.0
Release:        0.30.%{snapshot}%{?dist}
Summary:        C/C++ API for interfacing with XQuery processors

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://xqc.sourceforge.net

# snapshot archive created from upstream revision 7 with:
# svn export https://xqc.svn.sourceforge.net/svnroot/xqc/trunk/xqc xqc 
# tar czf xqc.tar.gz xqc
Source0:        xqc.tar.gz
Source1:        http://downloads.sourceforge.net/%{name}/intro.pdf
BuildArch:      noarch

BuildRequires: make
BuildRequires:  doxygen

%description
The goal of the XQC project is to create standardized C/C++ APIs for 
interfacing with XQuery processors. They should provide mechanisms to compile 
and execute XQueries, manage contexts, and provide a basic interface for 
the XQuery Data Model.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
cp %{SOURCE1} .

%build
%configure
make %{?_smp_mflags}
cd docs
doxygen Doxyfile.xqc

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%doc LICENSE.txt intro.pdf examples/ docs/xqc/
%{_includedir}/xqc.h
%exclude %{_includedir}/xqc++.hpp

%changelog
%autochangelog
