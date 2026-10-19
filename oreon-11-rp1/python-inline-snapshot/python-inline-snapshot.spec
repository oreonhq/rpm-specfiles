%global source0_hash 82432a58b7ea77a172515f5024cd26fdea8dc0f873c7a4251e4e0471a914db14
Name:           python-inline-snapshot
Version:        0.35.4
Release:        1%{?dist}
Summary:        golden master/snapshot/approval testing library which puts the values right into your source code
License:        MIT
URL:            https://15r10nk.github.io/inline-snapshot/latest
Source0:        https://files.pythonhosted.org/packages/source/i/inline_snapshot/inline_snapshot-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-inline-snapshot = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-inline-snapshot
Summary:        golden master/snapshot/approval testing library which puts the values right into your source code
%description -n python3-inline-snapshot

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir inline_snapshot-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-inline-snapshot usr/lib/python3*/site-packages/inline_snapshot* usr/lib64/python3*/site-packages/inline_snapshot* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/inline_snapshot* usr/lib64/python3*/site-packages/inline_snapshot* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-inline-snapshot -f %{oreon_filedir}/python3-inline-snapshot.list

%changelog

%autochangelog
