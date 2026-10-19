%global source1_hash 276b91c7fdfcf6779a89a623af21492c2d29806875203fb51d55271dedb56b00
%global source0_hash 1d79da684ba4b8bee82e55987361cceb970678045a26ad0b5435de44510b3252
%global pkg  anthy-unicode
%bcond_without xemacs
Name:  anthy-unicode
Version: 1.0.0.20260213
Release:        1%{?dist}
License: LGPL-2.0-or-later AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:  https://github.com/fujiwarat/anthy-unicode/wiki
%if %{with xemacs}
%endif
Source0:        https://github.com/fujiwarat/anthy-unicode/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/fujiwarat/anthy-unicode/releases/download/%{version}/%{name}-%{version}.tar.xz.sha256sum#/%{name}.tar.xz.sha256sum
Source2:        anthy-unicode-init.el
Summary:        Japanese character set input library for Unicode
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  meson
# /oreon:deps
%description
Anthy Unicode is another Anthy project and provides the library to input
Japanese on the applications, such as X applications and emacs. and the
user dictionaries and the users information which is used for the conversion,
is stored into their own home directory. So Anthy Unicode is secure than
other conversion server.

%package -n emacs-%{pkg}
Summary: Emacs files for %{pkg}
Requires: %{name} = %{version}-%{release}
Requires: emacs-filesystem
BuildArch: noarch
%description -n emacs-%{pkg}
This package contains the byte compiled elips packages to run %{pkg}
with GNU Emacs.

%if %{with xemacs}
%package -n xemacs-%{pkg}
Summary: XEmacs files for %{pkg}
Requires: %{name} = %{version}-%{release}
Requires: xemacs-filesystem >= %{_xemacs_version}
BuildArch: noarch
%description -n xemacs-%{pkg}
This package contains the elips packages to run %{pkg} with GNU XEmacs.
%endif

%package devel
Summary: Header files and library for developing programs which uses Anthy Unicode
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
The anthy-devel package contains the development files which is needed to build
the programs which uses Anthy Unicode.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
SAVED_SUM=$(cat %SOURCE1 | cut -d' ' -f1)
MY_SUM=$(sha256sum %SOURCE0 | cut -d' ' -f1)
if test x"$SAVED_SUM" != x"$MY_SUM" ; then
    echo "checksum mismatch for Source0" >&2
    exit 1
fi
%autosetup -S git -n anthy-unicode-1.0.0.20260213

%build

%meson \
        -Demacs=enabled \
        %{nil}
%meson_build
%install
%meson_install
pushd ./src-util
install -m 644 dic-tool-input $RPM_BUILD_ROOT%{_datadir}/%{pkg}
install -m 644 dic-tool-result $RPM_BUILD_ROOT%{_datadir}/%{pkg}
popd
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_emacs_sitestartdir}
%if %{with xemacs}
mkdir -p $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
pushd ./src-util
make clean
xemacs --batch --eval '(setq load-path (cons nil load-path))' -f batch-byte-compile *.el
make
make install-lispLISP DESTDIR=$RPM_BUILD_ROOT EMACS=xemacs lispdir="%{_xemacs_sitelispdir}/%{pkg}" INSTALL="install -p"
popd
%oreon_autofiles emacs-anthy-unicode usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles anthy-unicode-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

sed -e "s|@datadir@|$PWD|" -e "s|@PACKAGE@|redhat-linux-build/mkanthydic|" \
  anthy-unicode.conf.in > test.conf
_TEST_ENV="CONFFILE=$PWD/test.conf"
cd redhat-linux-build/test
env $_TEST_ENV ./anthy --all
env $_TEST_ENV ./checklib
cd ../../src-util
env $_TEST_ENV ../redhat-linux-build/src-util/anthy-dic-tool-unicode --load dic-tool-input
diff $HOME/.config/anthy/private_words_default dic-tool-result
env $_TEST_ENV ../redhat-linux-build/src-util/anthy-dic-tool-unicode --dump
mkdir -p $HOME/.anthy
mv $HOME/.config/anthy/private_words_default $HOME/.anthy
env $_TEST_ENV ../redhat-linux-build/src-util/anthy-dic-tool-unicode --migrate
diff $HOME/.config/anthy/private_words_default dic-tool-result
cd ..
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n emacs-anthy-unicode -f %{oreon_filedir}/emacs-anthy-unicode.list
%files -n anthy-unicode-devel -f %{oreon_filedir}/anthy-unicode-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0.20260213-1
- Prepare for Oreon 11 (RP1)
