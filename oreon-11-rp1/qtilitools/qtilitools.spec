%global source0_hash 79aa0c5f2b742b38346b83234a4e26d7b4a633f1eba47c89a9ee9309d7ef2a8d
Name:		qtilitools
Version:	0.1.2
Release:        4%{?dist}
License:	BSD-3-Clause
URL:		https://github.com/qtilities/%{name}
Source0:        https://github.com/qtilities/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Summary:        Scripts/commands used with qtilities apps
BuildArch:      noarch
Patch0:         language-fix.patch
# oreon:deps
BuildRequires:  cmake
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
