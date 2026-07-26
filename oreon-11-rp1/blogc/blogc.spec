%global source0_hash 4856c5c6a659e36f49a9f45631832ce80f108d6e37e3fc6e944829f318110478

%global commit       b1ae9c96a2244184aa8c0e1303e3bcc1e8d78117
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global commitdate   20240602
Name:    blogc
Version: 0.20.1^%{commitdate}.%{shortcommit}
Release: 4%{?dist}
# All code is BSD-3-Clause except src/common/utf8.c which is MIT
License: BSD-3-Clause AND MIT
Summary: A blog compiler

URL:     https://blogc.rgm.io/
VCS:     git:https://github.com/blogc/blogc.git
Source0: blogc.tar.gz
# Need Git files for build version from a commit
Source1: getsource.sh
# https://github.com/blogc/blogc/pull/17
Patch0:   https://github.com/blogc/blogc/pull/17.patch#/getaddrinfo.patch
# https://github.com/blogc/blogc/pull/18
Patch1:   https://github.com/blogc/blogc/pull/18.patch#/mitlicense.patch

BuildRequires: bash
BuildRequires: cmake
BuildRequires: coreutils
BuildRequires: diffutils
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: libcmocka-devel
BuildRequires: rubygem-ronn-ng
BuildRequires: tar

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

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

%autosetup  -n blogc -p 1

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

%check
%ctest

%files
%{_mandir}/man*/blogc.*
%{_mandir}/man*/blogc-source.*
%{_mandir}/man*/blogc-template.*
%{_mandir}/man*/blogc-toctree.*
%{_mandir}/man*/blogc-pagination.*
%{_bindir}/blogc
%doc README.md
%license LICENSE

%files git-receiver
%{_mandir}/man*/blogc-git-receiver.*
%{_bindir}/blogc-git-receiver
%license LICENSE

%files make
%{_mandir}/man*/blogc-make.*
%{_mandir}/man*/blogcfile.*
%{_bindir}/blogc-make
%license LICENSE

%files runserver
%{_mandir}/man*/blogc-runserver.*
%{_bindir}/blogc-runserver
%license LICENSE

%changelog
%autochangelog
