%global source0_hash c5d24d8c096546353fbc7cedf208392d5a02afe9d56ebcc1cccb258d7c4d2220
%bcond autoreconf 1
Name:           libIDL
Summary:        Library for parsing IDL (Interface Definition Language)
Version:        0.8.14
%global so_version 0
Release:        1%{?dist}
%global doc_license GPL-3.0-or-later
License:        LGPL-2.0-or-later
SourceLicense:  %{shrink:
                %{license} AND %{doc_license} AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later WITH Autoconf-exception-generic
                GPL-2.0-or-later WITH Libtool-exception
                }
%global minorversion %(echo '%{version}' | cut -d . -f 1-2)
URL:            https://download.gnome.org/sources/libIDL/%{minorversion}/
Source0:        https://download.gnome.org/sources/libIDL/0.8//libIDL-0.8.14.tar.bz2
Source1:        libIDL-config-2.1
Patch:          libIDL-0.8.6-multilib.patch
Patch:          libIDL-0.8.14-parser-primary_expr-unused-parent-node.patch
Patch:          libIDL-0.8.14-long-long-format-warnings.patch
Patch:          libIDL-0.8.14-lexer-sscanf-type-punning.patch
Patch:          libIDL-0.8.14-old-libIDL-config-script.patch
%if %{with autoreconf}
%endif
%global common_description %{expand:
libIDL is a library for parsing IDL (Interface Definition Language). It can be
used for both COM-style and CORBA-style IDL.}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  tex(latex)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description %{common_description}

%package devel
Summary:        Development libraries and header files for libIDL
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel%{?_isa}
%description devel %{common_description}

This package contains the header files and libraries needed to write or compile
programs that use libIDL.

%package doc
Summary:        Documentation for libIDL
License:        %{doc_license}
BuildArch:      noarch
%description doc %{common_description}

This page contains info pages and HTML and PDF documentation for libIDL.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif

%configure --disable-static

%build

rm libIDL2.info
%make_build all libIDL2.info libIDL2.html libIDL2.pdf
%install
%make_install
rm '%{buildroot}%{_libdir}/libIDL-2.la'
rm '%{buildroot}%{_infodir}/dir'
install -t '%{buildroot}%{_pkgdocdir}' -D -p -m 0644 \
    AUTHORS BUGS ChangeLog HACKING MAINTAINERS NEWS README libIDL2.pdf
cp -rp 'libIDL2.html' '%{buildroot}%{_pkgdocdir}/html'
install -t '%{buildroot}%{_datadir}/aclocal/libIDL.m4' -D -p -m 0644 \
    libIDL.m4
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libIDL-devel -f %{oreon_filedir}/libIDL-devel.list
%files -n libIDL-doc -f %{oreon_filedir}/libIDL-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.14-1
- Prepare for Oreon 11 (RP1)
