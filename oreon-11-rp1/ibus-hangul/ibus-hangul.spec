%global require_ibus_version 1.3.99
%global require_libhangul_version 0.1.0

Name:       ibus-hangul
Version:    1.5.5
Release:    12%{?dist}
Summary:    The Hangul engine for IBus input platform
License:    GPL-2.0-or-later
URL:        https://github.com/libhangul/ibus-hangul
Source0:    https://github.com/libhangul/ibus-hangul/releases/download/%{version}/%{name}-%{version}.tar.xz

# not upstreamed patches
Patch1:     ibus-hangul-setup-abspath.patch
Patch2:     ibus-hangul-fixes-osk.patch
# oreon url source checksums begin
%global source0_sha256 a5aac88286cd18960229860e3e1a778978a7aeaa484ad9acfa48284b87fdc3bb
%global source0_file ibus-hangul-1.5.5.tar.xz
# oreon url source checksums end

BuildRequires:  gettext-devel, automake, libtool
BuildRequires:  libhangul-devel >= %{require_libhangul_version}
BuildRequires:  pkgconfig
BuildRequires:  ibus-devel >= %{require_ibus_version}
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  gtk3-devel
BuildRequires:  make

Requires:   ibus >= %{require_ibus_version}
Requires:   libhangul >= %{require_libhangul_version}
Requires:   python3-gobject
Requires:   python3

%description
The Hangul engine for IBus platform. It provides Korean input method from
libhangul.

%package tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ibus-hangul-1.5.5.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a5aac88286cd18960229860e3e1a778978a7aeaa484ad9acfa48284b87fdc3bb" || { echo "oreon: Source0 SHA256 mismatch for ibus-hangul-1.5.5.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
./autogen.sh
%configure \
           --disable-static \
           --with-python=python3 \
           %{?_with_hotkeys} \
           --enable-installed-tests \
           %{nil}

make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install INSTALL="install -p"

%py_byte_compile %{python3} $RPM_BUILD_ROOT%{_datadir}/ibus-hangul/setup

rm -f ${RPM_BUILD_ROOT}%{_bindir}/ibus-setup-hangul
sed -i 's!^Exec=ibus-setup-hangul!Exec=%{_libexecdir}/ibus-setup-hangul!' ${RPM_BUILD_ROOT}%{_datadir}/applications/ibus-setup-hangul.desktop

desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/ibus-setup-hangul.desktop

%find_lang %{name}

%check
make check \
    DISABLE_GUI_TESTS="ibus-hangul" \
    VERBOSE=1

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-hangul
%{_libexecdir}/ibus-setup-hangul
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/*
%{_datadir}/applications/ibus-setup-hangul.desktop
%{_datadir}/icons/hicolor/*/apps/*

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/ibus-hangul
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/ibus-hangul

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.5-12
- Prepare for Oreon 11 (RP1)
