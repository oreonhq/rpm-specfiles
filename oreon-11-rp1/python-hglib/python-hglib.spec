%global source0_hash b18bd1ed53c90ee57d5714d66ad6bb72b64e930d4aeca9830892c08bb28da608

Summary:        Mercurial Python library
Name:           python-hglib
Version:        2.6.2
Release:        24%{?dist}
License:        MIT
URL:            http://selenic.com/repo/python-hglib
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch:          0001-hglib-tests-migrate-away-from-unmaintained-nose.patch
Patch:          0001-hglib-tests-remove-deprecated-constructions.patch
Patch:          0001-Use-raw-string-to-avoid-invalid-escape-sequence.patch
BuildArch:      noarch
BuildRequires:  mercurial
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurials command server for communication with
hg.

%package     -n python3-hglib
Summary:        Mercurial Python library
%description -n python3-hglib
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurials command server for communication with
hg.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l hglib

%check
%pyproject_check_import

%pytest

%files -n python3-hglib -f %{pyproject_files}

%changelog
%autochangelog
