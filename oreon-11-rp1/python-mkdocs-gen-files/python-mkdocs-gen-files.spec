%global source0_hash 57d7ff2229e23d077e46d14a33db6d37c8823f6ce1a503c874c1764a71679763
Name:           python-mkdocs-gen-files
Version:        0.6.1
Release:        1%{?dist}
Summary:        MkDocs plugin to programmatically generate documentation pages during the build
License:        MIT
URL:            https://github.com/oprypin/mkdocs-gen-files
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_gen_files/mkdocs_gen_files-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-gen-files = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-gen-files
Summary:        MkDocs plugin to programmatically generate documentation pages during the build
# oreon:reqs
Requires:       python3dist(mkdocs) <= 1.6.1
Requires:       python3dist(mkdocs) >= 1.4.1
Requires:       python3dist(properdocs) >= 1.6.5
# /oreon:reqs
%description -n python3-mkdocs-gen-files

%prep
%global oreon_srcdir mkdocs_gen_files-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-gen-files usr/lib/python3*/site-packages/mkdocs_gen_files* usr/lib64/python3*/site-packages/mkdocs_gen_files* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_gen_files* usr/lib64/python3*/site-packages/mkdocs_gen_files* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-gen-files -f %{oreon_filedir}/python3-mkdocs-gen-files.list

%changelog

%autochangelog
