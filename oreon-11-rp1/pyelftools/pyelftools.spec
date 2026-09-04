%global source0_hash 5507d69b42ac7211e5db57b42f427376b2cf3e3ab9a72b9239f4fc243566869d

# main package is archful to run tests everywhere but produces noarch packages
%global         debug_package %{nil}

Summary:        Pure-Python library for parsing and analyzing ELF files
Name:           pyelftools
Version:        0.33
Release:        %autorelease
# elftools/construct is MIT
License:        Unlicense AND MIT
URL:            https://github.com/eliben/pyelftools
Source0:        https://github.com/eliben/pyelftools/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%global _description \
Pure-Python library for parsing and analyzing ELF files\
and DWARF debugging information.
%description   %_description

%package     -n python3-%{name}
Summary:        %{summary}
# https://github.com/eliben/pyelftools/issues/180
Provides:       bundled(python3-construct) = 2.6
BuildRequires:  %{_bindir}/llvm-dwarfdump
BuildRequires:  %{_bindir}/readelf
BuildRequires:  python3-devel
BuildArch:      noarch
%description -n python3-%{name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
%ifnarch x86_64
rm test/external_tools/llvm-dwarfdump
rm test/external_tools/readelf
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files elftools

pushd %{buildroot}%{_bindir}
mv readelf.py pyreadelf-%{python3_version}
ln -s pyreadelf-%{python3_version} pyreadelf-3
ln -s pyreadelf-3 pyreadelf
popd

%check
%pyproject_check_import
%{__python3} test/run_all_unittests.py
%{__python3} test/run_examples_test.py
# tests may fail because of differences in output-formatting
# from binutils' readelf.  See:
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#tests
%{__python3} test/run_readelf_tests.py || :

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE
%doc CHANGES
%{_bindir}/pyreadelf
%{_bindir}/pyreadelf-%{python3_version}
%{_bindir}/pyreadelf-3

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.32-1
- Prepare for Oreon 11 (RP1)
