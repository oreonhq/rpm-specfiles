%global source0_hash f1c9417c62111e40a81c482c692c5cdd131ff93317baa993044cb291912ebba3
Name:           python-diff-cover
Version:        10.5.1
Release:        1%{?dist}
Summary:        Run coverage and linting reports on diffs
License:        Apache-2.0
URL:            https://github.com/Bachmann1234/diff-cover
Source0:        https://files.pythonhosted.org/packages/source/d/diff_cover/diff_cover-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.7
Requires:       python3-diff-cover = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-diff-cover
Summary:        Run coverage and linting reports on diffs
%description -n python3-diff-cover

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir diff_cover-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-diff-cover usr/lib/python3*/site-packages/diff_cover* usr/lib64/python3*/site-packages/diff_cover* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/diff_cover* usr/lib64/python3*/site-packages/diff_cover* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-diff-cover -f %{oreon_filedir}/python3-diff-cover.list

%changelog

%autochangelog
