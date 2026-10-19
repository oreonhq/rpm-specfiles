%global source0_hash c0dec80a394e04ff3463c7333124482f39f2ada1a134c466330680634ee100aa
%global forgeurl https://github.com/stressapptest/stressapptest
%global commit 6714c57d0d67f5a2a7a9987791af6729289bf64e
%forgemeta
Name:           stressapptest
Version:        1.0.9
Release:        1%{?dist}
Summary:        Stressful Application Test - userspace memory and IO test
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Stressful Application Test (or stressapptest, its unix name) is a memory
interface test. It tries to maximize randomized traffic to memory from
processor and I/O, with the intent of creating a realistic high load situation
in order to test the existing hardware devices in a computer. It has been used
at Google for some time and now it is available under the Apache 2.0 license.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
