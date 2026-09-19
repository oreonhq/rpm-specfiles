%global source0_hash 608ba6b934869a5fe5d7402a178e2a24101d71eda2cb9b4b19e09058023eb8dc

# EL8 and earlier does not have _vpath_builddir defined
%{?!_vpath_builddir:%define _vpath_builddir %{_target_platform}}

%if %{?cmake_build:1}%{?!cmake_build:0}
%global old_build 0
%else
%global old_build 1
%endif

%if 0%{?rhel} > 0
# bug 1883094 - hexchat-autoaway failed to build in aarch64 because hexchat-devel is missing
excludearch:    aarch64
# bug 1883095 - hexchat-autoaway failed to build in 390x because hexchat-devel is missing
excludearch:    s390x
%if 0%{?rhel} == 9
# hexchat-devel is missing for ppc64le
excludearch:    ppc64le
%endif
%endif

Name:           hexchat-autoaway
Version:        2.0
Release:        19%{?dist}
Summary:        HexChat plugin that automatically mark you away

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/andreyv/hexchat-autoaway
Source0:        https://github.com/andreyv/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

## Upstream PR#3 "feat(away-nick-suffix): append away suffix to nickname"
Patch0:         https://patch-diff.githubusercontent.com/raw/andreyv/hexchat-autoaway/pull/3.patch#/0001-append-away-suffix-to-nickname.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gtk2-devel >= 2.14
BuildRequires:  hexchat-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires: make
Requires: gtk2 >= 2.14
Requires: hexchat

%description
This HexChat plugin will automatically mark you away when your
computer is idle. It works on systems that use the GTK+ X11
backend, such as GNU/Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%build
%if %old_build
mkdir -p %_vpath_builddir
cd %_vpath_builddir && %cmake3 -DCMAKE_BUILD_TYPE=Release ..
%make_build
cd -
%else
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%endif

%install
%if %old_build
%make_install -C %_vpath_builddir
%else
%cmake_install
%endif

%files
%license COPYING
%doc README.md
%{_libdir}/hexchat/plugins/libautoaway.so

%changelog
%autochangelog
