%global source0_hash 55a7517cd3572bd2565df0cf450944a04d5273b279ebb369a895391957f0f960

Name:           libspectre
Version:        0.2.12
Release:        11%{?dist}
Summary:        A library for rendering PostScript(TM) documents

License:        GPL-2.0-or-later
URL:            http://libspectre.freedesktop.org
Source0:        http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%if 0%{?fedora} > 27 || 0%{?oreon}
BuildRequires: libgs-devel
%else
BuildRequires: ghostscript-devel >= 8.61
%endif

%description
%{name} is a small library for rendering PostScript(TM) documents.
It provides a convenient easy to use API for handling and rendering
PostScript documents.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%configure \
  --disable-silent-rules \
  --disable-static

%make_build


%install
%make_install

rm -fv %{buildroot}%{_libdir}/libspectre.la


%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README TODO
%{_libdir}/libspectre.so.1*

%files devel
%{_includedir}/libspectre/
%{_libdir}/libspectre.so
%{_libdir}/pkgconfig/libspectre.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.12-11
- Import
