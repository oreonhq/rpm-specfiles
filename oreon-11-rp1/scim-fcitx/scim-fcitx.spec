%global source0_hash 43400c00c777be5a9ca7f369856e89819cd832f1bb3ff2641660dffa887df2a5

Name:           scim-fcitx
Version:        3.1.1
Release:        44%{?dist}
Summary:        FCITX Input Method Engine for SCIM

License:        GPL-2.0-or-later
URL:            https://github.com/scim-im/scim-fcitx
Source0:        http://dl.sourceforge.net/scim/%{name}.%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  scim-devel
Requires:	scim

Patch0:         scim-fcitx-3.1.1-gcc43.patch
Patch1:         scim-fcitx-3.1.1-gcc47.patch
Patch2:         scim-fcitx-configure-c99.patch

%description
scim-fcitx is a port of the fcitx Chinese input method for the SCIM input
method platform.  It provides Wubi, Erbi, Cangjie, and Pinyin styles of input.

%package tools
Summary:    Fcitx tables tools

%description tools
This package contains input table tools from fcitx.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n fcitx
%patch -P0 -p1 -b .gcc43
%patch -P1 -p1 -b .gcc47
%patch -P2 -p1 -b .c99

%build
%configure --disable-static
# doesn't build with %{?_smp_mflags}
make

%install
make DESTDIR=${RPM_BUILD_ROOT} install

rm ${RPM_BUILD_ROOT}/%{_libdir}/scim-1.0/*/IMEngine/fcitx.la

pushd ${RPM_BUILD_ROOT}/%{_bindir}/
  mv createPYMB createPYMB3
  mv mb2txt mb2txt3
  mv txt2mb txt2mb3
popd

%files
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/scim-1.0/*/IMEngine/fcitx.so
%{_datadir}/scim/fcitx
%{_datadir}/scim/icons/fcitx

%files tools
%{_bindir}/*

%changelog
%autochangelog
