%global source0_hash ba1c1a2d618bca5c406647c83b89f07cc8810fa506a50622a6993ba130c1de11
Name:           python-soundfile
Version:        0.14.0
Release:        1%{?dist}
Summary:        An audio library based on libsndfile, CFFI and NumPy
License:        ...
URL:            https://github.com/bastibe/python-soundfile
Source0:        https://files.pythonhosted.org/packages/source/s/soundfile/soundfile-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-soundfile = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-soundfile
Summary:        An audio library based on libsndfile, CFFI and NumPy
%description -n python3-soundfile

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir soundfile-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-soundfile usr/lib/python3*/site-packages/soundfile* usr/lib64/python3*/site-packages/soundfile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/soundfile* usr/lib64/python3*/site-packages/soundfile* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-soundfile -f %{oreon_filedir}/python3-soundfile.list

%changelog

%autochangelog
