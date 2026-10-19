%global source0_hash aad8b69a0b9969edb62db0d1752354c0d50717b10e0cbb00e2a958381b9fc6b9
Name:           python-argcomplete
Version:        3.7.2
Release:        1%{?dist}
Summary:        Bash tab completion for argparse
License:        ...
URL:            https://github.com/kislyuk/argcomplete
Source0:        https://files.pythonhosted.org/packages/source/a/argcomplete/argcomplete-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-argcomplete = %{version}-%{release}
# /oreon:deps
%package -n       python3-argcomplete+test
Summary:        Metapackage for python3-argcomplete test extras
Requires:       python3-argcomplete = %{version}-%{release}
Provides:       python3dist(argcomplete[test]) = %{version}-%{release}

%description -n python3-argcomplete+test
Metapackage for python3-argcomplete test extras.

%description

%package -n     python3-argcomplete
Summary:        Bash tab completion for argparse
%description -n python3-argcomplete

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir argcomplete-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-argcomplete usr/lib/python3*/site-packages/argcomplete* usr/lib64/python3*/site-packages/argcomplete* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/argcomplete* usr/lib64/python3*/site-packages/argcomplete* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-argcomplete -f %{oreon_filedir}/python3-argcomplete.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.3-1
- Import
