%global source0_hash 867f94601c177236afb9d1c385f524b28ebc47e9b090cb08dfdc75dd18d5520c
Name:          python-libarchive-c
Version:       5.3
Release:        1%{?dist}
Summary:        Python interface to libarchive
License:       CC0-1.0
URL:           https://github.com/Changaco/python-libarchive-c
%global forgeurl %{url}
%global tag %{version}
%forgemeta
Source0:        https://github.com/Changaco/python-libarchive-c/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:         0001-Allow-rmd160-digest-to-be-missing-in-tests.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  libarchive-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python%{python3_pkgversion}-libarchive-c
Summary:        Python interface to libarchive
%{?python_provide:%python_provide python%{python3_pkgversion}-libarchive-c}
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pytest
Requires:      libarchive
%description -n python%{python3_pkgversion}-libarchive-c

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
%{_fixperms} %{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{?el7:export LANG=en_US.UTF-8}
pytest-%{python3_version} -s -vv tests %{?el7:-k "not test_check_archiveentry_using_python_testtar"}
%global _docdir_fmt %{name}
%files -f %{oreon_filedir}/main.list
%files -n python3-libarchive-c -f %{oreon_filedir}/python3-libarchive-c.list

%changelog

%autochangelog
