%global source0_hash ee8eddc271fe87142a5cb3af86561f8d0ca41c8bc9215c69c93c50d8e4902e0d
Name:           python-glymur
Version:        0.14.8
%global srcversion %(echo '%{version}' | sed -r 's/\\.(post)/\\1/')
Release:        1%{?dist}
Summary:        Interface to the OpenJPEG library for working with JPEG 2000 files
License:        MIT
URL:            https://github.com/quintusdias/glymur
Source0:        https://github.com/quintusdias/glymur/archive/v%{version}/glymur-%{version}.tar.gz
Source1:        jp2dump.1
Source2:        jpeg2jp2.1
Source3:        tiff2jp2.1
%global debug_package %{nil}
ExcludeArch:    %{ix86}
%if %{defined fc42}
%global no_pep_639_backend 1
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 60
BuildRequires:  python3dist(setuptools-scm) >= 8.0
Requires:       python3-glymur = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-glymur
Summary:        Interface to the OpenJPEG library for working with JPEG 2000 files
BuildArch:      noarch
Requires:       openjpeg2
Requires:       libtiff
Recommends:     %{py3_dist gdal}
%description -n python3-glymur

%prep

%autosetup -p1
%if 0%{?no_pep_639_backend}
tomcli set pyproject.toml del project.license
%endif

%install
%pyproject_install
install -m 0644 -p -D -t '%{buildroot}%{_mandir}/man1' \
    '%{SOURCE1}' '%{SOURCE2}' '%{SOURCE3}'
%oreon_autofiles python3-glymur usr/lib/python3*/site-packages/glymur* usr/lib64/python3*/site-packages/glymur* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/glymur* usr/lib64/python3*/site-packages/glymur* usr/bin/*

%build

%pyproject_wheel
%check

%pytest -n auto -rs -v
%files
%files -n python3-glymur -f %{oreon_filedir}/python3-glymur.list

%changelog

%autochangelog
