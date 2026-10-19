%global source0_hash a749518116624e0ff1f71c9eadfd28e8580c3be6534446fbcd421ab6a67d453e
Name: argbash
Version: 2.11.0
Release:        1%{?dist}
Summary:        Bash argument parsing code generator
License: LicenseRef-Callaway-BSD
URL: https://argbash.dev
Source0:        https://github.com/matejak/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: autoconf
Requires: bash
Requires: coreutils
Requires: grep
Requires: sed
Patch: 0001-Fix-uninitialized-wrapped-script-arrays-causing-shel.patch
# oreon:deps
BuildRequires:  ShellCheck
BuildRequires:  autoconf
BuildRequires:  bash
BuildRequires:  bash-completion
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  python3-docutils
# /oreon:deps
%description
Argbash helps your shell scripts to accept arguments.
You declare what arguments you want your script to accept and Argbash
generates the shell code that parses them from the command-line and exposes
passed values as shell variables.

Help message is also generated, and helpful error messages are dispatched
if the script is called with arguments that conflict with the interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
cd resources && \
    ROOT=%{buildroot} \
    PREFIX=%{_prefix} \
    PREFIXED_LIBDIR=%{_datarootdir} \
    SYSCONFDIR=%{_sysconfdir} \
    INSTALL_COMPLETION=yes \
    BASH_COMPLETION_DIRECTORY=%{_datarootdir}/bash-completion/completions \
    make install
%oreon_autofiles main

%check

cd resources && %{make_build} check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
