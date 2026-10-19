%global source0_hash 7ced054af610c442cc78fe82ba36a3f35c4884b35335faff3a670117d9d49279
Name:           python-rignore
Version:        0.8.1
Release:        1%{?dist}
Summary:        Python bindings for the ignore crate
License:        MIT
URL:            https://github.com/patrick91/rignore
Source0:        https://github.com/patrick91/rignore/archive/v%{version}/rignore-%{version}.tar.gz
%global common_description %{expand:
rignore is a Python module that provides a high-performance, Rust-powered file
system traversal functionality. It wraps the Rust ignore crate using PyO3,
offering an efficient way to walk through directories while respecting various
ignore rules.}
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core
BuildRequires:  tomcli
# /oreon:deps
%description %{common_description}

%package -n     python3-rignore
Summary:        Python bindings for the ignore crate
License:        %{shrink:
                MIT AND
                Unicode-DFS-2016 AND
                (MIT OR Apache-2.0) AND
                (Unlicense OR MIT)
                }
%description -n python3-rignore %{common_description}

%prep

%autosetup -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem dependency-groups.dev \
    '(pytest-cov|coverage)\b.*'

%build -p

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%install
%pyproject_install
%oreon_autofiles python3-rignore usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-rignore -f %{oreon_filedir}/python3-rignore.list

%changelog

%autochangelog
