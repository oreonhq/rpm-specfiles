%global source0_hash 9ce0671d1eddf31fdd3d7c40aaa19ef74acd64e625ef061d5e1f927a1e099447
%bcond tests 1
Name: pulp-cli
Version: 0.37.0
Release:        1%{?dist}
Summary:        Command line interface to talk to the Pulp 3 REST API
License: GPL-2.0-or-later
URL: https://github.com/pulp/%{name}
BuildArch: noarch
Source0:        https://github.com/pulp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Recommends: pulp-cli-deb
Recommends: python3-pygments
Recommends: python3-click-shell
Recommends: python3-secretstorage
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pulp-cli = %{version}-%{release}
# /oreon:deps
%description
%{name} provides the "pulp" command, able to communicate with the Pulp3 API in
a more natural way than plain http. Specifically, resources can not only be
referenced by their href, but also their natural key (e.g. name). It also
handles waiting on tasks on behalf of the user.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove the Python version upper bound to enable building with new versions in Fedora
sed -i '/requires-python =/s/,<3\.[0-9]\+//' pyproject.toml

# Remove upper version bound on setuptools to enable building with new versions in Fedora
sed -i '/requires =.*setuptools/s/<[0-9]\+//' pyproject.toml

# Remove upper version bound on packaging to enable building with new versions in Fedora
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml

# Remove all bounds on test dependencies; we must use what we have
sed -r -Ei 's/^([a-zA-Z0-9._-]+).*/\1/' test_requirements.txt

%build

%pyproject_wheel
%install
%pyproject_install
for shell_path in \
        bash:%{bash_completions_dir}/pulp \
        fish:%{fish_completions_dir}/pulp.fish \
        zsh:%{zsh_completions_dir}/_pulp; do
    shell="${shell_path%%:*}"
    path="${shell_path#*:}"
    dir="${path%/*}"
    install -m 755 -d "%{buildroot}${dir}"
    PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _PULP_COMPLETE="${shell}_source" \
    %{__python3} -c \
    "import sys; sys.argv = ['pulp']; from pulp_cli import main; sys.exit(main())" \
    > "%{buildroot}${path}"
done
%oreon_autofiles main
%if %{with tests}
%check

%pyproject_check_import pulp_cli
%pytest -m help_page
%endif
%files

%changelog

%autochangelog
