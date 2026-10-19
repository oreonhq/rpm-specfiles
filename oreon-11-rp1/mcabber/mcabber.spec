%global source0_hash 90528bcddd41b6e41d6702cd583ac22eef57360322315daa2275a8ed5f98dfda
%global gitcommit_full 87964c375c9457128f2dd1de4e0f6c8b2bd2a089
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20211025
Name:           mcabber
Version:        1.1.3
Release:        1%{?dist}
Summary:        Console Jabber instant messaging client
License:        GPL-2.0-or-later
URL:            https://mcabber.com
Source0:        https://github.com/McKael/%{name}/tarball/%{gitcommit_full}
# oreon:deps
BuildRequires:  clang
BuildRequires:  enchant-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gpgme-devel
BuildRequires:  libotr-devel
BuildRequires:  libtool
BuildRequires:  loudmouth-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
# /oreon:deps
%package devel
Summary: Development files for mcabber
Requires: %{name} = %{version}-%{release} pkgconfig
%description
mcabber is a console Jabber instant messaging/chat client with SSL support, MUC
(Multi-User Chat) support, history logging, commands completion, and external
action triggers.

%description devel
Headers and miscellaneous files used for building projects using mcabber

%prep

%autosetup -n McKael-mcabber-%{gitcommit}

%build

pushd %{name}
    bash autogen.sh
    %configure --disable-dependency-tracking \
               --enable-enchant \
               --enable-otr \
               CC=clang
    %make_build
popd
%install
pushd %{name}
    %make_install
    find contrib/ -type f | xargs chmod -x
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mcabber-devel -f %{oreon_filedir}/mcabber-devel.list

%changelog

%autochangelog
