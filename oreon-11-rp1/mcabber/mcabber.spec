%global source0_hash none

%global gitcommit_full 87964c375c9457128f2dd1de4e0f6c8b2bd2a089
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20211025

Name:           mcabber
Version:        1.1.3
Release:        0.11.%{date}git%{gitcommit}%{?dist}
Summary:        Console Jabber instant messaging client

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://mcabber.com
# Source0:        http://mcabber.com/files/%{name}-%{version}.tar.bz2
Source0:        https://github.com/McKael/%{name}/tarball/%{gitcommit_full}

BuildRequires:  make
BuildRequires:  clang
BuildRequires:  enchant-devel
BuildRequires:  gpgme-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  glib2-devel
BuildRequires:  gettext-devel
BuildRequires:  libotr-devel >= 4.0.0
BuildRequires:  loudmouth-devel
BuildRequires:  libtool

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

# Let's get the executable bits off the contrib files, avoiding unwanted deps.
    find contrib/ -type f | xargs chmod -x
popd

%files
%doc %{name}/contrib %{name}/AUTHORS %{name}/ChangeLog %{name}/NEWS
%doc %{name}/README %{name}/doc/README_PGP.txt %{name}/TODO %{name}/*.example
%license %{name}/COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_libdir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
