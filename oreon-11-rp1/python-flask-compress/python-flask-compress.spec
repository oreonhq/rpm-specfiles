%global source0_hash 802954fb3af048cf4ca2a3b414393bf2b98466ae8067e6654ea0aa34ba34aff5
Name:           python-flask-compress
Version:        1.25
Release:        1%{?dist}
Summary:        Compress responses in your Flask app with gzip, deflate, brotli or zstandard.
License:        MIT
URL:            https://github.com/colour-science/flask-compress
Source0:        https://files.pythonhosted.org/packages/source/f/flask_compress/flask_compress-%{version}.tar.gz
BuildArch:      noarch
Patch0:         flask-compress_setuptools-scm.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
BuildRequires:  python3dist(setuptools-scm[toml]) < 8
Requires:       python3-flask-compress = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flask-compress
Summary:        Compress responses in your Flask app with gzip, deflate, brotli or zstandard.
%description -n python3-flask-compress

%prep
%global oreon_srcdir flask_compress-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-compress usr/lib/python3*/site-packages/flask_compress* usr/lib64/python3*/site-packages/flask_compress* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_compress* usr/lib64/python3*/site-packages/flask_compress* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flask-compress -f %{oreon_filedir}/python3-flask-compress.list

%changelog

%autochangelog
