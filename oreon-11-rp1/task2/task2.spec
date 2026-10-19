%global source0_hash b1d3a7f000cd0fd60640670064e0e001613c9e1cb2242b9b3a9066c78862cfec
%global upstream_name task
Name:           task2
Version:        3.5.0
Release:        1%{?dist}
Summary:        Taskwarrior - a command-line TODO list manager
License:        MIT
URL:            https://taskwarrior.org
Source0:        https://%{upstream_name}warrior.org/download/%{upstream_name}-%{version}.tar.gz
Provides:       task = %{version}-%{release}
Obsoletes:      task < 3
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libuuid-devel
# /oreon:deps
%description
Taskwarrior is a command-line TODO list manager. It is flexible, fast,
efficient, unobtrusive, does its job then gets out of your way.

Taskwarrior scales to fit your workflow. Use it as a simple app that captures
tasks, shows you the list, and removes tasks from that list. Leverage its
capabilities though, and it becomes a sophisticated data query tool that can
help you stay organized, and get through your work.

This package provides the taskv2 compatibility package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}-%{version}

# add #include <cstdint>
sed -i '/<Pig.h>/ a #include <cstdint>' src/libshared/src/JSON.h
grep -C4 -nri "<cstdint>" src/libshared/src/JSON.h

%build

%cmake -DTASK_RCDIR=share/%{upstream_name}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm0644 scripts/zsh/_%{upstream_name} %{buildroot}%{_datadir}/zsh/site-functions/_%{upstream_name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -Dpm0644 scripts/bash/%{upstream_name}.sh %{buildroot}%{_datadir}/bash-completion/completions/%{upstream_name}
mkdir -p %{buildroot}%{_datadir}/fish/completions/
install -Dpm0644 scripts/fish/%{upstream_name}.fish %{buildroot}%{_datadir}/fish/completions/%{upstream_name}.fish
find scripts/ -type f -exec chmod -x {} ';'
find scripts/ -type f -exec sed -i -e '1{\@^#!.*@d}' {} ';'
rm -vrf %{buildroot}%{_datadir}/doc/%{upstream_name}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
