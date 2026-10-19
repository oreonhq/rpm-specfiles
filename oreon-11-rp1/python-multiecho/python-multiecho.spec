%global source0_hash 9783241951e43ff0bcb6855c1e375197df6c759bf68ff3f123a946a348db6a94
%bcond tests 0
Name:           python-multiecho
Version:        0.31
Release:        1%{?dist}
Summary:        Combine multi-echoes from a multi-echo fMRI acquisition
License:        Apache-2.0 OR MIT
URL:            https://github.com/Donders-Institute/multiecho
Source0:        https://github.com/Donders-Institute/multiecho/archive/%{version}/multiecho-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
MRI data acquisitions can involve multiple volumes acquired at different echo
times. Typically, subsequent processing pipelines assume data to be acquired at
a single echo time. This package provides a library and command-line tool to
combine multiple echoes from a multi-echo (BOLD f)MRI acquisition.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 62.2.0
Requires:       python3-multiecho = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-multiecho
Summary:        Combine multi-echoes from a multi-echo fMRI acquisition
%description -n python3-multiecho %{common_description}

%prep

%autosetup -p1
# Remove the shebang from the multiecho.combination module; upstream seems to
# have intended it to be directly executable as a script when working on the
# source, but it will not be installed with the executable bit set, so the
# shebang is useless. When packaged, we have the entry point “mecombine”
# anyway.
sed -r -i '1{/^#!/d}' multiecho/combination.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-multiecho usr/lib/python3*/site-packages/multiecho* usr/lib64/python3*/site-packages/multiecho* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/multiecho* usr/lib64/python3*/site-packages/multiecho* usr/bin/*

%check

%if %{with tests}
%pytest
%endif
%files
%files -n python3-multiecho -f %{oreon_filedir}/python3-multiecho.list

%changelog

%autochangelog
