%global source0_hash 0aed2c5df101d5108b9cc8d6da0dddfad1286a66b49c794e38b2a6d0d868393e
Name:		uncrustify
Version:	0.83.0
Release:        1%{?dist}
Summary:        Reformat Source
License:	GPL-2.0-or-later
URL:		https://uncrustify.sourceforge.net/
Source0:        https://prdownloads.sourceforge.net/uncrustify/uncrustify-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
Source Code Beautifier for C, C++, C#, D, Java, and Pawn

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir uncrustify-uncrustify-%{version}
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
