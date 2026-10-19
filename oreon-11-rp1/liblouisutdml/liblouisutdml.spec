%global source0_hash e951f5e58db0bd65f08d0a289da2ec93ed8f4b84f1f3cabcfbebc80d52e33e3c
Name:           liblouisutdml
Version:        2.12.0
Release:        8%{?dist}
Summary:        Braille transcription library for UTDML documents
License:        LGPL-3.0-or-later
URL:            https://liblouis.io
Source0:        https://github.com/liblouis/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         liblouisutdml-failing-testsuite.patch
Patch1:         liblouisutdml-includes.patch
Patch2:         liblouisutdml-gcc15.patch
Patch3:         liblouisutdml-wiskunde.patch
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  liblouis-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  texinfo-tex
# /oreon:deps
%description
This is a library intended to provide complete braille transcription services
for UTDML (Unified Tactile Document Markup Language) documents. It translates 
into appropriate braille codes and formats according to its style sheet and 
the specifications in the document.

liblouisutdml is the successor of liblouisxml.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{name} is a braille transcription library for UTDML (Unified Tactile
Document Markup Language) documents. The %{name}-devel package contains
libraries and header files for developing applications that use %{name}.

%package utils
Summary: Utilities that convert various file formats into braille
License: GPL-3.0-or-later
Requires: antiword
Requires: poppler-utils
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
This package provides the command-line utility file2brl that translates XML
or text files into embosser-ready braille files.

%package doc
Summary: Documentation of the library and the corresponding utilities
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description doc
%{name} is a braille transcription library for UTDML (Unified Tactile
Document Markup Language) documents. This package contains the user and
developer documentation of the library and the command-line utilities
provided by %{name}-utils.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure --disable-static --disable-java-bindings
make %{?_smp_mflags}
make -C doc liblouisutdml.pdf
%check

make check
%install
%make_install
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/liblouisutdml.la
rm -rf %{buildroot}/%{_defaultdocdir}/liblouisutdml
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n liblouisutdml-devel -f %{oreon_filedir}/liblouisutdml-devel.list
%files -n liblouisutdml-utils -f %{oreon_filedir}/liblouisutdml-utils.list
%files -n liblouisutdml-doc -f %{oreon_filedir}/liblouisutdml-doc.list

%changelog

%autochangelog
