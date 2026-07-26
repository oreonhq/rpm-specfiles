%global source0_hash f3843d59589ca554b2160136c294efc16150b8b91736746f07577ad88197958d

Summary:       A set of scripts to work locally on subversion checkouts using mercurial
Name:          hgsvn
Version:       0.6.0
Release:       26%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://pypi.python.org/pypi/hgsvn/
Source0:       https://files.pythonhosted.org/packages/source/h/hgsvn/hgsvn-%{version}.tar.gz
Patch:         0001-Convert-to-pytest.patch
BuildArch:     noarch
Requires:      mercurial >= 1.4.3
Requires:      subversion
Requires:      python3-hglib
Requires:      python3-setuptools
# Needed in %%check
BuildRequires: mercurial >= 1.4.3
BuildRequires: python3-devel
BuildRequires: python3-hglib
BuildRequires: python3-pytest
BuildRequires: subversion

%description
This set of scripts allows to work locally on subversion managed
projects using the mercurial distributed version control system.

Why use mercurial? You can do local (disconnected) work, pull the
latest changes from the subversion server, manage private branches,
submit patches to project maintainers, etc. And of course you have
fast local operations like hg log and hg annotate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l %{name}

%check
%pyproject_check_import
%pytest

%files -f %{pyproject_files}
%doc AUTHORS.txt README.txt TODO.txt
%{_bindir}/hgimportsvn
%{_bindir}/hgpullsvn
%{_bindir}/hgpushsvn

%changelog
%autochangelog
