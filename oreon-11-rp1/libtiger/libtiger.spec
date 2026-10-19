%global source0_hash 7342b255fb476d75b08dd4c56d5ce580f39b1c71c42e99fb7af9d999725d4166
Name:           libtiger
Version:        0.3.4
Release:        1%{?dist}
Summary:        Rendering library for Kate streams using Pango and Cairo
License:        LGPL-2.1-or-later
URL:            https://code.google.com/archive/p/libtiger
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/libtiger/libtiger-%{version}.tar.gz
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libkate-devel
BuildRequires:  make
BuildRequires:  pango-devel
# /oreon:deps
%description
Libtiger is a rendering library for Kate streams using Pango and Cairo.
More information about Kate streams may be found at 
http://wiki.xiph.org/index.php/OggKate

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pango-devel
Requires:       libkate-devel >= 0.2.7
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
%make_build
%install
rm -rf __doc
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
touch -r include/tiger/tiger.h.in %{buildroot}%{_includedir}/tiger/tiger.h
mv %{buildroot}%{_docdir}/%{name} __doc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libtiger-devel -f %{oreon_filedir}/libtiger-devel.list
%files -n libtiger-doc -f %{oreon_filedir}/libtiger-doc.list

%changelog

%autochangelog

