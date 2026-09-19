%global source0_hash ff7329b2362a2e8c4ef6058a69e86b934d3663228be07c7d4a794a6955b8468d

%global __cmake_in_source_build 1

Summary: Python Integration with Gamerzilla Library
Name: pylibgamerzilla
Version: 0.0.1
Release: 23%{?dist}
License: MIT
URL: https://github.com/dulsi/pylibgamerzilla
Source0: http://www.identicalsoftware.com/gamerzilla/%{name}-%{version}.tgz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: swig
BuildRequires: cmake
BuildRequires: libgamerzilla-devel
BuildRequires: python3-devel

%description
Python interface to the Gamerzilla trophy/achievement system for games.
It allows you display achievements from python games online.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake
%cmake_build

%install
mkdir -p %{buildroot}/%{python3_sitearch}
mkdir -p %{buildroot}/%{python3_sitelib}
cp %{_builddir}/%{name}-%{version}/_gamerzilla.so %{buildroot}/%{python3_sitearch}/
cp %{_builddir}/%{name}-%{version}/gamerzilla.py %{buildroot}/%{python3_sitelib}/

%files
%license LICENSE
%{python3_sitearch}/_gamerzilla.so
%{python3_sitelib}/gamerzilla.py
%{python3_sitelib}/__pycache__/gamerzilla.cpython-%{python3_version_nodots}{,.opt-?}.pyc

%changelog
%autochangelog
