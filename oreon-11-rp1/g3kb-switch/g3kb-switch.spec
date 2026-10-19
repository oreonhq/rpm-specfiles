%global source0_hash 91bf59bf8bc132a146a0556f3e293d69ea00114bc16c106a4d37f7a0f2c06a18
%global uuid g3kb-switch@g3kb-switch.org
Name:           g3kb-switch
Version:        1.5
Release:        1%{?dist}
Summary:        CLI keyboard layout switcher for GNOME Shell
License:        BSD-2-Clause AND GPL-2.0-only
URL:            https://github.com/lyokha/g3kb-switch
Source0:        https://github.com/lyokha/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          gnome-47.patch
Patch:          gnome-48.patch
Patch:          gnome-49.patch
Requires:       gnome-shell
Obsoletes:      %{name}-devel < 1.4-2
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)
# /oreon:deps
%description
This is a CLI keyboard layout switcher for Gnome 3 and 4x. It is
not based on the X interface but rather implements direct D-Bus
messaging with the Gnome Shell.

%package        zsh-completion
Summary:        Zsh completion for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)
%description    zsh-completion
Zsh command line completion support for %{name}.

%package        bash-completion
Summary:        Bash completion for %{name}
BuildArch:      noarch
BuildRequires:  bash-completion
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
%description    bash-completion
Bash command line completion support for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i '1{\@#!/usr/bin/env bash@d}' g3kb-switch-completion.bash

%build

export GITHUB_REF_NAME=%{version}
%cmake -DG3KBSWITCH_WITH_GNOME_SHELL_EXTENSION:BOOL=ON \
       -DG3KBSWITCH_VIM_XKBSWITCH_LIB_PATH:PATH=%{_lib}/%{name}
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_datadir}/pkgconfig/%{name}.pc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n g3kb-switch-zsh-completion -f %{oreon_filedir}/g3kb-switch-zsh-completion.list
%files -n g3kb-switch-bash-completion -f %{oreon_filedir}/g3kb-switch-bash-completion.list

%changelog

%autochangelog
