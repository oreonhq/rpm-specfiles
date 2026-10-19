%global source0_hash 087b58a9afe076bb08e2d726478e1f16cb928d67ffa9092817e033c335de522a
Name:           python-libcst
Version:        1.9.0
Release:        1%{?dist}
Summary:        A concrete syntax tree with AST-like properties for Python 3.0 through 3.15 programs.
License:        MIT
URL:            https://github.com/Instagram/LibCST
Source0:        https://files.pythonhosted.org/packages/source/l/libcst/libcst-%{version}.tar.gz
Source1:        python-libcst-%{version}-vendor.tar.xz
%global source1_hash be934874216d1ffa39987553130eac30eb1f0e316dd6bf2b5c13e89d5f0a2633
Patch:          libcst-fix-metadata.diff
Patch:          One-pyyaml-to-rule-them-all.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-libcst = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-libcst
Summary:        A concrete syntax tree with AST-like properties for Python 3.0 through 3.15 programs.
# oreon:reqs
Requires:       python3dist(pyyaml) >= 5.2
Requires:       python3dist(pyyaml) >= 6.0.3
Requires:       python3dist(pyyaml-ft) >= 8.0.0
# /oreon:reqs
%description -n python3-libcst

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libcst-%{version}
tar xf %{SOURCE1}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-libcst usr/lib/python3*/site-packages/libcst* usr/lib64/python3*/site-packages/libcst* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/libcst* usr/lib64/python3*/site-packages/libcst* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-libcst -f %{oreon_filedir}/python3-libcst.list

%changelog

%autochangelog
