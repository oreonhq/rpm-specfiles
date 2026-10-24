%global source0_hash 4e57f39797fd5d9e2d22b8806a252d7c0106c936039d1e71c8c6b8008e695c0a
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python-systemd
Version: 235
Release: 1%{?dist}
Summary: Python bindings for systemd
License: LGPL-2.1-or-later
URL: https://github.com/systemd/python-systemd
Source0: https://files.pythonhosted.org/packages/10/9e/ab4458e00367223bda2dd7ccf0849a72235ee3e29b36dce732685d9b7ad9/systemd-python-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: pkgconf
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: systemd-devel
BuildRequires: patchelf
%endif

Provides: python3-systemd = %{version}-%{release}
Requires: python3
Requires: systemd

%description
python-systemd talks to libsystemd.

%prep
%oreon_sha256
%autosetup -n systemd-python-%{version} -p1
cat > pyproject.toml << 'EOF'
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
EOF

%build
%oreon_py_build

%install
%oreon_py_install
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    patchelf --remove-rpath "$f"
  fi
done
%oreon_py_save_files systemd

%files -f %{oreon_py_files}
%license LICENSE.txt
