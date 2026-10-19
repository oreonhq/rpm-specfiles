%global source2_hash 4e3a0863dd448b928c5acba130974a16c1aff9a396a1b9e9cca067a198265f5e
%global source0_hash c7d4d13ebc2935bcd6cbef6a697aae572597f99f29c661995510e85fbd5ce58c
Name:           mucalc
Version:        2.1
Release:        1%{?dist}
Summary:        Convenient command line calculator
License:        GPL-3.0-or-later
URL:            https://marlam.de/mucalc
Source0:        https://marlam.de/%{name}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  muParser-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
mucalc is a convenient calculator for the command line. It evaluates
mathematical expressions that are given as arguments, read from an input
stream, or typed interactively. In interactive mode, it provides line editing
with tab-completion and persistent history using GNU readline. The evaluation
of expressions is handled by the muParser math parser library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
