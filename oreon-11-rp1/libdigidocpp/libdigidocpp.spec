%global source0_hash 773a6ad8f3eed3a3859a58c9bcd808c27c20b374850c7f14644707c3340a5038
Name:           libdigidocpp
Version:        4.3.0
Release:        2%{?dist}
Summary:        Library offers creating, signing and verification of digitally signed documents
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/open-eid/libdigidocpp
Source0:        https://github.com/open-eid/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       opensc%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xmlsec1-openssl)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Libdigidocpp library offers creating, signing and verification of digitally
signed documents, according to XAdES and XML-DSIG standards. Documentation
http://open-eid.github.io/libdigidocpp

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    doc
The %{name}-doc package contains documentation provided by upstream.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# it contains non UTF-8 files, but they do not worth the process of
# unpackaging and fixing the encoding
rm -rf doc/sample_files.zip

# Remove bundled minizip
rm -rf src/minizip

%build

%if 0%{?el7}
%{cmake3} .\
 -DCMAKE_INSTALL_SYSCONFDIR=/etc \
 -DSWIG_EXECUTABLE=SWIG_EXECUTABLE-NOTFOUND
%else
%{cmake} \
 -DCMAKE_INSTALL_SYSCONFDIR=/etc \
 -DSWIG_EXECUTABLE=SWIG_EXECUTABLE-NOTFOUND
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*
%if 0%{?el7}
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%endif
%files -f %{oreon_filedir}/main.list
%files -n libdigidocpp-devel -f %{oreon_filedir}/libdigidocpp-devel.list
%files -n libdigidocpp-doc -f %{oreon_filedir}/libdigidocpp-doc.list

%changelog

%autochangelog
