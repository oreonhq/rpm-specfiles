%global source0_hash a5aac88286cd18960229860e3e1a778978a7aeaa484ad9acfa48284b87fdc3bb
%global require_ibus_version 1.3.99
%global require_libhangul_version 0.1.0
Name:       ibus-hangul
Version:    1.5.5
Release:        1%{?dist}
Summary:        The Hangul engine for IBus input platform
License:    GPL-2.0-or-later
URL:        https://github.com/libhangul/ibus-hangul
Source0:        https://github.com/libhangul/ibus-hangul/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch1:     ibus-hangul-setup-abspath.patch
Patch2:     ibus-hangul-fixes-osk.patch
Requires:   ibus >= %{require_ibus_version}
Requires:   libhangul >= %{require_libhangul_version}
Requires:   python3-gobject
Requires:   python3
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  ibus-devel
BuildRequires:  libhangul-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check \
    DISABLE_GUI_TESTS="ibus-hangul" \
    VERBOSE=1
%files -f %{oreon_filedir}/main.list
%files -n ibus-hangul-tests -f %{oreon_filedir}/ibus-hangul-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.5-12
- Prepare for Oreon 11 (RP1)
