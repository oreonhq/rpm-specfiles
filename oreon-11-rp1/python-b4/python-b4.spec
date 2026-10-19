%global source0_hash 071823a1e904508a6fd9aaf8cc2f9a92697e1dfa270000b4d1130015b56f4137
Name:           python-b4
Version:        0.16.0
Release:        1%{?dist}
Summary:        A tool to work with public-inbox and patch archives
License:        GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/b4/b4.git/
Source0:        https://files.pythonhosted.org/packages/source/b/b4/b4-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-b4 = %{version}-%{release}
# /oreon:deps
%package -n       python3-b4+completion
Summary:        Metapackage for python3-b4 completion extras
Requires:       python3-b4 = %{version}-%{release}
Requires:       python3dist(shtab) >= 1.8
Provides:       python3dist(b4[completion]) = %{version}-%{release}

%description -n python3-b4+completion
Metapackage for python3-b4 completion extras.

%package -n       python3-b4+tui
Summary:        Metapackage for python3-b4 tui extras
Requires:       python3-b4 = %{version}-%{release}
Requires:       python3dist(textual[syntax]) >= 1.0
Requires:       python3dist(rich) >= 13.0
Provides:       python3dist(b4[tui]) = %{version}-%{release}

%description -n python3-b4+tui
Metapackage for python3-b4 tui extras.

%description

%package -n     python3-b4
Summary:        A tool to work with public-inbox and patch archives
# oreon:reqs
Requires:       python3dist(dkimpy) < 2.0
Requires:       python3dist(dkimpy) >= 1.0
Requires:       python3dist(ezgb) >= 0.2.0
Requires:       python3dist(liblore) >= 0.8
Requires:       python3dist(patatt) < 2.0
Requires:       python3dist(patatt) >= 0.6
Requires:       python3dist(pygit2) < 2.0
Requires:       python3dist(pygit2) >= 1.14
Requires:       python3dist(requests) < 3.0
Requires:       python3dist(requests) >= 2.24
# /oreon:reqs
%description -n python3-b4

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir b4-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-b4 usr/lib/python3*/site-packages/b4* usr/lib64/python3*/site-packages/b4* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/b4* usr/lib64/python3*/site-packages/b4* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-b4 -f %{oreon_filedir}/python3-b4.list

%changelog

%autochangelog
