%global source0_hash 92d00b33e2fb247ca49facc824999fa0bc7181a3cdf6ef65c4671ec1633c0bf2

%global pkg jedi

%global commit e942a0e410cbb2a214c9cb30aaf0e47eb0895b78
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210503

Name:           emacs-%{pkg}
Version:        0.3.0
Release:        0.18.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Python auto-completion for Emacs

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://tkf.github.io/%{name}/
Source0:        https://github.com/tkf/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        %{pkg}-init.el
# Remove useless dependency on argparse module (in Python standard library)
Patch0:         %{name}-0.3.0-python_requires.patch
# Invoke system jediepcserver
Patch1:         %{name}-0.2.8-jediepcserver.patch

BuildRequires:  emacs
BuildRequires:  emacs-auto-complete
BuildRequires:  emacs-epc
BuildRequires:  emacs-python-environment
BuildRequires:  python3-devel
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-auto-complete
Requires:       emacs-epc
Requires:       emacs-python-environment
Requires:       %{py3_dist jediepcserver}
BuildArch:      noarch

%description
Jedi.el is a Python auto-completion package for Emacs. It aims at helping your
Python coding in a non-destructive way. It also helps you to find information
about Python objects, such as docstring, function arguments and code location.

%package -n python3-jediepcserver
Summary:        Jedi EPC server
Provides:       jediepcserver = %{version}-%{release}

%description -n python3-jediepcserver
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

# Remove shebang
sed -i.orig -e 1d jediepcserver.py && \
touch -r jediepcserver.py.orig jediepcserver.py && \
rm jediepcserver.py.orig

%generate_buildrequires
%pyproject_buildrequires -t

%build
%{_emacs_bytecompile} %{pkg}-core.el %{pkg}.el

%pyproject_wheel

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* %{pkg}-core.el* setup.py -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
ln -s %{python3_sitelib}/jediepcserver.py $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/jediepcserver.py

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el

%pyproject_install
%pyproject_save_files jediepcserver

%check
export PYTEST_ADDOPTS="--deselect=test_jediepcserver.py::test_epc_server_runs_fine_in_virtualenv"
%tox

%files
%doc CONTRIBUTING.md README.rst
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%files -n python3-jediepcserver -f %{pyproject_files}
%{_bindir}/jediepcserver

%changelog
%autochangelog
