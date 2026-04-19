Summary:  Thai language support routines
Name: libthai
Version: 0.1.30
Release: 2%{?dist}
License: LGPL-2.1-or-later
Source: http://linux.thai.net/pub/thailinux/software/libthai/libthai-%{version}.tar.xz
Patch0: libthai-0.1.9-multilib.patch
URL: http://linux.thai.net

BuildRequires: gcc
BuildRequires: pkgconfig(datrie-0.2)
BuildRequires: doxygen
BuildRequires: make

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package devel
Summary:  Thai language support routines
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The libthai-devel package includes the header files and developer docs 
for the libthai package.

Install libthai-devel if you want to develop programs which will use
libthai.

%prep
%autosetup -p1

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# move installed doc files back to build directory to package them
# in the right place
if [ -d $RPM_BUILD_ROOT%{_docdir}/libthai ]; then
  mkdir installed-docs
  mv $RPM_BUILD_ROOT%{_docdir}/libthai/* installed-docs
  rmdir $RPM_BUILD_ROOT%{_docdir}/libthai
else
  mkdir -p installed-docs
  touch installed-docs/README.docs
fi

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/lib*.so.*
%{_datadir}/libthai

%files devel
%doc installed-docs/*
%{_includedir}/thai
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.30-3
- Fix build failure when doc directory is missing

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.30-2
- Prepare for Oreon 11 (RP1)
