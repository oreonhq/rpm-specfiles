%global source0_hash 006b9cac46470a9499797bc9c579305ae4719e0a8e495e5401dfbf1e66ce7fb4
Name:           python-markdown-exec
Version:        1.12.3
Release:        1%{?dist}
Summary:        Utilities to execute code blocks in Markdown files.
License:        ISC
URL:            https://pawamoy.github.io/markdown-exec
Source0:        https://files.pythonhosted.org/packages/source/m/markdown_exec/markdown_exec-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-markdown-exec = %{version}-%{release}
# /oreon:deps
%package -n       python3-markdown-exec+ansi
Summary:        Metapackage for python3-markdown-exec ansi extras
Requires:       python3-markdown-exec = %{version}-%{release}
Requires:       python3dist(pygments-ansi-color) >= 0.3
Provides:       python3dist(markdown-exec[ansi]) = %{version}-%{release}

%description -n python3-markdown-exec+ansi
Metapackage for python3-markdown-exec ansi extras.

%description

%package -n     python3-markdown-exec
Summary:        Utilities to execute code blocks in Markdown files.
# oreon:reqs
Requires:       python3dist(pymdown-extensions) >= 9
# /oreon:reqs
%description -n python3-markdown-exec

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir markdown_exec-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-markdown-exec usr/lib/python3*/site-packages/markdown_exec* usr/lib64/python3*/site-packages/markdown_exec* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/markdown_exec* usr/lib64/python3*/site-packages/markdown_exec* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-markdown-exec -f %{oreon_filedir}/python3-markdown-exec.list

%changelog

%autochangelog
