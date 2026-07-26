%global source0_hash 05f889aa28f9e5f09a1bd68026b2319d0fdc49302ec2df1b1aab9dda0e1d5fa2

Summary:       Library for performing syntax highlighting in Qt documents
Name:          source-highlight-qt
Version:       0.2.3
Release:       49%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only
URL:           http://srchiliteqt.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/srchiliteqt/source-highlight-qt/source-highlight-qt-%{version}.tar.gz
BuildRequires: make
BuildRequires: boost-devel
BuildRequires: source-highlight-devel
BuildRequires: qt-devel

%description
Source-highlight-qt is a library for performing syntax highlighting in
Qt documents by relying on GNU Source-Highlight library.

Although the use of GNU Source-highlight library is pretty hidden by
this library, so the programmer must not need the details of GNU
Source-highlight library, yet, some general notions of GNU
Source-highlight might be useful.

%package       devel
Summary:       Header files, libraries and development documentation for %{name}
Requires:      %{name} = %{version}-%{release}
Requires:      source-highlight-devel
Requires:      qt-devel
Requires:      boost-devel

%description   devel
This package contains the header files, static libraries and
development documentation for source-highlight-qt. If you like to
develop programs using source-highlight-qt, you will need to install
source-highlight-qt-devel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --with-qt=%{_libdir}/qt4/bin
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name \*.a -delete
find %{buildroot} -name \*.la -delete
mv %{buildroot}/usr/share/doc/source-highlight-qt/examples __examples
mv %{buildroot}/usr/share/doc/source-highlight-qt/source-highlight-qt.html .
rm -rf %{buildroot}/usr/share/{doc,info}

%check
pushd lib/tests
make check

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog NEWS THANKS TODO.txt
%{_libdir}/libsource-highlight-qt4.so.3*

%files devel
%doc __examples/* source-highlight-qt.html
%{_includedir}/srchiliteqt
%{_libdir}/libsource-highlight-qt4.so
%{_libdir}/pkgconfig/source-highlight-qt4.pc

%changelog
%autochangelog
