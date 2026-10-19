%global source0_hash b1e60b13f10e1b6185763f52fe0df7fa65735e5f5c8b0dedc1a65067af46bdfb
%bcond check 0
Name: conan
Version: 2.33.0
Release:        1%{?dist}
License: MIT
Summary:        Open-source C/C++ package manager
URL: https://github.com/%{name}-io/%{name}
Source0:        https://github.com/%{name}-io/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
%if %{with check}
%endif
Requires: cmake
Requires: gcc
Requires: gcc-c++
Requires: git-core
Requires: ninja-build
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-conan = %{version}-%{release}
# /oreon:deps
%description
Conan is a package manager for C and C++ developers.

It is fully decentralized. Users can host their packages on their servers,
privately.

Works across all platforms. It can create, upload and download binaries for
any configuration and platform, even cross-compiling, saving lots of time in
development and continuous integration. The binary compatibility can be
configured and customized. Manage all your artifacts in the same way on all
platforms.

Integrates with any build system. Provides tested support for most major
build systems.

Its python based recipes, together with extensions points allows for great
power and flexibility.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -e 's/, .*//g' -i %{name}s/requirements.txt
find -name '*.py' \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; -exec sed -i '1d' {} \; \)

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%if %{with check}
%{pytest} -v test/unittests
rm test/integration/toolchains/gnu/test_autotoolsdeps.py test/integration/toolchains/microsoft/test_vs_layout.py test/integration/workspace/test_workspace.py
%{pytest} -v test/integration
%endif
%files

%changelog

%autochangelog
