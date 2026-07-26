%global source0_hash c502fdd83ad59dcbcda34d4ae4f61a1a4c11baa7a69adc3445675f26b1b042c1

Name:           rpmdeplint
Version:        2.0
Release:        %autorelease
Summary:        Tool to find errors in RPM packages in the context of their dependency graph
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-ci/rpmdeplint
Source0:        %{pypi_source rpmdeplint}
BuildArch:      noarch

# The base package is just the CLI, which pulls in the rpmdeplint
# Python modules to do the real work.
Requires:       python3-rpmdeplint = %{version}-%{release}

%description
Rpmdeplint is a tool to find errors in RPM packages in the context of their
dependency graph.

%package -n python3-rpmdeplint
%{?python_provide:%python_provide python3-rpmdeplint}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  make
# These rpms don't provide python3.11dist(librepo|solv)
# https://bugzilla.redhat.com/show_bug.cgi?id=2237481
BuildRequires:  python3-librepo
BuildRequires:  python3-solv
Requires:       python3-librepo
Requires:       python3-solv

%description -n python3-rpmdeplint
Rpmdeplint is a tool to find errors in RPM packages in the context of their
dependency graph.

This package provides a Python 3 API for performing the checks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n rpmdeplint-%{version}

%generate_buildrequires
%pyproject_buildrequires -x docs -x tests

%build
%pyproject_wheel
make -C docs man

%install
%pyproject_install

mkdir -p %{buildroot}%{_mandir}/man1/
mv docs/_build/man/rpmdeplint.1 %{buildroot}%{_mandir}/man1/

%pyproject_save_files rpmdeplint

%check
%pytest tests/unit/ -k "not TestDependencyAnalyzer"
# Acceptance tests do not work in mock because they require .i686 packages.

%files
%{_bindir}/rpmdeplint
%{_mandir}/man1/rpmdeplint.1.*

%files -n python3-rpmdeplint -f %{pyproject_files}
%license COPYING
%doc README.md

%changelog
%autochangelog
