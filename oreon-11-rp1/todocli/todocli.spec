%global source0_hash ab29a5d2389aad705a8d260af5df58006e5905ee5881e0ea920cf6035f62fda2

%global commit ab9bbbda643b99681c642ba5350730e5bdbfdec7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global project todo.py
%global owner okulbilisim
%global date 20171025

Name:           todocli
Version:        0.1
Release:        39.%{date}git%{shortcommit}%{?dist}
Summary:        Command line To Do application

License:        MIT
URL:            https://github.com/okulbilisim/todo.py
Source0:        https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{commit}.tar.gz
Patch0:         todocli-fix-version.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A To Do command line application with SQLite back end written in Python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{project}-%{commit}
%patch -P0 -p1
#Remove egg.info
rm -rf %{name}.egg.info

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 0644 todocli.1 %{buildroot}/%{_mandir}/man1/
 
%files
%doc README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/* 
%{python3_sitelib}/*

%changelog
%autochangelog
