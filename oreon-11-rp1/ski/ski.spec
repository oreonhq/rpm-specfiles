%global source0_hash 797e3443b605c861bd193e40e646ce687ee9679d0ecfe35758344d1456716f06
Name:           ski
Version:        1.5.1
Release:        1%{?dist}
Summary:        IA-64 user and system mode simulator
License:        GPL-2.0-only and GPL-2.0-or-later
URL:            https://github.com/trofi/ski
Source0:        https://github.com/trofi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
ExcludeArch:    aarch64
Obsoletes: %{name}-libs < 1.4.0
Obsoletes: %{name}-devel < 1.4.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
The Ski IA-64 user and system simulator originally developed by HP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
