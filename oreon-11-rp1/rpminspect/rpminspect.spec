%global source1_hash aa3cebced2177147f558fa38b9c73a99a883127a429eed32507bc6e5f5359228
%global source0_hash 9b9cec725aac9ec21f54725c11a5a642066e725ee991699014a4a51bdfc6caa2
Name:           rpminspect
Version:        2.1
Release:        1%{?dist}
Summary:        Build deviation analysis and compliance tool
Group:          Development/Tools
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND Apache-2.0 AND MIT AND BSD-1-Clause AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-4.0
URL:            https://github.com/rpminspect/rpminspect
Source0:        https://github.com/rpminspect/rpminspect/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/rpminspect/rpminspect/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-62977BB9C841B965.gpg
Requires:       librpminspect%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  clamav-devel
BuildRequires:  elfutils-devel
BuildRequires:  file-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  gnupg2
BuildRequires:  json-c-devel
BuildRequires:  kmod-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcap-devel
BuildRequires:  libcdson-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libmandoc-devel
BuildRequires:  libxml2-devel
BuildRequires:  libyaml-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  rpm-devel
BuildRequires:  xmlrpc-c-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Build deviation and compliance tool.  This program runs a number of tests
against one or two builds of source RPM files.  The built artifacts are
inspected and compared to report changes and validate policy compliance
against the defined parameters.

%package -n librpminspect
Summary:        Library providing RPM test API and functionality
Group:          Development/Tools
Requires:       desktop-file-utils
Requires:       gettext
Requires:       annobin-annocheck
Requires:       clamav-data
Requires:       system-rpm-config
Requires:       dash
Requires:       ksh
Requires:       zsh
Requires:       tcsh
Requires:       rc
Requires:       bash
Requires:       libabigail >= 2.3
Requires:       systemd-udev
%description -n librpminspect
The library providing the backend test functionality and API for the
rpminspect frontend program.  This library can also be used by other
programs wanting to incorporate RPM test functionality.

%package -n librpminspect-devel
Summary:        Header files and development libraries for librpminspect
Group:          Development/Tools
Requires:       librpminspect%{?_isa} = %{version}-%{release}
%description -n librpminspect-devel
The header files and development library links required to build software
using librpminspect.

%package -n rpminspect-data-generic
Summary:        Template data files used to drive rpminspect tests
Group:          Development/Tools
%description -n rpminspect-data-generic
The rpminspect-data-generic package is meant as a template to build your
product's own data file.  The files in it contain product-specific
information.  The files in this package explain how to construct the
control files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson -D tests=false %{?fedora:-D with_system_libtoml=true}
%meson_build
%install
install -D -m 0644 libxdiff/AUTHORS %{buildroot}%{_pkgdocdir}/libxdiff/AUTHORS
install -D -m 0644 libxdiff/README %{buildroot}%{_pkgdocdir}/libxdiff/README
install -D -m 0644 libxdiff/COPYING %{buildroot}%{_defaultlicensedir}/%{name}/libxdiff/COPYING
install -D -m 0644 libtoml/README.md %{buildroot}%{_pkgdocdir}/libtoml/README.md
install -D -m 0644 libtoml/README.rpminspect %{buildroot}%{_pkgdocdir}/libtoml/README.rpminspect
install -D -m 0644 libtoml/LICENSE %{buildroot}%{_defaultlicensedir}/%{name}/libtoml/LICENSE
%meson_install
%find_lang %{name}
%oreon_autofiles librpminspect usr/*/lib*.so.*
%oreon_autofiles librpminspect-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles rpminspect-data-generic usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n librpminspect -f %{oreon_filedir}/librpminspect.list
%files -n librpminspect-devel -f %{oreon_filedir}/librpminspect-devel.list
%files -n rpminspect-data-generic -f %{oreon_filedir}/rpminspect-data-generic.list

%changelog

%autochangelog
