%global source0_hash 4856c5c6a659e36f49a9f45631832ce80f108d6e37e3fc6e944829f318110478
%global commit       b1ae9c96a2244184aa8c0e1303e3bcc1e8d78117
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global commitdate   20240602
Name:    blogc
Version: 0.20.1^%{commitdate}.%{shortcommit}
Release:        4%{?dist}
License: BSD-3-Clause AND MIT
Summary:        A blog compiler
URL:     https://blogc.rgm.io/
VCS:     git:https://github.com/blogc/blogc.git
Source0:        blogc.tar.gz
Source1: getsource.sh
Patch0:   https://github.com/blogc/blogc/pull/17.patch#/getaddrinfo.patch
Patch1:   https://github.com/blogc/blogc/pull/18.patch#/mitlicense.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  bash
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libcmocka-devel
BuildRequires:  rubygem-ronn-ng
BuildRequires:  tar
# /oreon:deps
%description
blogc(1) is a blog compiler. It compiles source files and templates into
blog/website resources.

%package git-receiver
Summary: A simple login shell/git hook to deploy blogc websites
Requires: git-core
Requires: make
Requires: tar
Requires: %{name}-make%{?_isa} = %{version}-%{release}
%description git-receiver
blogc-git-receiver is a simple login shell/git hook to deploy blogc websites.

%package make
Summary: A simple build tool for blogc
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-runserver%{?_isa} = %{version}-%{release}
%description make
blogc-make is a simple build tool for blogc websites.

%package runserver
Summary: A simple HTTP server to test blogc websites
%description runserver
blogc-runserver is a simple HTTP server to test blogc websites.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir blogc
%oreon_prep
%build

%cmake -DBUILD_BLOGC_GIT_RECEIVER=ON \
       -DBUILD_BLOGC_MAKE=ON \
       -DBUILD_BLOGC_RUNSERVER=ON \
       -DBUILD_MANPAGES=ON \
       -DBUILD_TESTING=ON \
       -DCMAKE_C_COMPILER=gcc
%cmake_build
%install
%cmake_install
%oreon_autofiles blogc-git-receiver usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles blogc-make usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles blogc-runserver usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n blogc-git-receiver -f %{oreon_filedir}/blogc-git-receiver.list
%files -n blogc-make -f %{oreon_filedir}/blogc-make.list
%files -n blogc-runserver -f %{oreon_filedir}/blogc-runserver.list

%changelog

%autochangelog
