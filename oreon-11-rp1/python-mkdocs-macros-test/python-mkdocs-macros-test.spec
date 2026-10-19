%global source0_hash c5aba3cd060f28a9804d14ff0eda38287c83373529a91dbee922038aead422f0
%global commit ebf273bbfc52ece3bd4f341829e63c09a0555b47
Name:           python-mkdocs-macros-test
Version:        0.1.0
Release:        1%{?dist}
Summary:        Test macros library for the MkDocs macros plugin
License:        MIT
URL:            https://github.com/fralau/mkdocs-macros-test
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs-macros-test/mkdocs-macros-test-%{version}.tar.gz
Source1:        %{url}/raw/%{commit}/LICENSE.md
Source2:        %{url}/raw/%{commit}/README.md
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-macros-test = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-macros-test
Summary:        Test macros library for the MkDocs macros plugin
%description -n python3-mkdocs-macros-test

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs-macros-test-%{version}
cp -p %SOURCE1 %SOURCE2 .

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-macros-test usr/lib/python3*/site-packages/mkdocs_macros_test* usr/lib64/python3*/site-packages/mkdocs_macros_test* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_macros_test* usr/lib64/python3*/site-packages/mkdocs_macros_test* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-mkdocs-macros-test -f %{oreon_filedir}/python3-mkdocs-macros-test.list

%changelog

%autochangelog
