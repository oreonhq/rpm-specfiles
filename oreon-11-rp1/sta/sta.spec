%global source0_hash 1b2e3f900ba092625c626634fe6808d685c5ee5837b224d7b90c9c888e566fdd

Name: sta
Summary: Simple statistics tool for the command line
License: MIT

%global git_date 20231130
%global git_commit 94559e3dfa97d415e3f37b1180b57c17c7222b4f
%global git_sha %(c="%{git_commit}"; echo "${c:0:7}")

Version: 0^%{git_date}.%{git_sha}
Release: 5%{?dist}

URL: https://github.com/simonccarter/sta
Source0: %{URL}/archive/%{git_commit}/sta-%{git_commit}.tar.gz

# Adds a man page for the program.
# Submitted upstream: https://github.com/simonccarter/sta/pull/13/
Patch0: sta--man-page.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cxxtest
BuildRequires: gcc-c++
BuildRequires: make

%description
sta is a lightweight, fast tool for calculating basic descriptive statistics
from the command line. Inspired by "st", this project differs in that
it is written in C++, allowing for faster computation of statistics
given larger non-trivial data sets.

Additions include the choice of biased vs unbiased estimators
and the option to use the compensated variant algorithm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

%build
autoreconf -ifv
%configure
%make_build

%install
%make_install

%check
cd test/
cxxtestgen --error-printer --have-std -o tests.cpp sta_test_1.h sta_test_2.h
g++ %{optflags} %{build_ldflags} -o tester tests.cpp
./tester

%files
%doc README.md
%license LICENCE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
