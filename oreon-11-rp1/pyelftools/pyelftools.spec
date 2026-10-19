%global source0_hash 5507d69b42ac7211e5db57b42f427376b2cf3e3ab9a72b9239f4fc243566869d
%global         debug_package %{nil}
Summary:        Pure-Python library for parsing and analyzing ELF files
Name:           pyelftools
Version:        0.33
Release:        1%{?dist}
License:        Unlicense AND MIT
URL:            https://github.com/eliben/pyelftools
Source0:        https://github.com/eliben/pyelftools/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 46.4.0
Requires:       python3-pyelftools = %{version}-%{release}
# /oreon:deps
%description

%package     -n python3-%{name}
Summary:        Pure-Python library for parsing and analyzing ELF files
Provides:       bundled(python3-construct) = 2.6
BuildRequires:  %{_bindir}/llvm-dwarfdump
BuildRequires:  %{_bindir}/readelf
BuildRequires:  python3-devel
BuildArch:      noarch
%description -n python3-%{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
%ifnarch x86_64
rm test/external_tools/llvm-dwarfdump
rm test/external_tools/readelf
%endif

%build

%pyproject_wheel
%install
%pyproject_install
pushd %{buildroot}%{_bindir}
mv readelf.py pyreadelf-%{python3_version}
ln -s pyreadelf-%{python3_version} pyreadelf-3
ln -s pyreadelf-3 pyreadelf
popd
%oreon_autofiles main usr/lib/python3*/site-packages/pyelftools* usr/lib64/python3*/site-packages/pyelftools* usr/bin/*

%check

%pyproject_check_import
%{__python3} test/run_all_unittests.py
%{__python3} test/run_examples_test.py
%{__python3} test/run_readelf_tests.py || :
%files
%files -n python3-pyelftools -f %{oreon_filedir}/python3-pyelftools.list

%changelog

%autochangelog
