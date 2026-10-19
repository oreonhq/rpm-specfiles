%global source0_hash 0cef77fda779579f4c582a53dc7890895dc5da6157d6dbd728d30e4b25f94fbb
Name:           R-oskeyring
Version:        %R_rpm_version 0.1.6
Release:        1%{?dist}
Summary:        Raw System Credential Store Access from R
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=oskeyring&version=%{version}#/oskeyring_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Aims to support all features of the system credential store, including non-
portable ones. Supports Keychain on macOS, and Credential Manager on
Windows. See the keyring package if you need a portable API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
