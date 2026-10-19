%global source1_hash 37fb702124396be090cf7bdda999bc4741b9c85b1f27d2a66df95a31b1b6c9e2
%global source0_hash ced99d452f43055f1ecba0df52274fee64447df3373b275f3d312400ac621739
%undefine __cmake_in_source_build
Name:       csmock
Version:    3.8.4
Release:        1%{?dist}
Summary:        A mock wrapper for Static Analysis tools
License:    GPL-3.0-or-later
URL:        https://github.com/csutils/%{name}
Source0:        https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
Source2:    kdudka.pgp
Requires: csmock-common                 >= %{version}-%{release}
Requires: csmock-plugin-clang           >= %{version}-%{release}
Requires: csmock-plugin-cppcheck        >= %{version}-%{release}
Requires: csmock-plugin-gitleaks        >= %{version}-%{release}
Requires: csmock-plugin-shellcheck      >= %{version}-%{release}
BuildArch: noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gnupg2
BuildRequires:  help2man
BuildRequires:  python3-GitPython
BuildRequires:  python3-devel
# /oreon:deps
%description
This is a metapackage pulling in csmock-common and basic csmock plug-ins.

%package -n csbuild
Summary: Tool for plugging static analyzers into the build process
Requires: cscppc
Requires: csclng
Requires: csdiff
Requires: csmock-common
Requires: cswrap
Requires: python%{python3_pkgversion}-GitPython
%description -n csbuild
Tool for plugging static analyzers into the build process, free of mock.

%package common
Summary: Core of csmock (a mock wrapper for Static Analysis tools)
Requires: csdiff > 3.5.1
Requires: csgcca
Requires: cswrap
Requires: mock >= 5.7
Requires: tar
Requires: xz
%description common
This package contains the csmock tool that allows to scan SRPMs by Static
Analysis tools in a fully automated way.

%package plugin-bandit
Summary: csmock plug-in providing the support for Bandit.
Requires: csmock-common
%description plugin-bandit
This package contains the bandit plug-in for csmock.

%package plugin-cbmc
Summary: csmock plug-in providing the support for cbmc
Requires: csexec
Requires: csmock-common
%description plugin-cbmc
This package contains the cbmc plug-in for csmock.

%package plugin-clang
Summary: csmock plug-in providing the support for Clang
Requires: csclng
Requires: csmock-common
%description plugin-clang
This package contains the clang plug-in for csmock.

%package plugin-clippy
Summary: csmock plug-in providing the support for Rust Clippy.
Requires: csmock-common
%description plugin-clippy
This package contains the Rust Clippy plug-in for csmock.

%package plugin-cppcheck
Summary: csmock plug-in providing the support for Cppcheck
Requires: cscppc
Requires: csmock-common
%description plugin-cppcheck
This package contains the cppcheck plug-in for csmock.

%package plugin-divine
Summary: csmock plug-in providing the support for divine
Requires: csexec
Requires: csmock-common
%description plugin-divine
This package contains the divine plug-in for csmock.

%package plugin-gitleaks
Summary: experimental csmock plug-in
Requires: csmock-common
%description plugin-gitleaks
This package contains the gitleaks plug-in for csmock.

%package plugin-infer
Summary: csmock plug-in providing the support for Infer
Requires: csmock-common
%description plugin-infer
This package contains the Infer plug-in for csmock.

%package plugin-pylint
Summary: csmock plug-in providing the support for Pylint.
Requires: csmock-common
%description plugin-pylint
This package contains the pylint plug-in for csmock.

%package plugin-semgrep
Summary: csmock plug-in providing the support for semgrep scan
Requires: csmock-common
%description plugin-semgrep
This package contains the semgrep plug-in for csmock.

%package plugin-shellcheck
Summary: csmock plug-in providing the support for ShellCheck.
Requires: csmock-common
Requires: csmock-plugin-shellcheck-core
%description plugin-shellcheck
This package contains the shellcheck plug-in for csmock.

%package plugin-shellcheck-core
Conflicts: csmock-plugin-shellcheck < %{version}-%{release}
Summary: script to run shellcheck on a directory tree
%description plugin-shellcheck-core
This package contains the run-shellcheck.sh script to run shellcheck on a directory tree.

%package plugin-smatch
Summary: csmock plug-in providing the support for smatch
Requires: csmatch
Requires: csmock-common
Requires: cswrap
%description plugin-smatch
This package contains the smatch plug-in for csmock.

%package plugin-snyk
Summary: csmock plug-in providing the support for snyk
Requires: csmock-common
%description plugin-snyk
This package contains the snyk plug-in for csmock.

%package plugin-strace
Summary: csmock plug-in providing the support for strace
Requires: csexec
Requires: csmock-common
%description plugin-strace
This package contains the strace plug-in for csmock.

%package plugin-symbiotic
Summary: csmock plug-in providing the support for symbiotic
Requires: csexec
Requires: csmock-common
%description plugin-symbiotic
This package contains the symbiotic plug-in for csmock.

%package plugin-valgrind
Summary: csmock plug-in providing the support for valgrind
Requires: csexec
Requires: csmock-common
%description plugin-valgrind
This package contains the valgrind plug-in for csmock.

%package plugin-unicontrol
Summary: experimental csmock plug-in
Requires: csmock-common
%description plugin-unicontrol
This package contains the unicontrol plug-in for csmock.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%cmake                                        \
    -DVERSION='%{name}-%{version}-%{release}' \
    -DPython3_EXECUTABLE='%{__python3}'
%cmake_build
%install
%cmake_install
%oreon_autofiles csbuild usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-bandit usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-cbmc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-clang usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-clippy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-cppcheck usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-divine usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-gitleaks usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-infer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-pylint usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-semgrep usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-shellcheck usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-shellcheck-core usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-smatch usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-snyk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-strace usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-symbiotic usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-valgrind usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmock-plugin-unicontrol usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n csbuild -f %{oreon_filedir}/csbuild.list
%files -n csmock-common -f %{oreon_filedir}/csmock-common.list
%files -n csmock-plugin-bandit -f %{oreon_filedir}/csmock-plugin-bandit.list
%files -n csmock-plugin-cbmc -f %{oreon_filedir}/csmock-plugin-cbmc.list
%files -n csmock-plugin-clang -f %{oreon_filedir}/csmock-plugin-clang.list
%files -n csmock-plugin-clippy -f %{oreon_filedir}/csmock-plugin-clippy.list
%files -n csmock-plugin-cppcheck -f %{oreon_filedir}/csmock-plugin-cppcheck.list
%files -n csmock-plugin-divine -f %{oreon_filedir}/csmock-plugin-divine.list
%files -n csmock-plugin-gitleaks -f %{oreon_filedir}/csmock-plugin-gitleaks.list
%files -n csmock-plugin-infer -f %{oreon_filedir}/csmock-plugin-infer.list
%files -n csmock-plugin-pylint -f %{oreon_filedir}/csmock-plugin-pylint.list
%files -n csmock-plugin-semgrep -f %{oreon_filedir}/csmock-plugin-semgrep.list
%files -n csmock-plugin-shellcheck -f %{oreon_filedir}/csmock-plugin-shellcheck.list
%files -n csmock-plugin-shellcheck-core -f %{oreon_filedir}/csmock-plugin-shellcheck-core.list
%files -n csmock-plugin-smatch -f %{oreon_filedir}/csmock-plugin-smatch.list
%files -n csmock-plugin-snyk -f %{oreon_filedir}/csmock-plugin-snyk.list
%files -n csmock-plugin-strace -f %{oreon_filedir}/csmock-plugin-strace.list
%files -n csmock-plugin-symbiotic -f %{oreon_filedir}/csmock-plugin-symbiotic.list
%files -n csmock-plugin-valgrind -f %{oreon_filedir}/csmock-plugin-valgrind.list
%files -n csmock-plugin-unicontrol -f %{oreon_filedir}/csmock-plugin-unicontrol.list

%changelog

%autochangelog
