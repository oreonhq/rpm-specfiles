%global source0_hash 660d82dcbeb8e83d1702bd97f223f761625da06111c0cc988eac6b8ab0c1b61f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-pyelftools
Version: 0.33
Release: 2%{?dist}
Summary: ELF and DWARF parsing library
License: Unlicense
URL: https://github.com/eliben/pyelftools
Source0: https://files.pythonhosted.org/packages/source/p/pyelftools/pyelftools-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3
%endif
Requires: python3

%description
ELF and DWARF parsing library.

%prep
%oreon_sha256
%autosetup -n pyelftools-%{version} -p1

%build

%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib
cp -a elftools %{buildroot}$sitelib/
find %{buildroot} -type f -exec grep -I -l -E '^#! */usr/bin/env python' {} + | while read -r f; do
  sed -i '1s|^#! */usr/bin/env python.*|#!/usr/bin/python3|' "$f"
done
%oreon_filelist
while read -r f; do
  case "$f" in
    *.py) printf '%s\n' "$(dirname "$f")/__pycache__/*" ;;
  esac
done < %{_builddir}/%{name}.files | sort -u >> %{_builddir}/%{name}.files

%files -f %{_builddir}/%{name}.files
%license LICENSE
