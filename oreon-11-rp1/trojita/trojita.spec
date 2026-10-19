%global source0_hash baf055d9a6e613be4d99abeda07d921f90124eda7ac256c1a9902c04ece3fce1
%undefine __cmake_in_source_build
%bcond doxy 0
%bcond testsqtwebkit 0
%bcond ragel 0
%global gitdate 20230430
%global commit0 d1e1b4a69e934d1fed930634b4a6a637bea273a8
%global srcurl  https://github.com/KDE/%{name}
Name:           trojita
Version:        0.7.0.1
Release:        1%{?dist}
Source0:        %{srcurl}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
Source10:       %{name}_common-po-20221113.tar.xz
Patch11:        trojita-0.7.0.1-disable-gpg-tests.patch
License:        GPL-2.0-or-later
Summary:        IMAP e-mail client
URL:            http://%{name}.flaska.net
ExcludeArch:    ppc64 ppc64le s390x
%global ctest ctest%{?rhel:3} %{?_smp_mflags} --output-on-failure -VV
Requires:       qt5-qtsvg
%if %{with ragel}
%endif
%if %{undefined flatpak}
%endif
%if %{with doxy}
%endif
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gnupg2-smime
BuildRequires:  gpgme-devel
BuildRequires:  gpgmepp-devel
BuildRequires:  grantlee-qt5-devel
BuildRequires:  kf5-akonadi-contacts-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-sonnet-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  mimetic-devel
BuildRequires:  pinentry
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qgpgme-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qtkeychain-qt5-devel
BuildRequires:  ragel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Trojitá is a IMAP e-mail client which:
  * Enables you to access your mail anytime, anywhere.
  * Does not slow you down. If we can improve the productivity of an e-mail
    user, we better do.
  * Respects open standards and facilitates modern technologies. We value
    the vendor-neutrality that IMAP provides and are committed to be as
    inter-operable as possible.
  * Is efficient — be it at conserving the network bandwidth, keeping memory
    use at a reasonable level or not hogging the system's CPU.
  * Can be used on many platforms. One UI is not enough for everyone, but our
    IMAP core works fine on anything from desktop computers to cell phones
    and big ERP systems.
  * Plays well with the rest of the ecosystem. We don't like reinventing wheels,
    but when the existing wheels quite don't fit the tracks, we're not afraid
    of making them work.

This application is heavily based on Qt and uses WebKit.

%if %{with doxy}
# optional developer documentation
%package doc
BuildArch: noarch
Summary:   Documentation files for %{name}
%description doc
%{summary}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn%{name}-%{commit0} -a10
%patch 11 -p1 -b .disable-gpg-tests

%build

%if %{without testsqtwebkit}
export CXXFLAGS="%{optflags} -DSKIP_WEBKIT_TESTS"
%endif
%cmake_kf5 \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_RPATH=%{_libdir}/%{name} \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON \
    -DWITH_AKONADIADDRESSBOOK_PLUGIN:BOOL=%{!?flatpak:ON}%{?flatpak:OFF} \
    -DWITH_GPGMEPP:BOOL=ON \
    -DWITH_SONNET_PLUGIN:BOOL=ON \
    -DWITH_RAGEL:BOOL=%{?with_ragel:ON}%{!?with_ragel:OFF}
%cmake_build
%if %{with doxy}
doxygen src/Doxyfile
%endif
%install
%cmake_install
%find_lang %{name}_common --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*%{name}.desktop
xvfb-run -a %ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
