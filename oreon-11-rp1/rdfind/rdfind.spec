%global source0_hash 0a2d0d32002cc2dc0134ee7b649bcc811ecfb2f8d9f672aa476a851152e7af35
Name:		rdfind
Version:	1.8.0
Release:        1%{?dist}
Summary:        Program that finds duplicate files
License:	GPL-2.0-or-later
URL:		https://rdfind.pauldreik.se/
Source0:        https://%{name}.pauldreik.se//%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nettle-devel
# /oreon:deps
%description
Rdfind is a program that finds duplicate files. It is useful for compressing
backup directories or just finding duplicate files. It compares files based on
their content, NOT on their file names.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="%{optflags} -std=c++17"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
