Name:           libspectre
Version:        0.2.12
Release:        11%{?dist}
Summary:        A library for rendering PostScript(TM) documents

License:        GPL-2.0-or-later
URL:            http://libspectre.freedesktop.org
Source0:        http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 55a7517cd3572bd2565df0cf450944a04d5273b279ebb369a895391957f0f960
%global source0_file libspectre-0.2.12.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libspectre-0.2.12.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "55a7517cd3572bd2565df0cf450944a04d5273b279ebb369a895391957f0f960" || { echo "oreon: Source0 SHA256 mismatch for libspectre-0.2.12.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
